python = input("Enter string:")
print("The length of your input is:")
print(len(python))
vowels = 0

consonent = 0

for i in python:

    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):

        vowels=vowels+1

    else:
        consonent=consonent+1

print("Number of vowels are:")
print(vowels)

print("Number of consonent are:")
print(consonent)
