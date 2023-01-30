def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)

    cost = 0 if s[-1] == t[-1] else 1

    res = min([levenshtein(s[:-1], t) + 1,
               levenshtein(s, t[:-1]) + 1,
               levenshtein(s[:-1], t[:-1]) + cost])

    return res

file = open("cuvinte.in")
words = file.readline().split()
file.close()

graph = {}
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if words[i] not in graph:
            graph[words[i]] = {}
        if words[j] not in graph:
            graph[words[j]] = {}

        graph[words[i]][words[j]] = levenshtein(words[i], words[j])
        graph[words[j]][words[i]] = levenshtein(words[j], words[i])


