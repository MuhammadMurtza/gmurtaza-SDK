from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gmurtaza-lotr-sdk",
    version="1.0.0",
    description="A Python SDK for the Lord of the Rings API",
    author="Ghulam Murtaza",
    author_email="gmurtaza.va@gmail.com",
    packages=find_packages(),
    install_requires=["requests"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)