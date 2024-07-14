import random
 
class Game:
    def __init__(self):
        # get the computer's pick 
        self.computer_pick = self.get_computer_pick()
        
        # get the user's pick
        self.user = self.get_user_pick()
 
        # get the result of the game
        self.result = self.get_result()     
    
    def get_computer_pick(self):
        # get random number among 1, 2 and 3
        random_number = random.randint(1, 3)
        
        # possible options 
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        
        # return the value present at random_number
        return options[random_number]
 
    def get_user_pick(self):
        
        # infinite while loop 
        while True:
            user = input('Enter rock/paper/scissors: ')
 
            # convert to lowercase
            user = user.lower()
 
            # if user_pick is either rock or paper or scissors,
            # terminate the loop
            if user in ('rock', 'paper', 'scissors'):
                  break
            else:
                print('Wrong input!')
 
        return user
 
    def get_result(self):
        # condition for draw
        if self.computer_pick == self.user:
            return 'draw'
        
        # condition for the user to win
        elif self.user == 'paper' and self.computer_pick == 'rock':
            return 'win'
        elif self.user == 'rock' and self.computer_pick == 'scissors':
            return 'win'
        elif self.user == 'scissors' and self.computer_pick == 'paper':
            return 'win'
        
        # in all other conditions, users lose    
        else:
            return 'lose'
 
    def print_result(self):
        print(f"Computer's pick: {self.computer_pick}")
        print(f'Your pick: {self.user}')
        print(f'You {self.result}')
 
 
# create an object of the Game class
game = Game()
game.print_result()

