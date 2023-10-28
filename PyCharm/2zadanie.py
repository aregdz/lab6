#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
if __name__ == '__main__':
    word1 = input("Введите 1 слово: ")
    word2 = input("Введите 2 слово: ")
    if word1 == word2:
        print(f"Слова полностью совпадают, их длина: {len(word1)} букв")
    else:
        if len(word1) < len(word2):
            min_len = len(word1)
        else:
            min_len = len(word2)
        count = 0
        for i in range(min_len):
            if word1[i] == word2[i]:
                count += 1
            else:
                break
        if count == 0:
            print("Слова не имеют совпадающих начальных букв.")
        else:
            print(f"Количество совпадающих начальных букв: {count}")