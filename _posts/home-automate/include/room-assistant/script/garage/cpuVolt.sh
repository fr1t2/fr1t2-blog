#!/bin/bash

THROTTLED=`/opt/vc/bin/vcgencmd get_throttled |cut -d "=" -f2`
RESULTS=0

if [[ "$THROTTLED" != *"0x0"*  ]];then
	RESULTS=1
fi

echo $RESULTS

