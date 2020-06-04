#!/usr/bin/env python3


import random


def main():
  lines = open('words.txt').read().splitlines()
  for name_counter in range(25):
    word_list = []
    for word_counter in range(2):
      word = random.choice(lines)
      word_list.append(word)
    for word in word_list:
      print(word, end=" ")
    print("\n")
  print("\n")


if __name__ == '__main__':
  main()
