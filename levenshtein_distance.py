def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)

    cost = 0 if s[0] == t[0] else 1

    res = min([levenshtein(s[1:], t) + 1,
               levenshtein(s, t[1:]) + 1,
               levenshtein(s[1:], t[1:]) + cost])

    return res

print(levenshtein("examen", "restanta"))
s = "examen"
print(s,s[1:])