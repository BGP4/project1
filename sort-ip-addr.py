#!/usr/bin/env python

from netaddr import *
import csv

def read_csv(fname):
# Read in the csv file
# csv format: type,prefix

  # Prefix length
  p_len = int(24)

  with open(fname, mode='r') as f:
    cr = csv.reader(f)

    # initialise a new dictionary to store type and prefixes
    prefix_list = []

    # read in each row and deaggregate if needed
    for row in cr:
      prefix_list.append(IPNetwork(row[1]))

  # sort prefixes
  prefix_list.sort()

  # print prefixes
  for key in prefix_list:
    print key

def main():

  # file name containing BB prefix list
  csv_filename = 'BNG-prefix-list.csv'

  # read in BB prefix list file
  # store in a list, sort and print them
  read_csv(csv_filename)

if __name__ == '__main__':
  main()

