import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shapey",
    version="0.0.1",
    author="caganze",
    author_email="caganze@gmail.com",
    description=" package to draw boxes in 2d plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caganze/shapey/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"),
)