ooni-support
============

Support scripts for OONI on M-Lab

```
sudo yum install git svn rpm-build m4
mkdir ooni-support-slicebuild # This temporary directory will be removed by slicebuild.sh
cd ./ooni-support-slicebuild
git clone --recursive https://github.com/m-lab-tools/ooni-support.git
cd ooni-support
git checkout <tag>
./package/slicebuild.sh mlab_ooni
```
