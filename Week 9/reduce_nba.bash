#!/bin/bash

awk -F"," '{ printf("%s,%s,%s,%s\n",$1, $2, $3, $6) }' nba_full.csv > nba.csv 
