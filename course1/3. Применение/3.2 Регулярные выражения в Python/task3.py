import re
import sys

pattern = r'z.{3}z'

for line in sys.stdin:
    if re.search(pattern, line):
        line = line.rstrip()
        print(line)
