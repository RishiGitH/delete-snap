# Project Title

Genearating a snap. Snaps are containerised software packages that are simple to create and install. They auto-update and are safe to run.

## Getting Started

These instructions will help you create a snap app  and publish it to the live ubuntu store .

### Prerequisites

You need snap installed on your system :-
```
 sudo apt update
 sudo apt install snapd
```

To list snaps on the sysem :-
```
 snap ls
```

Git clone this repo :-
```
git clone https://github.com/RishiGitH/rishi-requests-test.git
```

You need an ubuntu one account to publish the app check 

https://snapcraft.io/login


### Installing

A step by step series of examples that tell you how to generate your first snap

Make a copy of your snapcraft.yaml and Initialize your snap 
```
cp snap/snapcraft.yaml  snapcraft.yaml
snap init
```

You will see a  snap folder which will have a blank snapcraft.yaml either replace it with current one or edit it as
per your requirements .Edit the name in snapcraft.yaml from rishi-requests-test to anything else if u want to register it 
```
mv snapcraft.yaml snap/snapcraft.yaml
```
Generate .snap
```
sudo snapcraft
```

You will find a .snap file in the same directory that you ran the snapcraft command. You can inspect the contents to ensure it contains all of the application's assets
cmd to inspect contents
```
unsquashfs -l *.snap
```

Install the snap
```
sudo snap install --devmode --dangerous *.snap
```

List your installed snaps to confirm
```
snap list
```

Run the snap
```
yoursnapname -h
```

Make sure the name matches what has been used previously 

Create an ubuntu one account then login with username and pass
```
snapcraft login
```
Register your app
```
snapcraft register yoursnapname
```
Deploy the app 
```
snapcraft push --release edge *.snap
```

You can check it on the ubuntu app store any version above Ubuntu 18.04 or install it on any system

```
snap install yoursnapname
```


## Additional Info
```
snap get name
snap set name -- config details set and get package
```

Downgrade a snap
```
sudo snap revert hello - downgrade
```
Going inside the snap vm 
```
multipass list
multipass start snapcraft-snapname
multipass stop snapcraft-snapname
```

You may find it useful to shell into a VM using multipass shell YOURVMNAME e.g. multipass shell snapcraft-rubber-band-async. Then you get a bash

 You should find the prime snap build directory via cd /root/prime though you will need to sudo bash first.
 


 ## Release a stable upgrade verison
 
 edit the version in snap/snapcraft.yaml

generate and push new snap 
```
sudo snapcraft 
sudo snapcraft push --release=stable rishi-requests-test_0.2_amd64.snap
```


## Snapcraft yaml makeup and details 
--plugin
Used to simplify and accelerate your build on commonly used frameworks and platforms. A plugin will often add, and may require, its own additional metadata. See Snapcraft plugins for more details.
Examples: python, go, java, cmake, autotools

--source
The location of the file or files needed to build your part, it can can refer to a directory tree, a compressed archive, or a revision control repository
Examples: ., https://github.com/coderholic/pyradio.git, gnu-hello.tar.gz

--build-packages
A list of the packages required to build your part. Package names are those used by the build host’s package manager, such as apt or dnf.
Examples: [pkg-config, libncursesw5-dev, sed, ]

--stage-packages
A list of the packages required by your part to run. Package names are those used by the build host’s package manager, such as apt or dnf.
Examples: [gnome-themes-standard, libncursesw5, dbus]



