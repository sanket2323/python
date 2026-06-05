def canConstruct( ransomNote: str, magazine: str) -> bool:
    ransomNote_dict = {}
    magazine_dict = {}

    for char in ransomNote:
        ransomNote_dict = ransomNote_dict.get(char, 0) + 1

    for char in magazine:
        magazine_dict = magazine_dict.get(char, 0) + 1

    for char in ransomNote:

        if  ransomNote_dict[char] > magazine_dict.get(char,0) :
            return False

    return True


print(canConstruct('a','b'))