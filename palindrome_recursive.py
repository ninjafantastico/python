def isPalindrome(string):
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and isPalindrome(string[1:-1])

def isPalindrome_Iterative(string):
    for i in range(len(string)/2):
        if string[0] != string[-1]:
            return False
    return True

word = "helloolleh"
print(isPalindrome(word))
