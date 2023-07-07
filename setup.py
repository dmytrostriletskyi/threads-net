"""
Setup the package.
"""
from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as read_me:
    long_description = read_me.read()

with open('requirements/project.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    version='0.0.2',
    name='threads-net',
    description='Threads (threads.net) Python API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dmytrostriletskyi/threads',
    license='MIT',
    author='Dmytro Striletskyi',
    author_email='dmytro.striletskyi@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
