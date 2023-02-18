from setuptools import setup

setup(
    name='hangman',
    version='0.1.0',
    py_modules=['hangman'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'hangman = hangman:cli',
        ],
    },
)