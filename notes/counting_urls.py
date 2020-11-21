import collections
import glob
import gzip
import re
import pprint

counter = collections.Counter()
for filename in glob.glob('/users/mike/data/nasa/split/*.gz'):
    for line in gzip.open(filename):
        mo = re.search(r'GET (.*) HTTP/1', line)
        if mo is not None:
            url = mo.group(1)
            counter[url] += 1

result = counter.most_common(20)
pprint.pprint(result)
