#!/bin/bash
#title:         connections.sh
#description:   Netstat Script
#author:        R12W4N
#==============================================================================
[ "$DEBUG" == 'true' ] && set -x
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
BLUE=`tput setaf 4`

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

function trap_ctrlc ()
{
    echo "Ctrl-C caught...performing clean up"
 
    echo "Doing cleanup"
    trap "kill 0" EXIT
    exit 2
}
trap "trap_ctrlc" 2 


netstat -lnutp | grep 'tunnel' | grep -v 'tcp6'
