from pprint import pprint

list_of_dicts = [({"bin": bin(num), "dec": num,
                   "hex": hex(num), "oct": oct(num)})
                 for num in range(16)]
pprint(list_of_dicts)


