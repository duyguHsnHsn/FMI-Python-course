from setuptools import setup

setup(
    name='run-and-jump',
    version='0.1.0',
    py_modules=['raj'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'raj = raj:cli',
        ],
    },
)