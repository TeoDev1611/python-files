from setuptools import setup, find_packages

LONG_DESCRIPTION = 'A PACKAGE FOR USE FILE OPERATIONS FOR EXAMPLE: DELETE, DIRECTORY COPY, PASTE'
DESCRIPTION = 'MAKE FILE OPERATIONS WITH PYTHON'
VERSION = '0.1'
setup(
    name="Files",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    author="Mateo Hurtado",
    author_email='teodev1611@gmail.com', 
    license="MIT",
    url="https://teodev1611.github.io",
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