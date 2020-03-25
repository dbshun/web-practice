# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:50:24 2020

@author: 12052
"""
def Fibonacci_of(num):
    if num ==1:
        return 1
    if num == 2:
        return 1
    return Fibonacci_of(num-1)+Fibonacci_of(num-2)
def main():
    for i in range(1,201):
        result=Fibonacci_of(i)
        print(result)
if __name__ == '__main__':
    main()
