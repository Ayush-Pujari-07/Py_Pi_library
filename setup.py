import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Py_Pi_library"  # Name of the repository
AUTHOR_USER_NAME = "Ayush-pujari-07"
SRC_REPO = "Py_Pi_library"  # Name of the source repository
AYTHER_EMAIL = "ayush08.pujari@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AYTHER_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={
        "": "src"
    },
    packages=setuptools.find_packages(where="src")
)
