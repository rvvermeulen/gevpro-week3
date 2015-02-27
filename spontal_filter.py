#!/usr/bin/python3
#spontal_filter.py
#Roos Vermeulen

import sys
import xml.etree.ElementTree as ET    

def filter(tree, uitvoerbestand):
	root = tree.getroot()
	for point in root.findall("POINT"):
		bottom = float(point.find("BOTTOM_HZ").text)
		top = float(point.find("TOP_HZ").text)
		start = float(point.find("F0_START").text)
		end = float(point.find("F0_END").text)
		if (start < bottom) or (end < bottom) or (start > top) or (end > top):
			root.remove(point)
	tree.write(uitvoerbestand)
	

def main(argv):
	if len(argv) == 3:
		xmltree = ET.parse(argv[1])
		antwoord = filter(xmltree, argv[2])
		
	else:
		print("Usage: spontal_filter.py spontal.xml <uitvoerbestand>.xml, voer de naam van het uitvoerbestand in", file=sys.stderr)
		exit(-1)

if __name__ == '__main__':
    main(sys.argv)
