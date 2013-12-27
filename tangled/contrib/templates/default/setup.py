from setuptools import setup, find_packages


setup(
    name='${qualified_package}',
    version='0.1.dev0',
    description='Tangled ${package} integration',
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
    ${package} = ${qualified_package}.command:Command

    """,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
