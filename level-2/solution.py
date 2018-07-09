# -*- coding: UTF-8 -*-
import string

with open(r'character.txt', 'r') as f:
    content = f.read()
    chars = filter(lambda x: x in string.letters, content)
    print chars

# result: equality
