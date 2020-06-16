#!/bin/bash
cd /home/m4dc0d3r/Documents/SCRIPTS/commit-every-day/
date +"%D %T" > date.txt
git add .
git commit -m  "`date`"
git push -u origin master
