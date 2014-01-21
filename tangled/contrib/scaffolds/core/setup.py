from setuptools import setup, find_packages


setup(
    name='${package_name}',
    version='0.1.dev0',
    description='Tangled ${package} integration (core)',
    packages=find_packages(),
    install_requires=(
        'tangled>=${version_tangled}',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
        ),
    },
    entry_points="""
    [tangled.scripts]
    ${package} = ${package_name}.command:Command

    """,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
