#!/bin/sh

TOPLEFT=`tput cup 0 0`
NORMAL=`tput sgr0`
RED=`tput setaf 1`
GREEN=`tput setaf 2`
BROWN=`tput setaf 3`
BLUE=`tput setaf 4`
MAGENTA=`tput setaf 5`
CYAN=`tput setaf 6`
WHITE=`tput setaf 7`
BOLD=`tput bold`

clear
while true
do

	IFS=""
	echo -ne "$TOPLEFT$NORMAL"

	COLS=`tput cols`	
	FORMAT="%-"$COLS"s\\n"
	echo "Press Ctrl+C to exit" | awk "{ printf(\"$FORMAT\", \$0) }"
	echo -ne `/usr/bin/sensors | 
		awk "{ printf(\"$FORMAT\", \\$0) }" | 

		sed -r "s/( |:)([ +.0-9-]+)(.{1,3}[VMC])(.*)/\1$BOLD$CYAN\2$NORMAL$CYAN\3$NORMAL\4/g" |
		sed -r "s/= ([ +.0-9-]+)(.{0,4})([,\)])/= $BOLD$GREEN\1$NORMAL$GREEN\2$NORMAL\3/g" |
		sed -r "s/sensor = (.*$)/sensor = $GREEN\1$NORMAL/g" |

		sed -r "s/^(.*):/$BOLD$BROWN\1$NORMAL:/g" |
		sed -r "s:(ALARM):$BOLD$RED\1$NORMAL:g"
	`

	sleep 1s
done
