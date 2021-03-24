# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:12:27 2021

@author: user
"""

"""
1.min =1 ,max = 100
2.猜的數字要縮小範圍
  終極密碼的概念
3.如果猜錯5次就離開
  顯示次數猜錯5次

"""

import random

m = 1
M =100
ans = random.randint(m,M)
play = 0
r = 5


while ans != play:
    
    print ()
    print ("="*18)   
    play = int(input("輸入%d~%d之間猜數"%(m,M)))
        
    if ( r > 0 ):

    
        if (play < m or play > M):
            print ("數字超出範圍，重新輸入")
            continue

        if (play > ans) :
            print ("猜小一點")
            r -= 1
            print ("你剩%d次猜數的機會"%(r))   
            M = play

        if (play < ans) :
            print ("猜大一點")
            r -= 1
            print ("你剩%d次猜數的機會"%(r))   
            m = play

    if (r == 0):
        print("很可惜  沒機會了 你猜不到~~")
        print("答案是:",ans)
        break

if (ans == play):
    
    print("猜對了，猜了%d次"%((5-r)+1))


