#!/bin/bash

cpuTemp=`vcgencmd measure_temp |cut -d "=" -f2 |cut -d "'" -f1 | awk '{print ($1 *9/5) + 32}'`
echo $cpuTemp

