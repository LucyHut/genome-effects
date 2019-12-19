import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fungene_mdibl",
    version="0.0.3",
    author="Lucie Hutchins",
    author_email="lucie.hutchins@yahoo.com",
    description="Functional Genomic Experiments Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdibl/fungene",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
