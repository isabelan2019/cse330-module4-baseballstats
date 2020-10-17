import sys, os
import re

#one command-line argument: path to an input file
#no path given, print usage message
if len(sys.argv)<2:
    sys.exit(f"Usage:{sys.argv[0]} filepath")

filepath = sys.argv[1]

if not os.path.exists(filepath):
    sys.exit(f"Error: Filepath '{sys.argv[1]}' not found")

#regular expression match
regex = re.compile(r"(?P<name>[A-z]* [A-z]*) batted (?P<atBats>\d*) times with (?P<hits>\d*) hits")


#create dictionary
playersHits={}
playersAtBats={}
with open(filepath) as f:
    for line in f:
        stat = line.strip()
        result=regex.match(stat)
        if result:
            playersHits[result.group('name')]= 0
            playersAtBats[result.group('name')]= 0
            

with open(filepath) as f:
    for line in f:
        stat = line.strip()
        result=regex.match(stat)
        if result:
            oldValueHits = playersHits[result.group('name')]
            newValueHits = int(result.group('hits'))
            playersHits[result.group('name')] = oldValueHits + newValueHits

            oldValueAtBats = playersAtBats[result.group('name')]
            newValueAtBats = int(result.group('atBats'))
            playersAtBats[result.group('name')] = oldValueAtBats + newValueAtBats

#computes Cardinals' players' batting averages in a particular season
#batting avg = total hits / total at-bats
playersBattingAvg={}
for key in playersHits.keys():
   playersBattingAvg[key]= None

for key in playersBattingAvg.keys():
    playersBattingAvg[key] = playersHits[key]/playersAtBats[key]
           
unsortedBatAvg=playersBattingAvg.items()  

sortedBatAvg=sorted(unsortedBatAvg,key=lambda x:x[1], reverse=True)

for each in sortedBatAvg:
    print(each[0], ":", round(each[1],3))


#rounded to three decimal places
#sorted by batting avg (high to low before rounding)

