for i in range(1,10):
    print i

for i in range(1,10,2):
    print i

sudent1 = "zac"
student2 = "brandon"
student3 = "jr"
student4 = "khanh"


students = ["zac","brandon","jr","khanh"]
print students[0]

numOfStudents = len(students)
for i in range(0,numOfStudents):
    print students[i]

atlanta_teams = []
atlanta_teams.append("Falcons")
atlanta_teams.append("united")
atlanta_teams.append("braves")
atlanta_teams.pop()
print atlanta_teams
atlanta_teams.append("hawks")
print atlanta_teams
atlanta_teams.sort()
print atlanta_teams

reindeer = "dasher, dancer, prancer, vixon"

reindeerAsAList= reindeer.split(', ')
print reindeerAsAList

print reindeerAsAList[0:2]