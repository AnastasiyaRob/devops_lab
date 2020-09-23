from setuptools import setup, find_packages

setup(
    name="monitor",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
             "monitor = monitor.task3:main",
        ],
    },
    install_requires=[
        # put your requirements separated by comma here
    ],
    version="0.1",
    author="Captain Jack",
    author_email="captain_jack@gmail.com",
    description="Example of the test application",
    license="MIT",
)
