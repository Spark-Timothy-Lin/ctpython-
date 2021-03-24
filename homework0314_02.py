# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:07:54 2021

@author: user
"""

"""
1.請使用者輸入一個範圍的整數
2.求4的倍數有哪些
3.求那些是質數  (只可被1跟自己整除)

    

"""

player =int(input ("請輸入一個整數:"))

print (list(range (1,player+1)))

for i in range (1,player+1):

    if i%4 == 0:
        print (i,"是4的倍數，也不是質數")

    else:
        if i == 1:
            print (i,"不是4的倍數,也不是質數")
        elif i != 2 and i%2 ==0 :
            print (i,"不是4的倍數,也不是質數")
        elif i != 3 and i%3 ==0 :
            print (i,"不是4的倍數,也不是質數")
        elif i != 5 and i%5 ==0 :
            print (i,"不是4的倍數,也不是質數")
        elif i != 7 and i%7 ==0 :
            print (i,"不是4的倍數,也不是質數")
        else :
            print (i,"不是4的倍數,是質數")
