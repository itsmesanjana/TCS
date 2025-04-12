# Q7. The Caesar cipher is a type of substitution cipher in which each alphabet in the plaintext or
# messages is shifted by a number of places down the alphabet.
# For example, with a shift of 1, P would be replaced by Q, Q would become R, and so on. To pass an
# encrypted message from one person to another, it is first necessary that both parties have the ‘Key’
# for the cipher, so that the sender may encrypt and the receiver may decrypt it. Key is the number of
# OFFSET to shift the cipher alphabet. Key can have basic shifts from 1 to 25 positions as there are 26
# total alphabets.
# As we are designing custom Caesar Cipher, in addition to alphabets, we are considering numeric
# digits from 0 to 9. Digits can also be shifted by key places.
# For Example, if a given plain text contains any digit with values 5 and key =2, then 5 will be replaced
# by 7, “- ”(minus sign) will remain as it is.
# Key value less than 0 should result into “INVALID INPUT”
# Example 1: Enter your Plaintext: All the best
# Enter the Key: 1
# The encrypted Text is: Bmm uif Cftu 

def caesar_cipher(PT,K):
    if K<0:
        return "Invalid Key"
    encrypted_text=[]
    
    for char in PT:
        if "A"<=char<="Z":
            encrypted_text.append(chr((ord(char)- ord("A")+K)%26+ord("A")))
        elif "a"<=char<="z":
            encrypted_text.append(chr((ord(char)-ord("a")+K)%26+ord("a")))
        elif "0"<=char<="9":
            encrypted_text.append(chr((ord(char)-ord("0")+K)%10+ord("0")))
        else:
            encrypted_text.append(char)
    return "".join(encrypted_text)


plaintext = input("Enter your PT: ")
key = int(input("Enter the key: "))

encrypted_text = caesar_cipher(plaintext, key)
print("The encrypted Text is:", encrypted_text)
