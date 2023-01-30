def longest_common_seq(str1, str2):
    if str1 == "" or str2 == "":
        return ""

    if str1[0] == str2[0]:
        return str1[0] + longest_common_seq(str1[1:], str2[1:])

    elif len(longest_common_seq(str1[1:], str2)) > len(longest_common_seq(str1, str2[1:])):
        return longest_common_seq(str1[1:], str2)
    else:
        return longest_common_seq(str1, str2[1:])


def shortest_common_seq(str1, str2):
    com, i, j = "", 0, 0
    for char in longest_common_seq(str1, str2):
        # Add str1 prefix
        while str1[i] != char:
            com += str1[i]
            i += 1

        # Add str2 prefix
        while str2[j] != char:
            com += str2[j]
            j += 1

        # Add common seq
        com += char
        i, j = i + 1, j + 1

    # Return with str1 and str2 suffix
    return com + str1[i:] + str2[j:]


text1 = input("Str1 = ")
text2 = input("Str2 = ")

print(shortest_common_seq(text1, text2))
