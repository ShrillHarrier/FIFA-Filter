import csv

#These functions provide better organization and clarity in the main
def goalieStats(line):
    return ["Position: " + line[21], "Diving: " + line[83], "Handling: " + line[84], "Kicking: " + line[85], "Postioning: " + line[86], "Reflex: " + line[87], "Speed: " + line[65], "Price: " + (line[11])[3:len(line[11])] + " Euros"]

def playerStats(line):
    return ["""Position: """ + line[21], """Pace: """ + line[65], "ShotPower: " + line[69], "Passing: " + line[57], "Dribbing: " + line[59], "Defending: " + line[81], "Physical: " + line[72], "Price: " + (line[11])[3:len(line[11])] + " Euros"]

#Main
footballers = {} 

#player = input()

with open("Fifa19.csv", errors='replace') as fileIn:
    fileIn.readline()
    
    reader = csv.reader(fileIn)

    for line in reader:
        if(line[21] == "GK"):
            footballers[line[2]] = goalieStats(line)
        else:
            footballers[line[2]] = playerStats(line)

for footballer in footballers:
    print(footballer + ":")
    print(footballers[footballer]) 


