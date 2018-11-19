# DICTIONARIES
# Dictionaries are just like lists 
# Except... instead of numbered indicies, they
# have English indicies

greg = [
    "Greg",
    "Male",
    "Tall",
    "Developer"
]

# If i wanted to know Greg's job, I have to do greg[3] 
# No one is going to expect that

# Key:value pair
greg = {
    "name": "Greg",
    "gender": "Male",
    "height": "Tall",
    "job" : "Developer"
}

# print greg["name"]
# print greg["job"]

# Make a new dictonary
zombie = {} #dictionary
zombies = [] #list
# zombies.append()
zombie['weapon'] = "fist"
zombie['health'] = 100
zombie['speed1'] = 10

print zombie
print zombie['weapon']

for key,value in zombie.items():
    print "Zombie has a key of %s with a value of %s" % (key,value)

# In our game, poor zombie loses his weapon (arm falls off)
# we need to remove his "weapon" key
del zombie['weapon']
print zombie
is_nighttime = True
if(is_nighttime):
    zombie['health'] += 50

# Put lists and dictionaries together!!!
zombies = []
zombies.append({
    'name': 'Hank',
    'weapon': 'baseball bat',
    'speed': 10 
})
zombies.append({
    'name': 'willie',
    'weapon': 'axe',
    'speed': 3
    'victims': [
        'squirrel',
        'rabbit',
        'racoon'
    ]
})
#This will get the first zombie in zombies weapon
print zombies[0]['weapon']
#this will get the second victim, in the second zombie list of victims
print zombies[1]['victims'][1]

# If we wanted to know zombie1's weapon: