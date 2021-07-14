#/bin/bash

#Make sure to start wireshark first and record traffic
while read -r line; do
	echo $line
	firefox --new-tab $line &
	sleep 30
	killall firefox-esr
	sleep 10
	rm -Rf /home/user/.mozilla/firefox/qttfpds2.default-ers/sessionstore-backups
done < websiteshttps.txt
