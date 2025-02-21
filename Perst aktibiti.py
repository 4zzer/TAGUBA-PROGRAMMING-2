# Write a function print_dict_length(d) that prints the number of key-value pairs in dictionary d.
# If the dictionary is empty, print "Dictionary is empty."

def print_dict_length(d): # function to print le number of key-value pairs in dictionary d
    if len(d) == 0:
        print("Dictionary is empty.")
    else:
        print('Length of the dictionary: ' + str(len(d)))

d = {           # le dictionary         
    'ign': 'AshDash',
    'hp': 100,
    'shield': 50,
    'weapon': 'vandal',
}

print_dict_length(d)

d.clear # delete le entire items in le dictionary

print(d)