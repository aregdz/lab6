#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
if __name__ == '__main__':
   s = input("Введите предложение: ")
   x = s.lower()
   while "c" in x:
       l = x.find("c")
       x = x[:l] + x[l+1:]
   while "с" in x:
       l = x.find("с")
       x = x[:l] + x[l+1:]
   print(x)
