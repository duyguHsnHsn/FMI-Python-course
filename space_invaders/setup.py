from setuptools import setup

setup(
    name='space_invaders',
    version='0.1.0',
    py_modules=['spinv'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'spinv = spinv:cli',
        ],
    },
)