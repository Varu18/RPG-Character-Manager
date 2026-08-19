#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

struct Item
{
    std::string nameItem;
    std::string typeItem;
    bool occupied = false;
};

struct Player
{
    std::string playerName;
    std::string playerClass;
    int playerLevel = 1;
    int playerHP = 100;
    int playerGold = 0;
    int playerXP = 0;

    Item inventory[5];
};

Player player;

Item healthPotion{"Health Potion", "Consumable", true};
Item ironSword{"Iron Sword", "Weapon", true};
Item manaPotion{"Mana Potion", "Consumable", true};

bool characterCreated = false;
int maxHP = 100;
std::string monsters[4] = {"Goblin", "Skeleton", "Orc", "Slime"};

void showMenu(){

    std::cout << "=========================" << std::endl;
    std::cout << "RPG CHARACTER MANAGER" << std::endl;
    std::cout << "=========================" << std::endl;
    std::cout << "1.Create Character" << std::endl;
    std::cout << "2.Show Character" << std::endl;
    std::cout <<"3.Fight monster" << std::endl;
    std::cout <<"4.Heal Character" << std::endl;
    std::cout <<"5.Exit" << std::endl;
        
}

void addItem(Player& player, Item anotherItem)
{
    for (int i = 0; i < 5; i++)
    {
        if (!player.inventory[i].occupied)
        {
            player.inventory[i] = anotherItem;
            player.inventory[i].occupied = true;
            break;
        }
    }
}

void createCharacter(Player& player){
    std::cout << "Enter character name: ";
    std::cin >> player.playerName;

    std::cout << "Enter character class: ";
    std::cin >> player.playerClass;

    player.playerLevel = 1;
    player.playerGold = 0;
    player.playerHP = 100;
    player.playerXP = 0;

  player.inventory[0] = healthPotion;
  player.inventory[1] = ironSword;

  addItem(player, manaPotion);

    std::cout << "Character created!" << std::endl;

    characterCreated = true;
}

void showCharacter(Player player){

    std::cout << "====================" << std::endl;
    std::cout << "Name: " << player.playerName << std::endl;
    std::cout << "Class: " << player.playerClass << std::endl;
    std::cout << "Level: " << player.playerLevel << std::endl;
    std::cout << "XP: " << player.playerXP << std::endl;
    std::cout << "Gold: " << player.playerGold << std::endl;
    std::cout << "Current HP: " << player.playerHP << " / " << maxHP << std::endl;
    std::cout << "====================" << std::endl;
    std::cout << "====================" << std::endl;
    std::cout << "INVENTORY" << std::endl;
    std::cout << "====================" << std::endl;

for (int i = 0; i < 5; i++)
{
    if (player.inventory[i].occupied)
    {
       std::cout << "Slot " << i + 1 << ": "
          << player.inventory[i].nameItem << std::endl;
    }
    else{
      std::cout << "Slot " << i + 1 << ": Empty" << std::endl;
    }
}
}

void fightMonster(Player& player){

  int damage = rand() % 71 + 10;
  int gold = rand() % 16 + 5;
  int randomMonster = rand() % 4;
  int randomXP = rand() % 21 + 10;
  std::cout << "====================" << std::endl;
  std::cout << "BATTLE" << std::endl;
  std::cout << "====================" << std::endl;

std::cout << "A wild " << monsters[randomMonster] << " appears!" << std::endl;
std::cout << "The " << monsters[randomMonster] << " hits you for "
          << damage << " damage!" << std::endl;
  
  player.playerHP -= damage;

  if( player.playerHP <= 0){
    player.playerHP = 0;
    std::cout << "You are dead!" << std::endl;
  }
  else{
    player.playerGold += gold;
    player.playerXP += randomXP;
    std::cout << "Current HP: " << player.playerHP << std::endl;
    std::cout << std::endl;
    std::cout << "====================" << std::endl;
    std::cout << "REWARDS" << std::endl;
    std::cout << "====================" << std::endl;
    std::cout << "The " << monsters[randomMonster] << " dropped "
          << gold << " gold!" << std::endl;
    std::cout << "You gained " << randomXP << " XP!" << std::endl;
    if(player.playerXP >= 100){
      player.playerLevel += 1;
      player.playerXP -= 100;
      std::cout << std::endl;
    std::cout << "====================" << std::endl;
    std::cout << "LEVEL UP!" << std::endl;
    std::cout << "====================" << std::endl;

std::cout << "Congratulations!" << std::endl;
std::cout << "You reached Level "
          << player.playerLevel << "!" << std::endl;
    }
    std::cout << std::endl;
    std::cout << "====================" << std::endl;
    std::cout << "UPDATED CHARACTER" << std::endl;
    std::cout << "====================" << std::endl;

showCharacter(player);
  }
}

void healCharacter(Player& player){
  int oldHP = player.playerHP;
  std::cout << "Healing.." << std::endl;
  player.playerHP += 20;

  if( player.playerHP > 100){
    player.playerHP = 100;
  }

  int healedAmount = player.playerHP - oldHP;
  std::cout << "You recovered " << healedAmount << " HP!" << std::endl;
  std::cout << "Current HP: " << player.playerHP << std::endl;
}

int main()
{
     int option;
     std::srand(std::time(0));
do{
   showMenu();

   std::cout << "Choose an option: ";
   std::cin >> option;
  if (option == 1)
  { 
    if(characterCreated){
      std::cout << "Character already exists!" << std::endl;
    }
      else{
      createCharacter(player);
    }
  

  }
  else if (option == 2){

    if(!characterCreated){
      std::cout << "No character has been created yet!" << std::endl;
    }
    else{
    showCharacter(player);
    }
  }
  else if(option == 3){
    
    if(!characterCreated){
      std::cout << "Create a character first!" << std::endl;
    }
    else{

    if(player.playerHP == 0){
      std::cout << "You are already dead!" << std::endl;
    }
    else{
    fightMonster(player);
    }
  }
  }
  else if(option==4){
    healCharacter(player);
  }
  else if (option == 5){
    std::cout << "Goodbye!" << std::endl;
  }
else{
    std::cout << "Invalid option!" << std::endl;
}

}
while (option != 5);
return 0;
}
