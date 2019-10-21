# Cloudmesh Compute-Azure

##Goal

Extend the current cloudmesh-compute-azure to include security group functions. 

##Progress
### Week 8 October 14
* Implemented a script using azure python libraries to start compute service without cloudmesh
* Found the methods needed to create security group in azure package
* Successfullly created security group when creating vm 

##TODO
* Attach security group when starting compute service(create vm)
* Integrate the script with cloudmesh-compute-azure
* Test the functionality of cloudmesh-compute-azure
* Benchmark the finished cloudmesh-compute-azure

##Reference
* [Create vm on azure using python](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/python#)
* [Issue/Example related to NSG creation on github-azure](https://github.com/MicrosoftDocs/azure-docs/issues/30555)
* [Discussion regarding NSG security rules](https://stackoverflow.com/questions/55970074/issues-with-network-security-group-deployment-using-python-networksecuritygrou)
* [Azure documentation-Security Group](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)
* [Azure Security Rules Operation class -python](https://docs.microsoft.com/en-us/python/api/azure-mgmt-network/azure.mgmt.network.v2017_03_01.operations.securityrulesoperations?view=azure-python)