#!/bin/bash

date +"%D %T" > date.txt
git add .
git commit -m  '`date +"%D %T"`'
git push -u origin master
