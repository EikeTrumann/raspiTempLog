#!/bin/bash
# this are the  packages used for plotting the data
# the installation takes a very long time and must be completed before the software can be used
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install libblas-dev        ## 1-2 minutes
sudo apt-get install liblapack-dev      ## 1-2 minutes
sudo apt-get install python-dev         ## Optional
sudo apt-get install libatlas-base-dev  ## Optional (speed up execution)
sudo apt-get install gfortran           ## 2-3 minutes
sudo apt-get install python-setuptools  ## ?
sudo easy_install scipy                 ## 2-3 hours
## previous might also work: python-scipy without all dependencancies
sudo apt-get install python-matplotlib  ## 1 hour
