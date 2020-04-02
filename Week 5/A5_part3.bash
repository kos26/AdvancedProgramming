#!/bin/bash

file=A5
txtfile=/home/$USER/Assignment5

if [ -d $file ]
then
	echo "$file exists on your system, sub-directories got created in it with existing files removed."
	cd $file/
	ls | xargs rmdir
	awk -F "," '{printf("%s.%s.%s\n",$2, $1, $3)}' ../student.txt | xargs mkdir
else
	mkdir $file
	echo "$file does not exist in your system so it got created with sub-directories in it."
	cd $file/
	awk -F "," '{printf("%s.%s.%s\n",$2, $1, $3)}' ../student.txt | xargs mkdir
fi

