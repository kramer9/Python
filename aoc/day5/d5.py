https://adventofcode.com/2021/day/5


import re
m = re.search(r'(?<=-)\w+', 'spam-egg')
m.group(0)
print (m.group(0))