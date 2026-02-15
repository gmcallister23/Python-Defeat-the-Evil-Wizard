import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= random.randint(self.attack_power - 10, self.attack_power) #Modifying the attack system to have random attack damage within specified range
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

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

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

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
    
    def evade(self):
        print(f'{self.name} has evaded the Wizards attack!  {self.name} takes no damage!')

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=25) #add bonus power somehow

    def divine_shield(self):
        self.health += 5
        print(f'{self.name} had blocked the wizards attack with the Divine Shield!  {self.name} received no damage! \n {self.name} gains +5 health')

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
        return Paladin(name)
    elif class_choice == '4':
        return Archer(name)
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
                player.special_ability(Character)
                action_taken = True
            elif choice == '3':
                player.heal(Character)
                action_taken = True
            elif choice == '4':
                player.display_stats()
                action_taken = False
            else:
                print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

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