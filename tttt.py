x = open("tttt.in")
row1 = x.readline()[0:3]
row2 = x.readline()[0:3]
row3 = x.readline()[0:3]
rows = [row1,row2,row3]
combins = []
indiv = 0
team = 0
x.close()

#indivudal
#rows
for i in rows:
    if i[0] == i[1] and i[1] == i[2]:
        indiv += 1
    else:
        combins.append(i)

#columns
index = 0
for i in range(3):
    if row1[index] == row2[index] and row3[index] == row2[index]:
        indiv += 1
    else:
        combins.append(row1[index]+row2[index]+row3[index])
    index += 1

#horizontal
if row1[0] == row2[1] and row2[1] == row3[2]:
    indiv += 1
else:
    combins.append(row1[0]+row2[1]+row3[2])

if row1[2] == row2[1] and row2[1] == row3[0]:
    indiv += 1
else:
    combins.append(row1[2]+row2[1]+row3[0])
#team
teams = list()
for i in combins:
    l = []
    count = False
    for x in i:
        if x in l:
            count = True
        l.append(x)
    if count == True:
        teams.append(set(i))
new = []
for i in teams:
    if i in new:
        continue
    else:
        new.append(i)
team = len(new)
    
y = open("tttt.out","w")
y.write(str(indiv) + "\n")
#print(indiv)
y.write(str(team))
#print(team)
y.close()
