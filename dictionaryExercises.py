#Dictionary Exercises 
#Exercise 1
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

# Printing Elizabeth's number
print phonebook_dict['Elizabeth']
# Add Kareem's number to phonebook dictionary
phonebook_dict.update({'Kareem': '938-489-1234'})
# Deleting Alice's number
del phonebook_dict['Alice']
# Changing Bob's number in the phonboook
phonebook_dict['Bob'] = '968-345-3245'
#printing out the numbers in the phonebook dictionary
print phonebook_dict
print

#Exercise 2
ramit = ({
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
})

# Write a python expression that gets the email address of Ramit
print ramit['email']
# Write a python expression that gets the first of Ramit's interests
print ramit['interests'][0]
# Wrtie a python expresssion that gets the email addresss of Jasmine
print ramit['friends'][0]['email']
# Wrtie a python expression that gets the second of Jan's two interests. 
print ramit['friends'][1]['interests'][1]