#Command to set up the setup.py file:
#python3 setup.py install

from setuptools import setup, find_packages
 
setup(name = "Database", packages = find_packages())
setup(name = "Protos", packages = find_packages())
setup(name = "Service", packages = find_packages())
setup(name = "Client", packages = find_packages())

#!/bin/bash

echo Enter the URL for which you want to find out the details
read URL
echo URL is:$URL

digURL()
{
    dig $URL +short
}

queryA ()
{
    dig $URL A  
}

queryMX ()
{
    dig $URL MX
}

queryCNAME ()
{
    dig $URL CNAME
}

queryTTL()
{
    dig +nocmd +noall +answer +ttlid $URL
}

reverseDNS8844()
{
    dig -x 8.8.4.4 
}

reverseDNS8888()
{
    dig -x 8.8.8.8 
}

echo "IP address for URL is"
digURL
echo
echo

echo "Running query A on URL, result  is"
queryA
echo
echo

echo "Running query MX on URL, result is"
queryMX
echo
echo

echo "Running query CNAME on URL, result  is"
queryCNAME
echo
echo

echo "Running query TTLID on URL, result  is"
queryTTL
echo
echo

echo "Running reverse DNS on 8.8.4.4"
reverseDNS8844
echo
echo

echo "Running reverse DNS on 8.8.8.8"
reverseDNS8888
echo
echo
