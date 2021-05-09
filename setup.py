from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in client_info/__init__.py
from client_info import __version__ as version

setup(
	name='client_info',
	version=version,
	description='Frappe App to gather client details such as device, browser and location information.',
	author='Nithyanand K N',
	author_email='3396079+knnithyanand@users.noreply.github.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
