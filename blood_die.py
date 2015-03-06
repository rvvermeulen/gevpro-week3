#!/usr/bin/python3
#blood_die.py
#Roos Vermeulen

import sys
import json
from collections import namedtuple

Taal = namedtuple("Taal", "naam, classificatie")
	
def checkblooddie(taal):
	blood = taal[2].split()
	die = taal[3].split()
	return [True for word in blood if word in die]

def main():
	source = open("blood-die.json", "r")
	bestand = json.load(source)
	resultatenlijst = []
	[resultatenlijst.append(Taal(taal[0], taal[1])) for taal in bestand if checkblooddie(taal)]
	[print(resultaat.naam, "|", resultaat.classificatie) for resultaat in resultatenlijst]

if __name__ == '__main__':
    main()
