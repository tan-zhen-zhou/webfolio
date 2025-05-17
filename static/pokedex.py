# So that I can read from a CSV file
import csv
from time import sleep
# List of information of all pokemon
all_pokemon = []
all_pokemon_type1 = []
all_pokemon_type2 = []
all_pokemon_total = []
all_pokemon_hp = []
all_pokemon_attack = []
all_pokemon_defense = []
all_pokemon_sp_attack = []
all_pokemon_sp_defend = []
all_pokemon_speed = []
all_pokemon_generation = []
all_pokemon_legendary = []

# Note: I didn't know how to read from a CSV file, so I had to ask ChatGPT for help
# Also, I had to ask ChatGPT for help to "align" the table, because my table was easily disjointed

# Open the CSV file
with open('pokemon.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append each attribute to the respective list
        all_pokemon.append(row[1])  # Name
        all_pokemon_type1.append(row[2])
        all_pokemon_type2.append(row[3])
        all_pokemon_total.append(int(row[4]))
        all_pokemon_hp.append(int(row[5]))
        all_pokemon_attack.append(int(row[6]))
        all_pokemon_defense.append(int(row[7]))
        all_pokemon_sp_attack.append(int(row[8]))
        all_pokemon_sp_defend.append(int(row[9]))
        all_pokemon_speed.append(int(row[10]))
        all_pokemon_generation.append(int(row[11]))
        all_pokemon_legendary.append(row[12] == "TRUE")

# User defined functions
def display_pokemon(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary):
    '''Asks the user to enter number of pokemon to display and displays that number of pokemon'''
    # Asks for number of pokemon and prints the header
    iteration = int(input("Enter number of pokemon to display: "))
    print(f"{'No':<4} {'Name':<25} {'Type 1':<10} {'Type 2':<10} {'Total':<6} {'HP':<4} {'Attack':<7} {'Defense':<8} {'Sp. Atk':<8} {'Sp. Def':<8} {'Speed':<6} {'Gen':<4} {'Legendary':<10}")
    # For loop to print the information of each pokemon
    for i in range(iteration):
        print(f"{i+1:<4} {all_pokemon[i]:<25} {all_pokemon_type1[i]:<10} {all_pokemon_type2[i]:<10} {all_pokemon_total[i]:<6} "
      f"{all_pokemon_hp[i]:<4} {all_pokemon_attack[i]:<7} {all_pokemon_defense[i]:<8} {all_pokemon_sp_attack[i]:<8} "
      f"{all_pokemon_sp_defend[i]:<8} {all_pokemon_speed[i]:<6} {all_pokemon_generation[i]:<4} {all_pokemon_legendary[i]:<10}")

def first_type(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary):
    '''Asks the user to enter a type of pokemon and displays the first pokemon with that type'''
    # Check to print for header
    check = 0
    # Input type
    pokemon_type = input("Enter Type: ")
    # Finds out if the type is inside the lists all_pokemon_type1 or all_pokemon_type2
    if pokemon_type not in all_pokemon_type1 or pokemon_type not in all_pokemon_type2:
        print("No pokemon of this type.")
    else:
        # For loop to search through the list
        for i in range(len(all_pokemon_type1)):
            # Prints header when needed
            if pokemon_type == all_pokemon_type1[i]:
                check += 1
                if check == 1:
                    print(f"{'No':<4} {'Name':<25} {'Type 1':<10} {'Type 2':<10} {'Total':<6} {'HP':<4} {'Attack':<7} {'Defense':<8} {'Sp. Atk':<8} {'Sp. Def':<8} {'Speed':<6} {'Gen':<4} {'Legendary':<10}")
                # Prints each pokemon that fulfills the criteria
                print(f"{i+1:<4} {all_pokemon[i]:<25} {all_pokemon_type1[i]:<10} {all_pokemon_type2[i]:<10} {all_pokemon_total[i]:<6} "
      f"{all_pokemon_hp[i]:<4} {all_pokemon_attack[i]:<7} {all_pokemon_defense[i]:<8} {all_pokemon_sp_attack[i]:<8} "
      f"{all_pokemon_sp_defend[i]:<8} {all_pokemon_speed[i]:<6} {all_pokemon_generation[i]:<4} {all_pokemon_legendary[i]:<10}")
                break

def total_base_stat(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary):
    '''Asks the user to enter a total base stat, then outputs the pokemon with the same stat'''
    base_stat = int(input("Enter total base stat: "))
    # Check to print for header/if nothing can be printed
    check = 0
    for i in range(len(all_pokemon_total)):
        # Increments check
        if base_stat == all_pokemon_total[i]:
            check += 1
            # Prints header if needed
            if check == 1:
                print(f"{'No':<4} {'Name':<25} {'Type 1':<10} {'Type 2':<10} {'Total':<6} {'HP':<4} {'Attack':<7} {'Defense':<8} {'Sp. Atk':<8} {'Sp. Def':<8} {'Speed':<6} {'Gen':<4} {'Legendary':<10}")
            # Prints the data of pokemon if it meets the criteria
            print(f"{i+1:<4} {all_pokemon[i]:<25} {all_pokemon_type1[i]:<10} {all_pokemon_type2[i]:<10} {all_pokemon_total[i]:<6} "
      f"{all_pokemon_hp[i]:<4} {all_pokemon_attack[i]:<7} {all_pokemon_defense[i]:<8} {all_pokemon_sp_attack[i]:<8} "
      f"{all_pokemon_sp_defend[i]:<8} {all_pokemon_speed[i]:<6} {all_pokemon_generation[i]:<4} {all_pokemon_legendary[i]:<10}")
    # Print this if nothing can be found
    if check == 0:
        print("No pokemon with this Total Base Stat.")

def min_set_stat(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary):
    '''Asks the user to enter minimum special attack, defense and speed then outputs pokemon with these stats or higher'''
    # Check to print for header/if nothing can be printed
    check = 0
    # Inputs
    min_special_atk = int(input("Enter min special attack stat: "))
    min_special_def = int(input("Enter min special defense stat: "))
    min_speed = int(input("Enter min speed stat: "))
    for i in range(len(all_pokemon)):
        # Check if the special attack, special defence and speed is equal to or larger than required
        if all_pokemon_sp_attack[i] >= min_special_atk and all_pokemon_sp_defend[i] >= min_special_def and all_pokemon_speed[i] >= min_speed:
            check += 1
            # Prints header if needed
            if check == 1:
                print(f"{'No':<4} {'Name':<25} {'Type 1':<10} {'Type 2':<10} {'Total':<6} {'HP':<4} {'Attack':<7} {'Defense':<8} {'Sp. Atk':<8} {'Sp. Def':<8} {'Speed':<6} {'Gen':<4} {'Legendary':<10}")
            # Prints the info of the pokemon
            print(f"{i+1:<4} {all_pokemon[i]:<25} {all_pokemon_type1[i]:<10} {all_pokemon_type2[i]:<10} {all_pokemon_total[i]:<6} "
      f"{all_pokemon_hp[i]:<4} {all_pokemon_attack[i]:<7} {all_pokemon_defense[i]:<8} {all_pokemon_sp_attack[i]:<8} "
      f"{all_pokemon_sp_defend[i]:<8} {all_pokemon_speed[i]:<6} {all_pokemon_generation[i]:<4} {all_pokemon_legendary[i]:<10}")
    if check == 0:
        print("No pokemon has such powerful stats")
                
def legendary(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary):
    '''Asks the user to enter the two types of the legendary pokemon, then outputs the legendary pokemon'''
    # Check to print for header/if nothing can be printed
    check = 0
    type1 = input("Enter Type1: ")
    type2 = input("Enter Type2: ")
    for i in range(len(all_pokemon)):
        # Check if the legendary pokemon's type matches what the user wants
        if all_pokemon_legendary[i] == True and all_pokemon_type1[i] == type1 and all_pokemon_type2[i] == type2:
            check += 1
            # Prints header if needed
            if check == 1:
                print(f"{'No':<4} {'Name':<25} {'Type 1':<10} {'Type 2':<10} {'Total':<6} {'HP':<4} {'Attack':<7} {'Defense':<8} {'Sp. Atk':<8} {'Sp. Def':<8} {'Speed':<6} {'Gen':<4} {'Legendary':<10}")

            # Prints info of pokemon
            print(f"{i+1:<4} {all_pokemon[i]:<25} {all_pokemon_type1[i]:<10} {all_pokemon_type2[i]:<10} {all_pokemon_total[i]:<6} "
      f"{all_pokemon_hp[i]:<4} {all_pokemon_attack[i]:<7} {all_pokemon_defense[i]:<8} {all_pokemon_sp_attack[i]:<8} "
      f"{all_pokemon_sp_defend[i]:<8} {all_pokemon_speed[i]:<6} {all_pokemon_generation[i]:<4} {all_pokemon_legendary[i]:<10}")
    if check == 0:
        print("No such legendary pokemon")

# Main Menu loop, validates or takes in instructions from users
# Initialise option
option = -1
while option != 0:
    print("""Pokemon Super Search Engine
1. Display Pokemon with their types and statistics
2. Display the first Pokemon of a Type of your choice
3. Display all Pokemon with Total Base stat of your choice
4. Display all Pokemon with a minimum set of stats
5. Display all legendary Pokemon of specific Type1 and Type2
6. Surprise
0. Quit
\n""")
    # Asks for option, then runs the UDF that does what the user says
    option = int(input("Enter option: "))
    if option == 1:
        display_pokemon(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary)
    elif option == 2:
        first_type(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary)
    elif option == 3:
        total_base_stat(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary)
    elif option == 4:
        min_set_stat(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary)
    elif option == 5:
        legendary(all_pokemon,all_pokemon_type1,all_pokemon_type2,all_pokemon_total,all_pokemon_hp,all_pokemon_attack,all_pokemon_defense,all_pokemon_sp_attack,all_pokemon_sp_defend,all_pokemon_speed,all_pokemon_generation,all_pokemon_legendary)
    elif option == 6:
        # Surprise reverses the name of every pokemon
        print("Loading surprise...")
        surprise_lst = []
        for i in range(len(all_pokemon)):
            surprise_lst.append(all_pokemon[i][::-1])
        all_pokemon = surprise_lst
        sleep(3)
        print("Done")

print("Bye")