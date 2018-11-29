phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}



print phonebook_dict['Alice']

phonebook_dict.update({'kareem': '938-489-1234'})
print phonebook_dict

phonebook_dict.pop('Alice')
print phonebook_dict

phonebook_dict.update({'Bob': '968-345-2345'})
print phonebook_dict


ramit = {
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
}

print ramit['email']
print ramit['interests'][0]
print ramit['friends'][0]['email']
print ramit['friends'][1]['interests'][1]

from collections import Counter
import string
text = raw_input('Enter a word:')
stripped_text = ''.join(ch for ch in text if ch not in set(string.punctuation))
histogram = Counter(stripped_text.split(' '))
max_word_len = max(len(x) for x in histogram.keys())
for i in histogram.items():
    print i[0] + (max_word_len - len(i[0])) * ' ', i[1], i[1] * '*'
total = str(sum(c[1] for c in histogram.items()))
print 'TOTAL' + (max_word_len - len('TOTAL')) * ' ', total, 'words'



