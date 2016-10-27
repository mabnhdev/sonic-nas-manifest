
Welcome to the SONiC NAS Host-Adapter
======================================
This SONiC repo contains the manifest file for the repo tool used to pull down sources for the SONiC network adaptation service (NAS) project. The SONiC NAS project is the switch abstraction interface (SAI) Host-Adapter originally written by Dell, and contributed to the SONiC project. It is assumed that you are familiar with Linux and have basic development knowledge.

Read the documentation
-------------------------
See [SONiC NAS Documentation](https://github.com/Azure/sonic-nas-manifest/wiki) for complete information.

Get SONiC NAS
-----------------
There are two ways to get the SONiC NAS:

- **Download and install binaries** - see [installation](#Installation) for complete information, **or**
- **Build from scratch** - see the step-by-step instructions below to build the project.
 
Build environment recommendations
---------------------------------
- Intel multi-core
- Ubuntu 16.04 or later (desktop edition with Python installed)
- 20G available free disk space
- bash (most shell commands refer to bash commands - we like csh as well)

The build environment
----------------------
### Prerequisites

Updated environment: `sudo apt-get update`
- GIT: `sudo apt-get install git`
- Repo: See http://source.android.com/source/downloading.html to install the `repo`.
```
    Make sure you have a bin/ directory in your home directory and that it is included in your path:
    $ mkdir ~/bin
    $ PATH=~/bin:$PATH
    Download the Repo tool and ensure that it is executable:
    $ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    $ chmod a+x ~/bin/repo
```
- apt-utils: `sudo apt-get install apt-utils`
- See [Docker environment setup guide](https://docs.docker.com/engine/installation/linux/ubuntulinux/) for complete information.
```
    sudo apt-get install docker.io
    sudo apt-get install docker-engine
    sudo service docker start
```
- To avoid running docker commands as root (with sudo):
```
    sudo groupadd docker ### The 'docker' group might already exist
    sudo gpasswd -a ${USER} docker ### Add your user id to the 'docker' group
    sudo service docker restart
```
- You may have to log out/in to activate the changes to groups   
- Ensure you have proper permissions to clone source file (ssh keys must be installed)

> **NOTE**: Setup your ssh keys with Github [Settings->keys](https://github.com/settings/keys) - we are using git over ssh. 

Clone the source code
---------------------
To get the source files for the SONiC NAS Host-Adapter, run the commands in an empty directory (root directory). For example *~/dev/sonic/*:
```
repo init -u ssh://git@github.com/Azure/sonic-nas-manifest.git
repo sync
```

The `repo sync` command downloads all of the source files that you need to build the SONIC NAS Host-Adapter. In addition to the source files, you will also need some binary libraries for the SAI. The SAI is currently not open sourced entirely, as it is based on Broadcom's SDK and there is no open source SAI implementation from Broadcom at this time.

All the build scripts are found in the [SONiC Build Tools repo](https://github.com/Azure/sonic-build-tools) and will be downloaded as part of the above `repo sync`.

Build the code
-----------------
Setup your path to include the *sonic-build-tools/scripts* folder (if you plan to run this command often, you could optionally add it to the .bashrc):
```
cd sonic-build-tools/scripts
export PATH=$PATH:$PWD
```

SONiC NAS Docker environment
----------------------------
To setup your Docker SONiC NAS image, use the script in the *sonic-build-tools/scripts* folder called `sonic_setup`. This script builds a docker container called `docker-sonic` which will be used by the build scripts:
```
cd sonic-build-tools/scripts/
sonic_setup
```

Test your environment
---------------------
You can run `sonic_build` in the *sonic-logging* directory (sonic-logging repo): 
```
cd sonic-logging
sonic_build -- clean binary
```

Build one repository
-----------------------
See the corresponding README.md file associated with the repo for the specific build commands, along with package dependencies.

Build all repositories
---------------------------
Issue the `sonic_build_all` command from the root directory to build all repos and create packages in the same root directory.
```
sonic_build_all
```

Installation
------------
Once all of the repos have been built, you can install the created ONIE Debian x86_64 image. You can then install all of the build packages, along with the other Debian files you downloaded earlier in the root directory.

See [SONiC NAS documentation](https://github.com/Azure/sonic-nas-manifest/wiki/Install-SONiC-Host-Adapter-on-Dell-S6000-Platform) for complete installation information.

(c) Dell 2016
