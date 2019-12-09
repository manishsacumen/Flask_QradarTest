#!/bin/bash

# Checks if PATHSTART variable is set or python is not 2.7 & installs python 2.7 if it does not exist.
PYTHON_VERSION=`python -c "import sys;v='{t[0]}.{t[1]}'.format(t=list(sys.version_info[:2]));sys.stdout.write(v)";`
echo "version of python is $PYTHON_VERSION"
if [[ -z "$PATHSTART" || "$PYTHON_VERSION" != "2.7" ]] ; then

    # Need to check if Python 2.7 already exists
    if ! rpm -qa | grep python2.7 > /dev/null ; then
          # No python 2.7 - need to install the rpms from /src_deps/init/python27_rpms
          # This command should auto resolve rpm dependencies
          echo "Installing python2.7 rpms"
          yum -y localinstall --disablerepo=* /src_deps/init/python27_rpms/*.rpm
    fi
fi
