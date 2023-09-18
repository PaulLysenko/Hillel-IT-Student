from random import randint


class GameFigure:
    """
    Клас містить dict з усіма ігровими фігурами та їх номером.
    """
    figure_dict = {
        1: 'rock',
        2: 'paper',
        3: 'scissors',
        4: 'lizard',
        5: 'spock'
    }


class Player:
    """
    Батьківський клас.
    """
    def __init__(self, figure):
        self.figure = figure


class HumanPlayer(Player):
    """
    Ініціалізує гравця з обраною фігурою, перевіряючи правильність введення;

    param val:
        Обрана фігура гравця.
    """
    def __init__(self, val):
        if val in GameFigure.figure_dict.values():
            super().__init__(figure=val)
        else:
            raise ValueError(f'There is no such option: {val}')


class HumanGetter:
    """
    1.Приймає варіант фігури гравця через input;
    2.Перевіряє варінт на відповідність до вимог.
    """
    while True:
        user_input = input('Enter figure: ')
        if user_input.isalpha():
            if user_input.lower() in ['paper', 'rock', 'scissors', 'lizard', 'spock']:
                lower = user_input.lower()
                break
            else:
                print("Enter ONLY needed options: 'paper', 'rock', 'scissors', 'lizard', 'spock'")
        else:
            print("You didn't enter any of needed options: 'paper', 'rock', 'scissors', 'lizard', 'spock'")


human = HumanPlayer(HumanGetter.lower)    #Ініціалізуємо гравця


class AIPLayer(Player):
    """
    Ініціалізує гравця AI.
    Обирає варіант фігури ком'ютера за допомогою randint.
    """
    def __init__(self):
        ai_num = randint(1, 5)
        ai_figure = GameFigure.figure_dict.get(ai_num)
        super().__init__(figure=ai_figure)


AI = AIPLayer()    #Ініціалізуємо гравця AI на базі randint


class Game:
    """
    Клас відповідальний за проведення гри.
    Містить збірку правил для кожної фігури.
    """
    rules_dict = {
        'paper': ('rock', 'spock'),
        'rock': ('scissors', 'lizard'),
        'scissors': ('paper', 'lizard'),
        'lizard': ('spock', 'paper'),
        'spock': ('scissors', 'rock')
    }

    @staticmethod
    def fight():
        """
        Проводить гру між гравцем і AI, визначаючи переможця.

        return: Результат гри.

        """
        hum = human.figure
        ai = AI.figure
        if hum == ai:
            return 'Oof, it\'s a tie'
        elif ai in Game.rules_dict.get(hum):
            return 'WOW you won!'
        else:
            return 'You lost to AI \nHa-ha :('


rps_game = Game.fight()    #Створюємо гру
print(rps_game)    #Виводимо результат гри на екран
