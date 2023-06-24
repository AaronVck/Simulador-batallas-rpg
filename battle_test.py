import random

class Character():
    def __init__(self, name, level, hp, atk, deff):
        self.level = level
        self.name = name
        self.HP = hp+(level/100)*hp
        self.ATK = atk+(level/100)*atk
        self.DEF = deff+(level/100)*deff
        
    def Attack(self, character):
        DMG_REDUCTION = character.DEF/(100+character.DEF)
        DMG = self.ATK * DMG_REDUCTION
        print('*******************************************************************')
        print(f'{self.name} can realize {DMG} points of flat damage to {character.name}')
        print('*******************************************************************')
        input()

    def Take_damage(self, damage, character):
        DMG_REDUCTION = self.DEF/(100+self.DEF)
        DMG = (character.ATK+damage) * DMG_REDUCTION
        self.HP = self.HP - round(DMG)
        print('/////////////////////////////////////////////////')
        print(f'{character.name} did {str(round(DMG))} of damage...')
        input()
        print(f'The Health Points of {self.name} are {self.HP}')
        print('/////////////////////////////////////////////////')
        input()

    def Status(self):
        print('______________________________________')
        print(f'Name: {self.name}')
        print(f'Level: {self.level}')
        print(f'Health Points {self.HP}')
        print(f'Attack Points {self.ATK}')
        print(f'Deffense Points {self.DEF}')
        print('______________________________________')
        input()
  
    def Fight(self, enemy, y_character, e_character):
        ally_hp = self.HP 
        enemy_hp = enemy.HP 
        while(self.HP > 0 and enemy.HP > 0):
            print('\033c', end='')
            print('Its your turn')
            movement = int(input(f'Define the additional damage that {self.Get_name()}is gonna do (Only numbers beetween 1-100): '))
            enemy.Take_damage(movement, y_character[0])
            
            if self.validate_win(y_character, e_character, ally_hp, enemy_hp, enemy) == True:
                break
            print(f'Its the turn of {enemy.Get_name()}...')
            enemy_movement = random.randint(1, 100)
            print(f'He/She is gonna do {enemy_movement} of additional damage.')
            input()
            self.Take_damage(enemy_movement, enemy)
            
            if self.validate_win(y_character, e_character, ally_hp, enemy_hp, enemy) == True:
                break
        

        
            
            

    def Get_name(self):
            
        return self.name

    def validate_win(self, y_character, e_character, ally_hp, enemy_hp, enemy):
        if(y_character[0].HP > e_character[0].HP and e_character[0].HP <= 0):
            enemy.HP = enemy_hp
            self.HP = ally_hp
            print('Congratulations, you win!!')
            input()
            return True
            
            
        elif(y_character[0].HP < e_character[0].HP and y_character[0].HP <= 0):
            enemy_hp = enemy.HP
            self.HP = ally_hp
            print('Better luck at the next time...')
            input()
            return True
            



def Validation():
    print('///////////////////////////////////////////////////')
    print('Please select a character before seeing the stats')
    print('///////////////////////////////////////////////////')
    input()

def Validation_select():
    print('///////////////////////////////////////////////////')
    print('Please create a character before select one')
    print('///////////////////////////////////////////////////')
    input()

def Create(characters):
    print('____________________________________________')
    print('We recommend that the level dont be above 100 and also the other stats should be under 255')

    name = input('Name: ')
    level = int(input('Level: '))
    Validate_level(level)
    hp = int(input('HP: '))
    Validate_stats(hp)
    atk = int(input('ATK: '))
    Validate_stats(atk)
    deff = int(input('DEFF: '))
    Validate_stats(deff)

    creation = Character(name, level, hp, atk, deff)

    characters.append(creation)

    print('Character created succesfully')
    print('____________________________________________')
    input()
    
def Select_ally(y_character,characters):
    y_character.clear()
            
    for i in range(0, len(characters)):

        print('**************************')
        print('')
        print(f'{str(i+1)}.- {characters[i].Get_name()}')
        print('')
        print('**************************')

    char = int(input('Pick one character (By number): ')) - 1

    y_character.append(characters[char])

    print(f'You have selected {characters[char].Get_name()} as your character')
    input()

def Select_enemy(e_character, characters):

    e_character.clear()

    select = input('You want a random enemy? Y/N').upper()

    if select == 'Y':

        random_number = random.randint(0, len(characters)-1)
        e_character.append(characters[random_number])
        input()

    elif select == 'N':

        for i in range(0, len(characters)):

            print('**************************')
            print('')
            print(f'{str(i+1)}.- {characters[i].Get_name()}')
            print('')
            print('**************************')

        char = int(input('Pick one character (By number): ')) - 1
        e_character.append(characters[char])
        print(f'You have selected {characters[char].Get_name()} as your enemy')
        input()

    else:
                
        print('Select a correct option')

def Validate_level(level):
    if level > 100:

        print('\033c', end='')
        print('///////////////////////////////////////////////////')
        print('You cant create a character above level 100')
        print('///////////////////////////////////////////////////')
        input()
        run()

    else:
        pass

def Validate_stats(stat):
    if stat > 255:

        print('\033c', end='')
        print('///////////////////////////////////////////////////')
        print('You cant create a character with stats above 255')
        print('///////////////////////////////////////////////////')
        input()
        run()

    else:
        pass


def run():

    

    

    menu="""Welcome to battle system simulator
1.-Create a character
2.-Select your character
3.-Select an enemy
4.-Show your status
5.-Show enemy status
6.-Fight
7.-Exit"""
    characters = []
    y_character = []
    e_character = []
    
    while(True): 
        try:
            option = int(input(f'{menu}'))

            if option == 1:
                print('\033c', end='')
                Create(characters)

            elif option == 2:

                if len(characters) == 0:

                    print('\033c', end='')
                    Validation_select()

                else:

                    print('\033c', end='')
                    Select_ally(y_character, characters)

            elif option == 3:
                if len(characters) == 0:

                    print('\033c', end='')
                    Validation_select()

                else:

                    print('\033c', end='')
                    Select_enemy(e_character, characters)

            elif option == 4:

                if len(y_character) == 0:

                    print('\033c', end='')
                    Validation()

                else:

                    print('\033c', end='')
                    print('Your character:')

                    y_character[0].Status()

            elif option == 5:

                if len(e_character) == 0:

                    print('\033c', end='')
                    Validation()

                else:

                    print('\033c', end='')
                    print('Enemy character:')

                    e_character[0].Status()

            elif option == 6:

                try:
                    print('\033c', end='')
                    y_character[0].Fight(e_character[0], y_character, e_character)

                except IndexError:
                    print('\033c', end='')
                    print('///////////////////////////////////////////////////')
                    print('Please select the characters before fight')
                    print('///////////////////////////////////////////////////')
                    input()
            

            elif option == 7:
            
                break

            else:
                print('\033c', end='')
                print('Please, enter a correct option')
                input() 
        except ValueError:
            print('\033c', end='')
            print('Please, enter a correct option')
            input()

        """subaru = Character('Subaru', 30, 200, 40, 60)
        emilia = Character('Emilia', 60, 600, 90, 100)
        subaru.Attack(emilia)
        emilia.Status()
        emilia.Take_damage(20, subaru)
        emilia.Status()"""
          
if __name__ == '__main__':
    run()