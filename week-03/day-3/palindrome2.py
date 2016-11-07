# Create a function that searches for all the palindromes in a string that are at least than 3 characters, and returns a list with the found palindromes. Example:

# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['og go', ' dad ', 'd d', 'dood', 'eve']

class PalindromeSearchEngine():
    list=[]

    def __init__(self, string):
        self.string = string

    def assamble_dat_shit(self):

        for i in range(len(self.string)-4):
            if self.string[i:i-4] == self.string[i:i+4][::-1]:
                print(self.string[i:i+3], 'is a palindrome')
            else:
                print(self.string[i:i+4], 'is not a palindrome')

pali = PalindromeSearchEngine('dog goat dad duck doodle never')
pali.assamble_dat_shit()
