import json

data = json.load(open('data.json'))

def keyCall():
    return input('Enter the value you want to search in our dictionary: ')

searchKey = keyCall()

search = True

def synonym(key):
    key = key.lower()
    translation = data[key]
    if translation != '':
        print(translation)
    else: print('The Key doesn\'t exist in the dictionary, Please check your input.. \\\n')

while search:
    if searchKey != '':
        synonym(searchKey)
        search = False
    else: 
        print('\nPlease enter a Value!\n')
        searchKey = keyCall()