# -*- coding: UTF-8 -*-
import re

with open (r'character.txt', 'r') as f:
    data = f.read()
    pattern =  re.compile(r'(?<![A-Z])[A-Z]{3}([a-z]{1})[A-Z]{3}(?![A-Z])')
    result = re.findall(pattern, data)
    result = "".join(result)
    print result

# result: linkedlist
