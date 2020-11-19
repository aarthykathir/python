sentence=input("Enter a string:")
def check_palindrome():
    rev_sentence=sentence[::-1]
    if(sentence==rev_sentence):
        status=True
    else:
        status=False
    return status

palindrome=check_palindrome()
if(palindrome):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
    
def palindrome(sentence):
    reverse=""
    for i in sentence:
        reverse=i+reverse
    print("Reverse String:",reverse)

palindrome(sentence)
