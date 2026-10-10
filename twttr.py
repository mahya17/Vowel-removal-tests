text = input("Enter text: ")
vowels = "AEIOUaeiou"
result = ""
for c in text:
    if c not in vowels:
        result += c
print(result)
