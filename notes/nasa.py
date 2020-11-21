'''
Analyzing the NASA weblogs
http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html

    Task: Find the most frequent TLDs.

My habit for building regular expressions:
1. copy-paste an example
2. try to match itself to find special regex characters
3. replace interesting pieces with      (.*)
4. make it more specific if necessary
5. switch from re.findall to re.search if appropriate
'''

import re
import collections

tld_pattern = r'\.([a-z]+)$'

counts = collections.Counter()

with open('notes/nasa.log.sample') as f:
    for line in f:
        host = line.split()[0]
        mo = re.search(tld_pattern, host.lower())
        if mo is not None:
            tld = mo.group(1)
            counts[tld] += 1

# print sorted(counts.items(), key= reverse=True)
print counts.most_common(5)

# "We read Knuth, so you don't have to" -- Core Contributors


pattern = r'(.*) - - \[(.*)\] "(.*)" (.*) (.*)'
records = []
with open('notes/nasa.log.sample') as f:
    for line in f:
        mo = re.search(pattern, line)
        if mo is not None:
            records.append(mo.groups())


##############################################
### Example of using generators            ###
##############################################
            
from collections import Counter, namedtuple
from datetime import datetime

pattern = r'(.*) - - \[(.*)\] "(.*)" (.*) (.*)'
Log = namedtuple('Log', 'address timestamp request code size')

def parselines(fp):
    'expects `fp` as a file-like object that yields lines'
    for line in fp:
        mo = re.search(pattern, line)
        if mo is not None:
            address, timestamp, request, response_code, response_size = mo.groups()
            timestamp = datetime.strptime(timestamp[:-6], '%d/%b/%Y:%H:%M:%S')
            yield Log(address, timestamp, request, response_code, response_size)

if __name__ == '__main__':
    with open('notes/nasa.log.sample') as f:
        logs = parselines(f)
        hours = (log.timestamp.hour for log in logs)
        counts = Counter(hours)

    for hour, count in sorted(counts.items()):
        print str(hour).ljust(3), count // 2 * '#'
    
