#!/bin/bash
    # Script to update a container's PATH to use python 2.7 if
    # not already using it

    PYTHON_VERSION=$(python -V 2>&1)

    echo "Checking Python version again. If not 2.7 we need to set it as default."
    echo "Python version is: $PYTHON_VERSION"

     echo "Path before start is $PATH"
    if [ "$PYTHON_VERSION" == "Python 2.6.6" ] ; then
           # Python 2.6 is still being used - Need to update app's PATH
          export PATH="/usr/local/bin:$PATH"
          echo "Path now is $PATH"
    fi