from setuptools import setup

setup(
    name='coin_collector',
    version='0.1.0',
    py_modules=['concol'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'concol = concol:cli',
        ],
    },
)