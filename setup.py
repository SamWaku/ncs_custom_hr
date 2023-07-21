from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ncs/__init__.py
from ncs import __version__ as version

setup(
	name="ncs",
	version=version,
	description="non",
	author="samuel wakumelo",
	author_email="samuelwaku1st@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
