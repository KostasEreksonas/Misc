#!/bin/sh

function displayDialog() {
	arr=("$@")
	len=${#arr[@]}
	for (( i=1; i<$len; i++ )); do
		dialog --title ${arr[0]} --infobox "Installing ${arr[$i]}" 0 0
		sleep 1
	done
}

vbox=(virtualbox-host-modules-arch \
		virtualbox-guest-iso \
		virtualbox)
read -p "Enter dialog title: " title
displayDialog $title "${vbox[@]}"
