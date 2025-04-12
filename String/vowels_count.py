def vowels_count(s):
    vowels =0
    consonants=0
    vowel_set={'a','e','i','o','u'}
    
    for ch in s:
        if ch.isalpha():
            if ch in vowel_set:
                vowels+=1
            else:
                consonants+=1
    if vowels>consonants:
        print("Yes")
    elif vowels<consonants:
        print("No")
    else:
        print("same")
        
s=input()
print(vowels_count(s))