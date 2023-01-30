def longest_common_seq(str1, str2):
    # Check if strings are empty
    if str1 == "" or str2 == "":
        return 0

    # Check if they share common chr
    if str1[0] == str2[0]:
        return 1 + longest_common_seq(str1[1:], str2[1:])

    else:
        return max(longest_common_seq(str1[1:], str2), longest_common_seq(str1, str2[1:]))


text1 = input("Str1 = ")
text2 = input("Str2 = ")

print(longest_common_seq(text1, text2))
