def count_vowels(s):
    total = 0
    for char in s:
        if char in 'aeiou':
            total += 1
    return total

print("Number of vowels:"),
print(count_vowels(s))
