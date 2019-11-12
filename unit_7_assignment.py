#By Kwame Boamah Tuesday, November 12th, 2019


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    deq = input("Do you wish to (e)ncode, (d)ecode, or (q)uit")
    if deq == "q":
        return"Goodbye."
    chosen_string = ("Type in something to encode/decode")
    rotate = int(input("How many rotations do you want to see"))
    codex = alphabet[rotate:] + alphabet[:rotate]
    if deq == "e":
        for words in chosen_string:
            return chosen_string[len(chosen_string)] == codex[len(chosen_string)]
    print(chosen_string)
    if deq == "d":
        for chosen_string in chosen_string:
            return codex[len(chosen_string)] == chosen_string[len(chosen_string)]
    print(codex)


main()
