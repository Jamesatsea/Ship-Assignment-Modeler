import random
        
def populateITOs():
    for i in range (nShips-1):
        rand = random.randint(1,2)
        if rand == 1:
            contLength = 4
        else:
            contLength = 6
        rand = random.randint(-180, 0)
        newData = {"contLen" : contLength, "startday" : rand}
        permITOArr.append(newData)
    return permITOArr
           
def populateShipSchedule():
    simEnd=len(shipSchedule[0])-182
    positionCounter = 0
    for i in range (nShips):
        startdate = 179+permITOArr[i]["startday"]
        positionCounter = startdate
        contLengthDays = permITOArr[i]["contLen"] * 30
        while positionCounter <= simEnd:
            for j in range (contLengthDays):
                shipSchedule [i][startdate+j] = 1
            positionCounter = positionCounter + contLengthDays + vacationDays
            startdate = startdate + contLengthDays + vacationDays

def findgaps():

    studyDays = nDays-365
    for i in range(studyDays):
        slotsNeeded = 0
        for j in range (nShips):
            if shipSchedule [j][i+180] == 0:
                slotsNeeded = slotsNeeded + 1
        gapArr.append (slotsNeeded)
    

###### Main ######

nCycles = int(input("Number of cycles to run simulation: "))
nShips = int(input("Number of Ships: "))
nYears = int(input("Number of years over which to run the simulation: "))
nDays=(nYears+1)*365
vacationDays = int(input("Number of vacation days between contracts: "))
mainGapArr = [0 for i in range(nCycles)]

for CycleCount in range (nCycles):
    gapArr = [0 for i in range(1)]
    rand = random.randint(1,2)
    if rand == 1:
        contLength = 4
    else:
        contLength = 6
    rand = random.randint(-180, 0)
    permITOArr = [{"contLen" : contLength, "startday" : rand}]
    populateITOs()
    shipSchedule = [[0 for i in range(nDays)] for j in range(nShips)]
    populateShipSchedule()
    findgaps()
    #gapArr = [x for x in gapArr[2:]]
    for i in range (nShips):
        slotsNeeded = gapArr.count(i)
        #print ("number needing " + str(i) + " is " + str(slotsNeeded))
        mainGapArr.append(gapArr.count(i))
        #print ("probability of needing " + str(i) + " is " + str(slotsNeeded / (nDays - 365)*100))

mainGapArr2 = [x for x in mainGapArr[nCycles:]]

contFour = 0
contSix = 0
for i in range (nShips):
    contLength = permITOArr[i]["contLen"]
    if contLength == 4:
        contFour = contFour +1
    else:
        contSix = contSix +1

print("Number of ITOs with 4 months contracts: " + str(contFour))
print("Number of ITOs with 6 months contracts: " + str(contSix))


for index in range (nShips):
    totalNeededper = 0
    for CycleCount in range (nCycles):
        totalNeededper = totalNeededper + mainGapArr2[index + CycleCount*nShips]
        #print (mainGapArr2[index + CycleCount*nShips])
    print ("The percentage of the time needing " +str(index) + " Floating ITOs is: " + str (round(totalNeededper/nCycles/(nDays-365)*100)) + "%")

    



