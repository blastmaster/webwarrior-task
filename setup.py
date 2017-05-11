from setuptools import setup

setup(
        name='webwarrior-task',
        version='0.0.1',
        description='webwarrior-task - A web frontend for taskwarrior.',
        long_description='',
        packages=['webwarrior'],
        install_requires=[
            'flask',
            'taskw',
        ],
)
