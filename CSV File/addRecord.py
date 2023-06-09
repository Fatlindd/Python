import csv 

file = open('Books.csv', 'a')
title = input('Enter a title: ')
author = input('Enter author: ')
year = input('Enter the year it was released: ')
newrecord = title + ',' + author + ',' + year + '\n'
file.write(str(newrecord))
file.close()


