"""
Setup the package.
"""
from setuptools import find_packages, setup

def get_file_content(file_name: str, **kwargs) -> str:
    try:
        with open(file_name, **kwargs) as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f'File "{file_name}" not found.')
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f'File "{file_name}" has wrong encoding.')

read_me = get_file_content('README.md', encoding='utf-8')
requirements = get_file_content('requirements.txt').splitlines()

setup(
    version='0.0.11',
    name='threads-net',
    description='Threads (threads.net) Python API wrapper',
    long_description=read_me,
    long_description_content_type='text/markdown',
    url='https://github.com/dmytrostriletskyi/threads-net',
    project_urls={
        'Issue Tracker': 'https://github.com/dmytrostriletskyi/threads-net/issues',
        'Source Code': 'https://github.com/dmytrostriletskyi/threads-net',
        'Download': 'https://github.com/dmytrostriletskyi/threads-net/tags'
    },
    license='MIT',
    author='Dmytro Striletskyi',
    author_email='dmytro.striletskyi@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)