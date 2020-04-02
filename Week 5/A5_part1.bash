#!/bin/bash

awk '/gmail.com/{printf("%s matched\n", $0)}' /home/$USER/Assignment5/people.txt
