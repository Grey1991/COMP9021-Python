# Uses National Data on the relative frequency of given names
# in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt
# with xxxx (the year of birth)
# ranging from 1880 to 2013.
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.


import os
from sys import exit


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

tallies = {'F': {}, 'M': {}}
records = {'F': {}, 'M': {}}
for filename in os.listdir(directory):
    pass
    # Replace pass above with code to read the contents of the processed file in case it is
    # a .txt file and compute:
    # - in tallies[gender][year], the total count of names of that gender on that year
    # - in records[gender][year], the count of the input name in case it is found.

frequencies = dict.fromkeys('M', 'F')
for gender in {'F', 'M'}:
    pass
    # Replace pass above to compute frequencies

# Insert code to make final computations and output the results.
