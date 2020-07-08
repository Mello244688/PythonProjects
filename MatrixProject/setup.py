import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matrix_pkg_mello244688",
    version="0.0.1",
    author="Scott Mello",
    author_email="scott.mello24@gmail.com",
    description="A small matrix algebra package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mello244688/MatrixPythonPackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)