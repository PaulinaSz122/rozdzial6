# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Wyświetl instrukcję gry"""
    print(
        """
        Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
        gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
        ludzkim mózgiem a moim krzemowym procesorem.
 
        Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
        Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
 
                        0 | 1 | 2
                        --+---+--
                        3 | 4 | 5
                        --+---+--
                        6 | 7 | 8
 
        Przygotuj się, Człowieku. Ostateczna batalia niebawem się rozpocznie. \n
        """
    )


def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Ustal czy pierwszy ruch należy do gracza, czy do komputera"""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("Więc pierwszy ruch należy do Ciebie. Będzie Ci potrzebny.")
        human = X
        computer = O
    else:
        print("Twoja odwaga Cię zgubi... Ja wykonuję pierwszy ruch.")
        human = O
        computer = X
    return computer, human


def new_board():
    """Utwórz nową planszę gry."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Wyświetl planszę gry na ekranie"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print("\t", board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    """Utwórz listę prawidłowych ruchów"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Ustal zwycięzcę gry."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[3]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def

