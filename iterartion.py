'''
How to loop like a Pythonista
'''

names = ['Luke', 'Leia', 'Han', 'Chewie']

# The bad way...
for i in range(len(names)):
    print names[i]

# The Pythonic Way (tm)
for name in names:
    print name

# Whenever you are looping
# and using index (``obj[index]``),
# there's probably a better way.

#####################################

# The bad way...
for i in range(len(names)):
    print i, names[i]

# The Pythonic Way:
for i, name in enumerate(names, 1):
    print i, name

#####################################    

# The bad way ...
for i in range(len(names)-1, -1, -1):
    print names[i]

# The Pythonic way ...
for name in reversed(names):
    print name

#####################################

for name in sorted(names):
    print name

#####################################

roles = ['hero', 'princess', 'pilot', 'copilot']

# The bad way ...
for i in range(len(names)):
    print names[i], roles[i]

# The Pythonic way ...
for name, role in zip(names, roles):
    print name, role

#####################################
print

for name in names:
    print len(name)

print
lengths = []
for name in names:
    lengths.append(len(name))
print lengths

print

lengths = map(len, names)
print lengths
    
