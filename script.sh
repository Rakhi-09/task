#!/bin/bash
usage() { echo "Usage: $0 [-a name1] [-b name2] [-c name3]" 1>&2; exit 1; }


while getopts ":a:b:c:" opt; do
  case $opt in
    a) USER1="$OPTARG"
    ;;
    b) USER2="$OPTARG"
    ;;
    c) USER3="$OPTARG"
    ;;
    \?) usage
    ;;
    
  esac
done
if [ -z "${USER1}" ] || [ -z "${USER2}" ] || [ -z "${USER3}" ]; then
    usage
fi
echo " Env var from Python script"
echo "USER1=$USER1"
echo "USER2=$USER2"
echo "USER3=$USER3"

