#Command to set up the setup.py file:
#python3 setup.py install

from setuptools import setup, find_packages
 
setup(name = "Database", packages = find_packages())
setup(name = "Protos", packages = find_packages())
setup(name = "Service", packages = find_packages())
setup(name = "Client", packages = find_packages())
