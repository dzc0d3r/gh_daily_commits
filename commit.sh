#!/bin/bash

date +"%D %T" > date.txt
echo "" > date.txt
git add .
git commit -m  "`date`"
#git push -u origin master
