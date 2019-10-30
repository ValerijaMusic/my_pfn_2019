#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 0.25h

import sys

tC = [t for t in range(1,101)]
tF = [(tc*9.0)/5.0+32.0 for tc in tC ] 

print("# {}\t{}".format("celsius","fahrenheit"))

for i in range(len(tC)):
    print("{:.2f}\t{:.2f}".format(tC[i],tF[i]))

