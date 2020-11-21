'''
JSON is easy.
'''

import json

with open('notes/books.json') as f:
    data = json.load(f)


stuff = {'a': [10, 20, 30],
        'b': {'greetings': 'hello',
              'count': 42},
        }

print json.dumps(stuff, indent=2)
