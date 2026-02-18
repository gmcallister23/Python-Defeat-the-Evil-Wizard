import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.evade_chance = 0
        self.shield_active = False
        self.wall = 0
        self.random_regen = 0

        #Attribute checks to make sure attributes are ran by every character
        self.double_shot_chance = 0
        self.holy_strike_chance = 0
        self.execute_chance = 0
        self.random_regen = 0
        

    def attack(self, opponent):

        self.random_power = random.randint(max(1, self.attack_power - 10), self.attack_power) #Modifying the attack system to have random attack damage within specified range
        total_damage = self.random_power #initializing total_damage before modifying it
        damage = self.random_power #localizing variable so they can be modified
        total_damage = damage
        opponent.health -= self.random_power
        print(f"{self.name} attacks {opponent.name} for {self.random_power} damage!")

         #this function checks if evade being used and resets evade to 0
        if random.random() < opponent.evade_chance:
            print(f'{opponent.name} evaded the attack!')
            opponent.evade_chance = 0
            return
        #This checks if shield is being used and establishes the damage dealt
        if opponent.shield_active:
            damage = damage // 2 #changed from self.random_power to damage so it wouldn't constantly be modified
            opponent.shield_active = False
            print(f"{opponent.name}'s shield reduced the damage!")

        #double_shot - This function checks if double shot is triggered.  It generates a random float (0-1) and compares it to the double shot chance, then moves on from there
        if random.random() < self.double_shot_chance:
            extra_damage = random.randint(max(1, self.attack_power - 10), self.attack_power)
            opponent.health -= extra_damage
            total_damage += extra_damage #initializing total_damage before modifying it
            print(f'{self.name} fires Double Shot for an extra {total_damage} damage!')
        
        #Holy Strike
        if random.random() < self.holy_strike_chance:
            bonus_damage = int(damage * .25) #updating the value to an int
            opponent.health -= bonus_damage
            total_damage += bonus_damage
            print(f'{self.name} uses Holy Strike for an additional {bonus_damage} damage, causing {total_damage} damage!')

        #Execute - this is an attack that has a really low chance of occurence, but will complete kill the opponent
        if random.random() < self.execute_chance:
            damage = opponent.health
            opponent.health -= damage
            print(f'{self.name} uses the Execute attack, deals {damage} damage.')
        #Warrior wall.  Reduces damage for certain number of turns.  Is triggered by engaging the special ability
        if opponent.wall > 0: 
            damage = damage // 4
            print(f"{opponent.name}'s wall reduces the damage!")

        #The mage can radomly regenerate it's health
        if random.random() < self.random_regen:
            self.health = self.max_health
            print(f'{self.name} has randomly regenerated all their health!')
        
        opponent.health -= damage
        # redundant print(f'{self.name} attacks {opponent.name} for {damage} damage')

        print(f'Total damage dealt: {total_damage}')


        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def end_turn(self):
        if self.wall > 0:
            self.wall -= 1

    def heal(self): #restores 25 health points
        if (self.max_health - self.health) < 25:  #Checks if health points are less than 25 points away from the max health
            self.health = (self.max_health - self.health) + self.health # Finds the difference of health and max health, then adds it back to make sure it doesn't exceed max health
        else:
            self.health = self.health + 25 # adds 25 health points to current health

        print(f'{self.name} has been healed!  {self.name} now has: {self.health}/{self.max_health}')
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.execute_chance = 0.05

    def special_ability(self, opponent=None):
        self.wall = 3
        print(f'{self.name} builds a defensive wall!  Damage reduced for 3 turns.')

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)
        self.random_regen = 0.33

    #The mage has a special attack ability that allows it to cause double damage, but sacrifices the original amount of damage to be caused
    def special_ability(self, opponent=None):
        damage = random.randint(max(1, self.attack_power - 10), self.attack_power)
        self.health -= damage #Mage loses the original amount of damage in health for this ability
        print(f'{self.name} uses Superbold and sacrifices {damage} health. Current health: {self.health}/{self.max_health}')
        double_damage = damage * 2
        opponent.health = double_damage
        print(f'Superbolt hits {opponent.name} for {double_damage} damage.')

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=40)
        self.double_shot_chance = 0.2 # creates a 20% chance that each attack will be a double shot
    
    #This function determines if evade will be successfully used or not, it uses self.evade_chance to set the probabilty that evade will work 75% of the time
    def special_ability(self, opponent=None):
        self.evade_chance = 0.75
        print(f'{self.name} prepares to evade the next attack!')

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=25) #add bonus power somehow
        self.holy_strike_chance = 0.2 #creates a 20% chance that each attack will include holy strike
    
    #this function calls the shield special ability.  It also adds 5 health whenever attacks are blocked
    def special_ability(self, opponent=None):
        self.shield_active = True
        self.health += 5
        print(f'{self.name} had blocked the wizards attack with the Divine Shield!  {self.name} received reduced damage! \n {self.name} gains +5 health')

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        action_taken = False #Added a loop to offer an additional action if player wants to view stats.  It checks to see if the action was taken, each action has a declaration.  The loop runs, until an action is taken
        while not action_taken:
            print("1. Attack")
            print("2. Use Special Ability")
            print("3. Heal")
            print("4. View Stats")

            choice = input("Choose an action: ")

            if choice == '1':
                player.attack(wizard)
                action_taken = True
            elif choice == '2':
                player.special_ability(wizard)
                action_taken = True
            elif choice == '3':
                player.heal()
                action_taken = True
            elif choice == '4':
                player.display_stats()
                action_taken = False
            else:
                print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        player.end_turn()
        wizard.end_turn()

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()