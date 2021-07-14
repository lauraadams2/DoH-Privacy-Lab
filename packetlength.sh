#!/bin/bash

for filename in /home/user/DoH-Privacy-Lab/capture09/*.txt; do
	python3 filter.py $filename >> cap09length.txt
done


