#!/usr/bin/env python3

import argparse
import os
import re


def read_filename(single_filename):
  words = []
  (filename, ext) = os.path.splitext(single_filename)
  words = filename.split(' ')
  return words


def scrub_list(words):
  no_empty_strings = []
  for item in words:
    item = re.sub('[^A-Za-z0-9]+', '', item)
    if item != '':
      no_empty_strings.append(item)
  words = no_empty_strings
  return words


def write_words_to_file(words, destination_file):
  for word in words:
    destination_file.write(word + "\n")
  return


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('directory', help='System path to directory containing files.')
  args = parser.parse_args()
  directory = args.directory
  destination_file = open('/Users/michael/Desktop/words.txt','w+')
  for (dirpath, dirnames, filenames) in os.walk(directory):
    for single_filename in filenames:
      words = read_filename(single_filename)
      words = scrub_list(words)
      write_words_to_file(words, destination_file)
  destination_file.close()
  exit()


if __name__ == '__main__':
  main()
