import platform
from setuptools import setup, find_packages

os_libraries = {
    # pip_system_certs works with venv. for conda use: python-certifi-win32
    'Windows': ['python-magic-bin'],
    'Linux': ['python-magic']
}

os_specific_requirements = os_libraries[platform.system()]


setup(
    name="pysnow",
    version = "0.7.17",
    description = "ServiceNow HTTP client library",
    authors = ["Robert Wikman <rbw@vault13.org>"],
    license = "MIT",
    readme = "README.md",
    homepage = "https://github.com/rbw/pysnow",
    install_requires=[
         "requests",
         "oauthlib",
         "requests-oauthlib",
         "six",
         "ijson",
         "pytz",
         "twine",
         "sphinx",
         "nose",
         "httpretty",
         "pytest",
         "pytest-cov"
    ] + os_specific_requirements,
)