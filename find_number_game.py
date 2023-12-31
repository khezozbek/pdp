import random
import sys

Gameover = ValueError


def random_number():
    number = int(random.randint(1, 10))
    return number


def check(number, guess):
    message = ''
    if guess > number:
        message = f"S iz kiritgan {guess}  soni    men o'ylagan sondan katta "
        return message
    if guess < number:
        message = f"siz kiritgan {guess}   soni men o'yalagan sondan kichik  "
        return message

    raise Gameover


def main():
    number = random_number()
    print(f"Salom men  1-10 gacha {number} bir son o\'yladim topishga urinib koringchi sizda 3 ta urinish bor   ")
    i = 1
    while True:
        try:
            guess = int(input(f"{i} tahminigizni kiriting "))
            message = check(number, guess)
            print(message)
            i += 1
            if i == 4:
                sys.exit('siz yutqazdiz ☺!')

        except Gameover:
            print("siz sonni topdingiz ☻!▌")
            break


if __name__ == '__main__':
    main()