import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # adapt "myname" to something unique
    # if you want to test the upload to test-PyPI
    name="calculator-myname",
    version="0.1.0",
    author="Firstname Lastname",
    author_email="firstname.lastname@example.org",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://example.org",
    packages=setuptools.find_packages(),
    install_requires=[
        "scipy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
