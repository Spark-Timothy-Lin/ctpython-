# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:21:23 2021

@author: user

1.由系統亂數產生1~49之間6個不重複的整數
2.請遞增排序印出

count ==0

"""

import random

math = list()


while True:
    if len(math)<6:
        ans = random.randint(1,49)
        while math.count(ans) == 0 :
            math.append(ans)
            
    else:
        break
print("產生的順序:",math)
math2=math
math2.sort()
print("遞增的順序:",math2)
