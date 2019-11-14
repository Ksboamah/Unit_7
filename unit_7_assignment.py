#By Kwame Boamah Tuesday, November 12th, 2019


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    deq = input("Do you wish to (e)ncode, (d)ecode, or (q)uit")
    if deq == "q":
        print("Goodbye.")
    else:
        chosen_string = input("Type in something to encode/decode")
        rotate = int(input("How many rotations do you want to see"))
        codex = alphabet[rotate:] + alphabet[:rotate]
        if deq == "e":
            new_string = ""
            for letters in chosen_string:
                if letters not in alphabet:
                    new_string += letters
                else:
                    position = alphabet.index(letters)
                    new_string += codex[position]
            print(new_string)
        elif deq == "d":
            new_string = ""
            for letters in chosen_string:
                if letters not in codex:
                    new_string += letters
                else:
                    position = codex.index(letters)
                    new_string += alphabet[position]
            print(new_string)


main()
