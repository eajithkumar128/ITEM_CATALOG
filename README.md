# ITEM CATALOG

Item catalog is an online application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Setting up the environment
To run the program the following softwares needs to be installed in the system.

  -  Virtual Box
  -  Vagrant 

### Install Virtual Box:

VirtualBox is the software that actually runs the VM. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

### Install Vagrant Machine:

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from vagrantup.com. Install the version for your operating system.

Windows Note: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

### Download the VM configuration
Use Github to fork and clone, or download, the repository https://github.com/udacity/fullstack-nanodegree-vm.

You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

Navigating to the FSND-Virtual-Machine directory and listing the files in it. This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows.


### Starting the virtual machine
Using the terminal, change directory using the command cd fullstack/vagrant, then type vagrant up to launch your virtual machine.

Once it is up and running, type vagrant ssh. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.

Now that you have Vagrant up and running type vagrant ssh to log into your virtual machine (VM). Change directory to the /vagrant directory by typing cd /vagrant. This will take you to the shared folder between your virtual machine and host machine.

### Load data to the database:
To load the data to the database run the following commands one by one present in the project root folder.

```sh
$ python modesNew.py
$ python DBUPLOAD.py
```

### Start the web server:
Run the "project.py" file present in the project root folder to start the web server.

```sh
$ python project.py
```

Once after starting the server open a web browser and navigate to "http://localhost:5000"

### JSON Endpoints
THis project also supports the API to fetch the category and item details in JSON format.
Visit the following URI to get the JSON data:

'''sh
JSON FORMAT FOR ALL THE CATEGORY AND ITEMS: /catalog/<int:category_id>/items/JSON
JSON FORMAT FOR PARTICULAR CATEGORY: /catalog/<int:category_id>/items/JSON
JSON FORMAT TO GET SPECIFC ITEM DETAIL: /catalog/<int:category_id>/items/<int:item_id>/JSON
'''
    
