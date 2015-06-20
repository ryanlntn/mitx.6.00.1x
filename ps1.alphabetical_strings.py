def longest_substring(s):
    longest = ''

    for i in range(len(s)):
        current = s[i]
        j = 1
        while i+j < len(s) and s[i+j] >= current[-1]:
            current += s[i+j]
            j += 1

        if len(current) > len(longest):
            longest = current

    return longest

print("Longest substring in alphabetical order is:"),
print(longest_substring(s))

