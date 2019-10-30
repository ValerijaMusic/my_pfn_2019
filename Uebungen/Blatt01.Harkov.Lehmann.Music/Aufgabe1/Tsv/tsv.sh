#!/bin/sh
# Harkov.Lehmann.Music
# Bearbeitungszeit: 1.5 Stunden

tail -n +2 islands.tsv > nohead.tsv
less islands.tsv | grep "hypothetical protein" > hypo.tsv
less islands.tsv | grep -v "hypothetical protein" | tail -n +2 > nothypo.tsv
cut -f 7 islands.tsv | tail -n +2 > locus.tsv
cut -f 1,2 islands.tsv | sort -u -g | tail -n +2 > ranges.tsv
