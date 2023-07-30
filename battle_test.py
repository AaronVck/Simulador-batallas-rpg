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
        print(f'{self.name} puede realizar {DMG} puntos fijos de danio {character.name}')
        print('*******************************************************************')
        input()

    def Take_damage(self, damage, character):
        DMG_REDUCTION = self.DEF/(100+self.DEF)
        DMG = (character.ATK+damage) * DMG_REDUCTION
        self.HP = self.HP - round(DMG)
        print('/////////////////////////////////////////////////')
        print(f'{character.name} hizo {str(round(DMG))} de danio...')
        input()
        print(f'Los puntos de salud de {self.name} son {self.HP}')
        print('/////////////////////////////////////////////////')
        input()

    def Status(self):
        print('______________________________________')
        print(f'Nombre: {self.name}')
        print(f'Nivel: {self.level}')
        print(f'Puntos de salud {self.HP}')
        print(f'Puntos de ataque {self.ATK}')
        print(f'Puntos de defensa {self.DEF}')
        print('______________________________________')
        input()
  
    def Fight(self, enemy, y_character, e_character):
        ally_hp = self.HP 
        enemy_hp = enemy.HP 
        while(self.HP > 0 and enemy.HP > 0):
            print('\033c', end='')
            print('Es tu turno')
            movement = int(input(f'Define el danio adicional que {self.Get_name()} va a realizar (Solo números entre 1-100): '))
            enemy.Take_damage(movement, y_character[0])
            
            if self.validate_win(y_character, e_character, ally_hp, enemy_hp, enemy) == True:
                break
            print(f'Es el turno {enemy.Get_name()}...')
            enemy_movement = random.randint(1, 100)
            print(f'El/Ella va a hacer {enemy_movement} de danio adicional.')
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
            print('Felicidades, ganaste!!')
            input()
            return True
            
            
        elif(y_character[0].HP < e_character[0].HP and y_character[0].HP <= 0):
            enemy_hp = enemy.HP
            self.HP = ally_hp
            print('Mejor suerte la proxima...')
            input()
            return True
            



def Validation():
    print('///////////////////////////////////////////////////')
    print('Por favor seleccione un personaje antes de ver las estadisticas.')
    print('///////////////////////////////////////////////////')
    input()

def Validation_select():
    print('///////////////////////////////////////////////////')
    print('Por favor cree un personaje antes de seleccionar uno.')
    print('///////////////////////////////////////////////////')
    input()

def Create(characters):
    print('____________________________________________')
    print('Recomendamos que el nivel no este por encima de 100 y que el resto de estadisticas esten por debajo de 255')

    name = input('Nombre: ')
    level = int(input('Nivel: '))
    Validate_level(level)
    hp = int(input('PS: '))
    Validate_stats(hp)
    atk = int(input('ATQ: '))
    Validate_stats(atk)
    deff = int(input('DEF: '))
    Validate_stats(deff)

    creation = Character(name, level, hp, atk, deff)

    characters.append(creation)

    print('Personaje creado satisfactoriamente.')
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

    char = int(input('Seleccione un personaje (Por numero): ')) - 1

    y_character.append(characters[char])

    print(f'Haz seleccionado a {characters[char].Get_name()} como tu personaje.')
    input()

def Select_enemy(e_character, characters):

    e_character.clear()

    select = input('¿Quieres un enemigo aleatorio? S/N').upper()

    if select == 'S':

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

        char = int(input('Selecciona un personaje (Por numero): ')) - 1
        e_character.append(characters[char])
        print(f'Haz seleccionado a {characters[char].Get_name()} como tu enemigo.')
        input()

    else:
                
        print('Selecciona una opcion valida')

def Validate_level(level):
    if level > 100:

        print('\033c', end='')
        print('///////////////////////////////////////////////////')
        print('No puedes crear personajes por encima del nivel 100.')
        print('///////////////////////////////////////////////////')
        input()
        run()

    else:
        pass

def Validate_stats(stat):
    if stat > 255:

        print('\033c', end='')
        print('///////////////////////////////////////////////////')
        print('No puedes crear personajes con estadisticas superiores a 255.')
        print('///////////////////////////////////////////////////')
        input()
        run()

    else:
        pass


def run():

    

    

    menu="""Bienvenido al simulador de batallas
1.-Crear un personaje
2.-Seleccionar tu personaje
3.-Seleccionar un enemigo
4.-Mostrar tus estadisticas
5.-Mostrar estadisticas enemigas
6.-Luchar
7.-Salir"""
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
                    print('Tu personaje:')

                    y_character[0].Status()

            elif option == 5:

                if len(e_character) == 0:

                    print('\033c', end='')
                    Validation()

                else:

                    print('\033c', end='')
                    print('Personaje enemigo:')

                    e_character[0].Status()

            elif option == 6:

                try:
                    print('\033c', end='')
                    y_character[0].Fight(e_character[0], y_character, e_character)

                except IndexError:
                    print('\033c', end='')
                    print('///////////////////////////////////////////////////')
                    print('Por favor selecciona personajes antes de luchar.')
                    print('///////////////////////////////////////////////////')
                    input()
            

            elif option == 7:
            
                break

            else:
                print('\033c', end='')
                print('Por favor selecciona una opcion valida')
                input() 
        except ValueError:
            print('\033c', end='')
            print('Por favor selecciona una opcion correcta')
            input()

        
          
if __name__ == '__main__':
    run()