from setuptools import setup, find_packages

setup(
    name="tgcli",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot',
    ],
    entry_points={
        'console_scripts': [
            'tgcli=tgcli:main',
        ],
    },
)
