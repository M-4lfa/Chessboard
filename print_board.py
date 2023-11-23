# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:42:33 2023

@author: Moisés
"""
from dataclasses import dataclass



 
#  i is line 
# j is column
def board_print(size: int):
    hor_line = '------'
    ver_line = '     |'
    first_ver_line = '|'
    a = []
    b = []
    for i in range (size):
        b.append(first_ver_line)
        for j in range(size):
            a.append(hor_line)
            b.append(ver_line)   
        print("".join(a))
        print("".join(b))
        print("".join(b))        
        print("".join(b))
        if i == size-1:
            print("".join(a))
        a = []
        b = []

def main():
    board_print(8)
    
if __name__ =="__main__":
        main()