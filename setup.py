from setuptools import setup, find_packages


setup(
    name='tangled.contrib',
    version='0.1.dev0',
    description='Tangled namespace for contributed packages',
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
    [tangled.scripts]
    contrib = tangled.contrib.scripts:Contrib

    """,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
