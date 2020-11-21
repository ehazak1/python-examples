import collections
import glob
import gzip
import re
import pprint


# Couner object instastiation - we know it's an object because of the capital
# 'C' in Counter - which points to a class
counter = collections.Counter()
# In the line below the 2nd glob is a function (and not a class), since it
# starts with a lowercase 'g'
for filename in glob.glob('Data/logs/*.gz'):
    # Uncompress the file using gzip, and go over each line
    for line in gzip.open(filname):
        # using the re (Regular Expression) module to search the pattern below
        # mo - matched object
        mo = re.search(r'GET (.*) HTTP/1', line)
        # if mo is not empty ...
        if mo is not None:
            # put the found url into the url variable
            url = mo.group(1)
            # increment the 'url' counter
            counter[url] += 1


# take the 20 most common results
result = counter.most_common(20)
# pretty print ...
pprint.pprint(result)
