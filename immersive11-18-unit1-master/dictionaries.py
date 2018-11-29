greg = [
    "Greg",
    "Male",
    "Tall",
    "Developer"
]

greg = {
    "name": "Greg",
    "genger": "Male",
    "height": "Tall",
    "job": "Developer"
}

print greg["name"]

zombie = {}
zombies = []
zombie['weapon'] = "fist"
zombie['health'] = 100
zombie['speed1'] = 10

print zombie

for key,value in zombie.items():
    print "zombie has a key of %s with a value of %s" % (key, value)

#remove a key

del zombie['weapon']
print zombie
is_nighttime = True
if(is_nighttime):
    zombie['health'] += 50

#put list and dictionaries together

zombies.append({
    'name': 'hank',
    'weapon': 'baseball bat',
    'speed': 10
})
zombies.append({
    'name': 'Willie',
    'weapon': 'axe',
    'speed': 3,
    'victims':[
        'squirrel',
        'rabbit',
        'racoon'
    ]
})

print zombies[1]['victims'][1]