#!/bin/sh
# Harkov.Lehmann.Music
# Bearbeitungszeit: 3 Stunden

cut -f 3 alignments.sam  | sort -u -d | grep NODE* > references.txt

less alignments.sam | grep -v ^@ | grep NODE > aligned_only.sam

#                                               v-- uniq only matches on repeated lines, so sort first
cut -f 3 alignments.sam  |  grep -E 'NODE|\*' | sort | uniq -c | tr -s " " | tr " "  "\t" | cut -f 2,3 > references_count.tsv
#                                                              |            Umwandeln zur             |
#                                                              |____ tabulator-getrennter Ausgabe ____|

less alignments.sam | grep -v ^@ | grep NODE | cut -f 1 | sort -n | uniq -c | tr -s " " | tr " "  "\t" | cut -f 2,3 > reads_n_alignments.tsv

cut -f 1 reads_n_alignments.tsv | sort | uniq -c | tr -s " " | tr " "  "\t" | cut -f 2,3 > reads_n_alignments_distri.tsv
