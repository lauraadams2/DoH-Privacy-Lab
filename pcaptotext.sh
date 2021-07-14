#!/bin/bash

num=0
for filename in /home/user/DoH-Privacy-Lab/capture08/*.pcapng; do
	echo num: $num
	tcpdump -r $filename > website_$num.txt
	((num=num+1))
done  
