import csv 
import glob

#This function checks if a club is already a key
def putClub(club, clubs):
    if((club in clubs) == False):
        clubs[club] = {}

    return clubs 

#This fucntion is useful for getting average club ratings (player/goalie ratings)
def getAverage(data):
    total = 0

    for x in data:
        total += int(x)

    return total/len(data)

#This club appends player ratings to each year of a club
def updateClub(file, clubs, line):
    if "19" in file:
        if line[9] in clubs:
            if file in clubs[line[9]]: 
                clubs[line[9]][file].append(line[7])
            else:
                clubs[line[9]][file] = list([line[7]])
    elif "18" in file:
        if line[4] in clubs:
            if file in clubs[line[4]]: 
                clubs[line[4]][file].append(line[9])
            else:
                clubs[line[4]][file] = list([line[9]])
    elif "17" in file:
        if line[8] in clubs:
            if file in clubs[line[8]]: 
                clubs[line[8]][file].append(line[6])
            else:
                clubs[line[8]][file] = list([line[6]])

    return clubs

#Predicts Fifa20 rating based on Fifa19 and Fifa18
def getPrediction(club):
    rate = 'n/a'
    
    if 'Fifa19' in club:
        rate = club['Fifa19']

    if 'Fifa19' in club and 'Fifa18' in club:
        rate -= club['Fifa18']
        rate += club['Fifa19']

    return rate
                  
#Main
filepointers = []

for name in glob.glob("Fifa*.csv"):
    filepointers.append(name)

clubs = {}

#Fill club list
with open(filepointers[2], encoding='UTF-8') as fileIn:
    fileIn.readline()
    reader = csv.reader(fileIn)

    for line in reader:
        #print(line[9])
        clubs = putClub(line[9], clubs)
        #print(clubs)

#Search for ratings
for file in filepointers:
    with open(file, encoding='UTF-8') as fileIn:
        fileIn.readline()
        reader = csv.reader(fileIn)

        file = file[0:6]
        for line in reader:
            clubs = updateClub(file, clubs, line)

#Get average rating each year
for club in clubs:
    for year in clubs[club]:
        clubs[club][year] = getAverage(clubs[club][year])

#Get predicted rating for 2020
for club in clubs:
    clubs[club]['Fifa20'] = getPrediction(clubs[club])

print(clubs)

        
        
        
        


    
