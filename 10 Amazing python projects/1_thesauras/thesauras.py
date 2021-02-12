import json
from difflib import get_close_matches

def main():
    data = json.load(open('data.json'))

    def keyCall():
        return input('Enter the key you want to search in our dictionary: ')

    searchKey = keyCall()

    search = True

    def synonym(key):
        translation = ''
        try:
            translation = data[key]
        except:
            newKeyFunc(key)
            return
        if translation != '':
            printTranslation(translation)
        else: 
            return newKeyFunc(key)
            

    def newKeyFunc(key):
        tempList = []
        tempList = get_close_matches(key, data.keys(), cutoff=0.8)
        if tempList == []:
            print('The key doesn\'t exist in the dictionary, Please check your input.. \n')
            return
        newKey = tempList[0]
        if input(f"Press 'y' if you try to mean '{newKey}': ").lower() == 'y':
            synonym(newKey)
            return
        print('The key doesn\'t exist in the dictionary, Please check your input.. \n')

    while search:
        if searchKey != '':
            synonym(searchKey.lower())
            search = False
        else: 
            print('\nPlease enter a Value!\n')
            searchKey = keyCall()
    
    
def printTranslation(input):
        for i in range(0, len(input)):
            print(f'{i+1}. {input[i]}')

if __name__ == '__main__':
    main()