def check_if_palindrome(word:str)-> bool:
    cleaned = []
    for character in word: 
        if character.isalpha():
            cleaned.append(character.lower())
            
    # code to check if pallindrome or not 
    for x in range(len(cleaned) // 2):
        if cleaned[x] != cleaned[-(x+1)]:
            return False
        return True
    
input_word = input("Enter the word: ")



