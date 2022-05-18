import setuptools

VERSION = '0.0.1' 
DESCRIPTION = 'Insync Insurance Package'
LONG_DESCRIPTION = 'A package dedicated to speed up rating in ICE.'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insyncinsurance",
    version=VERSION,
    author="Lewis Munday",
    author_email="lewis.munday@insyncinsurance.co.uk",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/insyncinsurance/insyncinsurance",
    project_urls={
        "Bug Tracker": "https://github.com/insyncinsurance/insyncinsurance/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU AGPLv3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=2.5"
)