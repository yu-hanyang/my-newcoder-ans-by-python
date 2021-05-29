import collections
import sys
string = ''
for line in sys.stdin:
    string += line.strip().replace(' ', '')
print(collections.Counter(string).most_common()[0][0])