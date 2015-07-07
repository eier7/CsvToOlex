#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#konverterer ruter fra .csv-fomat til Olex
#formatet i csv maa vaere slik:
#063.77066667°N,008.50241667°E,0.00
#063.77046667°N,008.50401666°E,0.00
#
# eivinde@harstad-elektronikk.no

import os
import re
import time
import sys

linecolor = ['Rod', 'Gul', 'Gronn', 'Lilla', 'Brun', 'Sort']

utfil = open("konvertertdata", "w")
utfil.write("Ferdig forenklet\n\n")
antallrute = 0
for rutefil in os.listdir("."):
    if rutefil.endswith(".csv"):
        utfil.write("Rute " + rutefil.split(".")[0] + "\n")
        utfil.write("Linjefarge " + linecolor[antallrute % 6] + "\n")
        f = open(rutefil, "r")
        for line in f:
            m = re.search("(\d*\.\d*)\xB0N,(\d*\.\d*)\xB0E", line)
            if m:
                lat = float(m.group(1)) * 60
                lon = float(m.group(2)) * 60
                timestamp = int(time.time())
                utfil.write(str(lat) + " " + str(lon) + " " + str(timestamp) + " Brunsirkel\n")
    utfil.write("\n")
    antallrute += 1

utfil.close()

####Carriage return windows fix
content = ''
outsize = 0
with open("konvertertdata", 'rb') as infile:
  content = infile.read()
with open("konvertertdata", 'wb') as output:
  for line in content.splitlines():
    outsize += len(line) + 1
    output.write(line + b'\n')


