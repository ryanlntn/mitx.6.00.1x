def count_bobs(s):
    total = 0
    segment_size = len('bob')
    for i in range(len(s)):
        segment = s[i:(i+segment_size)]
        if segment == 'bob':
            total += 1
    return total

print("Number of times bob occurs is:"),
print(count_bobs(s))
