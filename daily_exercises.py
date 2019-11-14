# original = "abcdefghij"
# first = original[:3]
# last = original[3:]
# final = first + last
# print(final)

# for letters in "Pyhton":
#     print(letters)


# def lacking_ends():
#     word = input("Type in a word consisting of 3 or more letters.")
#     if len(word) >= 2:
#         print(word[1:len(word) - 1])


# def longest_word(words):
#     longest = len(words[0])
#     for x in words:
#         if len(x) > longest:
#             longest = len(x)
#     print(longest)


# def upper_lower():
#     sentence = input("Type in a sentence and watch it transform.")
#     print(sentence.upper())
#     print(sentence.lower())


# def title_case():
#     sentence_2 = input("Type in a Sentence and watch it become a title.")
#     new_sentence_2 = sentence_2.split(" ")
#     blank = []
#     for x in new_sentence_2:
#         blank.append(x[0].upper() + x[1:])
#     name = " ".join(blank)
#     print(name)


def replace_4():
    sentence_3 = input("Type in a sentence with at least one four letter word.")
    split_list = sentence_3.split(" ")
    new_sentence_3 = []
    if len(word) in split_list == 4:
        word += "#$%@"
        new_sentence_3.append(word)
    else:
        new_sentence_3.append(word)
    phrase = " ".join(new_sentence_3)
    print(phrase)


def main():
    # lacking_ends()
    # longest_word(["dog", "fish", "bear", "horse", "falcon", "Phoenix"])
    # upper_lower()
    # title_case()
    replace_4()


main()
