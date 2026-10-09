def group_anagrams(lst):
    groups = {}
    for w in lst:
        key = "".join(sorted(w).lower())
        if key in groups:
            groups[key].append(w)
        else:
            groups[key] = [w]
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))