from setuptools import setup, find_packages


setup(
    name='tangled.contrib',
    version='0.1.dev0',
    description='Tangled namespace for contributed packages',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=find_packages(),
    install_requires=(
        'tangled>=0.1.dev0',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
        ),
    },
    entry_points="""
    [tangled.scaffolds]
    contrib = tangled.contrib.scaffolds:default
    contrib-core = tangled.contrib.scaffolds:core

    """,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
