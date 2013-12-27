import datetime
import os
import pkg_resources
import shutil
import string

from tangled.util import asset_path
from tangled.abcs import ACommand


class Contrib(ACommand):

    @classmethod
    def configure(cls, parser):
        subparsers = parser.add_subparsers(title='Contrib commands')

        new_parser = subparsers.add_parser('new')
        new_parser.add_argument('package_name')
        new_parser.add_argument('-t', '--template', default='default')
        new_parser.add_argument('-d', '--output-dir', default=None)
        new_parser.add_argument(
            '--overwrite', action='store_true', default=False)
        new_parser.add_argument(
            '--buildout', action='store_true', default=False)
        new_parser.add_argument(
            '--dry-run', action='store_true', default=False)
        new_parser.add_argument('--author', default=os.environ.get('USER', ''))
        new_parser.set_defaults(runner='new')

    def run(self):
        runner = getattr(self.args, 'runner', None)
        if runner:
            getattr(self, runner)()
        else:
            self.parser.print_help()

    def new(self):
        args = self.args
        package_name = args.package_name

        if args.template == 'default':
            qualified_package_name = 'tangled.contrib.{}'.format(package_name)
        elif args.template == 'core':
            qualified_package_name = 'tangled.{}'.format(package_name)

        output_dir = args.output_dir
        if output_dir is None:
            output_dir = os.path.join(os.getcwd(), qualified_package_name)

        relative_package_dir = qualified_package_name.replace('.', os.path.sep)
        package_dir = os.path.join(output_dir, relative_package_dir)

        if os.path.exists(output_dir):
            if args.overwrite:
                print('Overwriting {}'.format(output_dir))
                if not args.dry_run:
                    shutil.rmtree(output_dir)
            else:
                self.exit(
                    '{} exists; use --overwrite to replace'
                    .format(output_dir))

        template_dir = asset_path('tangled.contrib.templates', args.template)

        print('Using {0.template} template'.format(args))
        print('Creating package at {}...'.format(output_dir))

        if not args.dry_run:
            shutil.copytree(template_dir, output_dir)

        template_package_dir = os.path.join(
            os.path.dirname(package_dir), '__package__')
        shutil.move(template_package_dir, package_dir)

        if not args.buildout:
            os.remove(os.path.join(output_dir, 'buildout.cfg'))

        tangled_version = pkg_resources.get_distribution('tangled').version

        template_vars = {
            'package': package_name,
            'qualified_package': qualified_package_name,
            'package_dir': package_dir,
            'relative_package_dir': relative_package_dir,
            'author': args.author,
            'year': datetime.datetime.today().year,
            'version_tangled': tangled_version,
        }

        for current_dir, sub_dirs, files in os.walk(output_dir):
            for f in files:
                f = os.path.join(current_dir, f)
                with open(f) as fp:
                    content = fp.read()
                template = string.Template(content)
                content = template.substitute(template_vars)
                if args.dry_run:
                    print('# {}\n{}\n'.format(f, content))
                else:
                    with open(f, 'w') as fp:
                        fp.write(content)
