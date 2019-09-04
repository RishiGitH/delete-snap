snapcraft.yaml file descibing everything about snap in the folder


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


snapcraft to create snap

You will find a .snap file in the same directory that you ran the snapcraft command. You can inspect the contents to ensure it contains all of the application's assets

unsquashfs -l *.snap


Install the snap

sudo snap install --devmode --dangerous *.snap

List your installed snaps to confirm

snap list

Run the snap

test-offlineimap-rishi191 -h

Make sure the name matches what has been used previously (i.e test-offlineimap-rishi191)

snapcraft login

snapcraft register test-offlineimap-rishi191

snapcraft push --release edge *.snap

snap get name
snap set name -- config details set and get package


snapcraft init

sudo snap revert hello - downgrade


multipass list
multipass start snapcraft-pynsource
multipass stop snapcraft-rubber-band-async
You may find it useful to shell into a VM using multipass shell YOURVMNAME e.g. multipass shell snapcraft-rubber-band-async. Then you get a bash

 You should find the prime snap build directory via cd /root/prime though you will need to sudo bash first.


 rishi-requests-test_0.1_amd64.snap


 snapcraft push --release=stable rishi-requests-test_0.2_amd64.snap



