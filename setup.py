import setuptools

with open("README.md","r") as f:
    long_description = f.read()



__version__ = "0.0.0"

REPO_NAME = "Chicken-disease"
AUTHOR_USER_NAME = "BRAJ"
SRC_REPO = "cnnClassifier",
AUTHOUR_EMAIL = "braj@gmail.com"

setuptools.setup(
    mane=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOUR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)