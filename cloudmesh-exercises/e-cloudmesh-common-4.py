# import shell function
from cloudmesh.common.Shell import Shell


# using shell to print path
print("you are currently in "+Shell.pwd())

# using shell to print content in directory
print("this directory contains "+Shell.ls())


# using shell to create a directory
print("\n"+"adding a directory ")
print("---------------------")
Shell.mkdir("foo")

# checking mkdir usage
print(Shell.ls())


# remove the created directory
print("\n"+"Removing created directory")
print("---------------------")
Shell.rm("-r", "foo")
print(Shell.ls())

# ping google
print("\n"+Shell.ping("www.google.com"))
