import random


def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def main():
    print("\tWitaj w grze 'Jaka to liczba'!")
    print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
    print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

    the_number = random.randint(1, 100)
    guess = int(ask_number("Ta liczba to: ", 0, 100))
    tries = 1

    while guess != the_number:
        if guess > the_number:
            print("Za duża...")
        else:
            print("Za mała...")

        guess = int(ask_number("Ta liczba to: ", 0, 100))
        tries += 1

    print("Odgadłeś! Ta liczba to:", the_number)
    print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter")


main()
