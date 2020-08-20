import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="mktable2matrix",
    version="0.1.1",
    author="Guilherme Lucas",
    author_email="guilherme.slucas@gmail.com",
    description="Converts markdown table to Matrix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Guilhermeslucas/mktable2matrix",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)