#!/bin/bash

echo `df -h --output=avail --total |awk 'END {print $1}' |cut -f3`
