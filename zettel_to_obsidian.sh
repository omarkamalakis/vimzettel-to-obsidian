#!/bin/sh

for i in *.wiki; do
	python ~/zettelconvert/zettel_to_obsidian.py "$i"
	echo "Converted!"
done
