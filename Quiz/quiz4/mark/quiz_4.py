# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to2013.
# Prompts the user for a female first name, and finds out the years when this name was most popular
# in terms of ranking. Displays the ranking, and the years in decreasing order of frequency.


import sys
import os

targeted_first_name = input('Enter a female first name: ')
rank = float('inf')

best_years = []
#=========================================================
# Replace this comment with your code
year = 1880
unit_list = []
while year < 2014:
    with open('names/yob'+ str(year) + '.txt') as file:
        count = 0
        sum = 0
        target_number = 0
        for line in file:
            name, sex, str_number = line.split(',')
            number = int(str_number)
            if sex == 'F':
                sum += number
                count += 1
                if targeted_first_name == name:
                    target_number = number
                    current_rank = count
            else:
                ratio = target_number/sum
                break
        if ratio == 0:
            year += 1
            continue
        if current_rank < rank:
            rank = current_rank
            unit_list = []
            unit = [ratio, year]
            unit_list.append(unit)
        elif current_rank == rank:
            unit = [ratio, year]
            unit_list.append(unit)
        year += 1
if len(unit_list) == 1:
    best_years = [unit_list[0][1]]
elif len(unit_list) == 0:
    best_years = []
else:
    unit_list.sort()
    unit_list.reverse()
    best_years = [unit_list[i][1] for i in range(len(unit_list))]
#print(unit_list)
#====================================================
if not best_years:
    print('{} is not a female first name in my records.'.format(targeted_first_name))
else:
    print('By decreasing order of frequency, {} was most popular in the years: '.format(targeted_first_name), end = '')
    for year in best_years:
        print(year, end = ' ')
    print('\nIts rank was {} then.'.format(rank))

