# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:46:19 2021

@author: user
1.由系統產生7個整數數字(亂數1~100)ps重複沒關係
2.印出來  遞增排序
3.由使用者輸入7個數字之一  去找尋串列中的值
4.用2分法顯示找尋"過程"

"""

import random

math = list()
a=1
b=1
for i in range(27):
    math.append(random.randint(1,100))
    math.sort()
    

print(math)



che = int(input("請輸入上述數字其中一個數字:"))
while True:
    if math.count(che) == 0 :

        print("上述串列裡找不到您輸入的數字!!!!")
        print(math)
        che = int(input("請重新輸入上述數字其中一個數字:"))
    else:
        break
    
while True:
        
    if len(math)//2 == 0:
        leng= (len(math)//2)-1
        
        if leng == -1:
            leng = 0
            break


    else:
        leng= len(math)//2

        
        if che == math[leng]:
            del math[0:]
            math.append(che)
            a += 1
            b=0
            break
        
        elif che > math[leng]:
            del math[:leng+1]
            a += 1
            
        else :
            del math[leng:]
            a += 1
            
        if  len(math) > 1 :
            print("第",a-1,"次的數列:",math)
            b=0
        
if b == 0 :
    
    print("第",a-1,"次的數列:",math) 
    
    
print("經過",a-1,"次取得數字")
