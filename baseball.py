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
regex = re.compile(r"(?P<name>[\w']* [\w']*) batted (?P<atBats>\d*) times with (?P<hits>\d*) hits")


#create dictionary
playersHits={}
playersAtBats={}
with open(filepath) as f:
    for line in f:
        stat = line.strip()
        result=regex.match(stat)
        if result:
            #initalize keys in each dict 
            playersHits[result.group('name')]= 0
            playersAtBats[result.group('name')]= 0
            

with open(filepath) as f:
    for line in f:
        stat = line.strip()
        result=regex.match(stat)
        if result:
            #add hits to old value using name as key in each dict
            oldValueHits = playersHits[result.group('name')]
            newValueHits = int(result.group('hits'))
            playersHits[result.group('name')] = oldValueHits + newValueHits

            oldValueAtBats = playersAtBats[result.group('name')]
            newValueAtBats = int(result.group('atBats'))
            playersAtBats[result.group('name')] = oldValueAtBats + newValueAtBats


#create new dict to hold total batting averages for each player
playersBattingAvg={}
#iterate through one of the old dict to add in all the keys to new dict
for key in playersHits.keys():
   playersBattingAvg[key]= None

#computes Cardinals' players' batting averages in a particular season
#batting avg = total hits / total at-bats
for key in playersBattingAvg.keys():
    playersBattingAvg[key] = playersHits[key]/playersAtBats[key]
           
unsortedBatAvg=playersBattingAvg.items()  

#sorted by batting avg (high to low before rounding)
sortedBatAvg=sorted(unsortedBatAvg,key=lambda x:x[1], reverse=True)

#rounded to three decimal places
for each in sortedBatAvg:
    print(each[0], ":", '{:.3f}'.format(round(each[1],3)))

