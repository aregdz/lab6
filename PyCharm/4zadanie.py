#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
if __name__ == '__main__':
   x = input("Введите первое слово: ")
   y = input("Введите второе слово: ")
   for i in x:
      if i in y:
         print("да")
      else:
         print("нет")