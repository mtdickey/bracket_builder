from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='bracket_builder',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Build interactive visualizations for tournaments.",
    license="MIT",
    author="Michael Dickey",
    author_email='mtdickey17@gmail.com',
    url='https://github.com/mtdickey/bracket_builder',
    packages=['bracket_builder'],
    entry_points={
        'console_scripts': [
            'bracket_builder=bracket_builder.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='bracket_builder',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
