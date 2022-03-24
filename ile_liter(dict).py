s = "aabbcddeee"
dict = {}
for ch in s:
    keys = dict.keys()
    if ch in keys:
        dict[ch] += 1
    else:
        dict[ch] = 1
print(dict)
