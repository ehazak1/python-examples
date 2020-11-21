'''
Analyzing the NASA weblogs
http://ite.ee.lbl.gov/html/contrib/NASA-HTTP

    Task: find the most frequent TLDs (Top Level Domain)
'''

import re
import collections
tld_pattern = r'\.([a-z]+)$'

counts = collections.Counter()
with open('notes/nasa.log.sample') as f:
    for line in f.readlines():
        host = line.split()[0]
        mo = re.search(tld_pattern, host)
        if mo is not None:
            tld = mo.group(1)
            counts[tld] += 1

# print sorted(counts.items(), reverse=True)
print counts.most_common(5)

with open('notes/nasa.log.sample') as f:
    for line in f.readlines():
         print line
         break

