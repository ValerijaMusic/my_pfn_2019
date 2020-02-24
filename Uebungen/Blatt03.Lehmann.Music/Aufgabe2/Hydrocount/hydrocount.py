#!/usr/bin/env python3
# Lehmann.Music

import sys

hydrophob = hydrophil = 0

for amino in sys.argv:
    if amino == "A","J","F","I","L","M","P","V","W": 
        hydrophob += 1 
    elif amino == "C", "D","E","G","H","K","N", "Q","R","S","T","Y":
        hydrophil += 1 
