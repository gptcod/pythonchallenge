# -*- coding: UTF-8 -*-
import string

in_tab = string.ascii_lowercase
out_tab = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
tran_tab = string.maketrans(in_tab, out_tab)
result = 'map'.translate(tran_tab)
print result

# result: ocr
