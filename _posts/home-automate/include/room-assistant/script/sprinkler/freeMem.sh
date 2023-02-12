#!/bin/bash

memfree=`cat /proc/meminfo | grep MemFree | awk '{print $2}'`; 
memtotal=`cat /proc/meminfo | grep MemTotal | awk '{print $2}'`; 


awk '/MemFree/{free=$2} /MemTotal/{total=$2} END{print (free*100)/total}' /proc/meminfo

#echo $(($memfree * 100 / $memtotal))
