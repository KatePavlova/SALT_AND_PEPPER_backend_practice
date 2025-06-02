class WrongNumberOfPlayersError(Exception):
    def __str__(self):
        return "WrongNumberOfPlayersError"

class NoSuchStrategyError(Exception):
    def __str__(self):
        return "NoSuchStrategyError"

class DataFormatError(Exception):
    def __str__(self):
        return "DataFormatError"


def check_arguments(arg):
    if type(arg) is not list:
        raise DataFormatError
    for item in arg:
        if type(item) is not list:
            raise DataFormatError
        if len(item) != 2:
            raise DataFormatError
        if type(item[0]) is not str and type(item[1]) is not str:
            raise DataFormatError

def rps_game_winner(player_choice = None):
    check_arguments(player_choice)
    strategy = {'R': 0, 'S': 1, 'P': 2}

    if len(player_choice) < 1 or len(player_choice) > 2:
        raise WrongNumberOfPlayersError

    try:
        player1 = strategy[player_choice[0][1]]
        player2 = strategy[player_choice[-1][1]]

        if ((player2 - player1) % 3 <= 1):
            return ' '.join(player_choice[0])
        else:
            return ' '.join(player_choice[-1])

    except KeyError:
        raise NoSuchStrategyError


if __name__ == "__main__":
    TESTS = [[['player1', 'P'], ['player2', 'S'], ['player3', 'S']],   #    = > WrongNumberOfPlayersError
             [['player1', 'P'], ['player2', 'A']],                     #    = > NoSuchStrategyError
             [['player1', 'P'], ['player2', 'S']],                     #    = > 'player2 S'
             [['player1', 'P'], ['player2', 'P']],                     #    = > 'player1 P'
             [['player1', 'P']],                                       #    = > 'player1 P'
             [['player1', 'R'], ['player2', 'P']]]                     #    = > 'player2 P'

    for test in TESTS:
        try:
            print(rps_game_winner(test))
        except Exception as e:
            print(e)



