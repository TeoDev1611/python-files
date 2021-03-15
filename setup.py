from setuptools import setup, find_packages
from os import path

with open('./README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
DESCRIPTION = 'MAKE FILE OPERATIONS WITH PYTHON'
VERSION = '0.3'
setup(
    name="teo-files",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    author="Mateo Hurtado",
    author_email='teodev1611@gmail.com', 
    license="MIT",
    url="https://github.com/TeoDev1611/teo-files",
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    packages=find_packages(),
    keywords=['python', 'file', 'system', 'copy', 'delete', 'os', 'file', 'py-files'],
        classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)