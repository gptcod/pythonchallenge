# -*- coding: UTF-8 -*-
import requests

old_id = 12345
new_id = 0
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

for i in range(400):
    print ("this is {} times".format(i))
    url = base_url + str(old_id)

    r = requests.get(url)
    sentence = r.text
    number_start_pos = sentence.rfind(' ') + 1

    new_id = sentence[number_start_pos:]
    print old_id, new_id

    if new_id and new_id == old_id:
        break

    else:
        old_id = new_id

# result: peak
