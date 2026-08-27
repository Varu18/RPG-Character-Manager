#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

struct Item
{
    std::string nameItem;
    std::string typeItem;
    bool occupied = false;
    int valueItem = 0;
};

struct Monster
{
  std::string nameMonster;
  int monsterHP = 0;
  int monsterMaxHP = 0;
  int monsterDamage = 0;
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

Item healthPotion{"Health Potion", "Consumable", true, 20};
Item ironSword{"Iron Sword", "Weapon", true, 10};
Item manaPotion{"Mana Potion", "Consumable", true, 30};

bool characterCreated = false;
int maxHP = 100;

Monster goblin{"Goblin", 50, 50, 10};
Monster skeleton("Skeleton", 60, 60 ,12);
Monster orc{"Orc", 80, 80, 15};
Monster slime{"Slime", 40, 40, 8};
Monster monsters[4] = {goblin, skeleton, orc, slime};


void showBattle(Player& player, std::string monster, int monsterHP)
{

}

void showMenu()
{
    std::cout << "╔══════════════════════════════╗" << std::endl;
    std::cout << "║      ⚔ RPG CHARACTER ⚔       ║" << std::endl;
    std::cout << "╚══════════════════════════════╝" << std::endl;

    std::cout << std::endl;

    std::cout << "╔══════════════════════════════╗" << std::endl;
    std::cout << "║             MENU             ║" << std::endl;
    std::cout << "╠══════════════════════════════╣" << std::endl;
    std::cout << "║ 👤 1. Create Character       ║" << std::endl;
    std::cout << "║ 📋 2. Show Character         ║" << std::endl;
    std::cout << "║ ⚔️  3. Fight Monster          ║" << std::endl;
    std::cout << "║ ❤️  4. Heal Character         ║" << std::endl;
    std::cout << "║ 🎒 5. Remove Item            ║" << std::endl;
    std::cout << "║ 🧪 6. Use Item               ║" << std::endl;
    std::cout << "║ 🚪 7. Exit                   ║" << std::endl;
    std::cout << "╚══════════════════════════════╝" << std::endl;

}

void useItem(Player& player, int slot)
{
  if (slot < 1 || slot > 5)
  {
    std::cout << "Invalid inventory slot!" << std::endl;
    return;
  }
  if (!player.inventory[slot - 1].occupied)
{
    std::cout << "Inventory slot is empty!" << std::endl;
    return;
}
if (player.inventory[slot - 1].typeItem != "Consumable")
{
    std::cout << "This item is not consumable!" << std::endl;
    return;
}
player.playerHP += player.inventory[slot - 1].valueItem;

if (player.playerHP > maxHP)
{
    player.playerHP = maxHP;
}
std::cout << "You used "
          << player.inventory[slot - 1].nameItem
          << "!" << std::endl;
  player.inventory[slot - 1].occupied = false;
}

void removeItem(Player& player, int slot)
{
  if (slot < 1 || slot > 5)
  {
    std::cout << "Invalid inventory slot!" << std::endl;
    return;
  }
  
  if(!player.inventory[slot - 1].occupied){
    std::cout << "Inventory slot is already empty!" << std::endl;
    return; 
  }
  
  player.inventory[slot - 1].occupied = false;
}

bool addItem(Player& player, Item anotherItem)
{
    for (int i = 0; i < 5; i++)
    {
        if (!player.inventory[i].occupied)
        {
            player.inventory[i] = anotherItem;
            player.inventory[i].occupied = true;
            return true;
        }
    }

    return false;
}

void showInventory(Player& player)
{

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
        else
        {
            std::cout << "Slot " << i + 1 << ": Empty" << std::endl;
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

void showCharacter(Player& player)
{
    std::cout << "╔══════════════════════════════╗" << std::endl;
    std::cout << "║        👤 CHARACTER          ║" << std::endl;
    std::cout << "╠══════════════════════════════╣" << std::endl;
    std::cout << " 🏷️  Name: " << player.playerName << std::endl;
    std::cout << " ⚔️  Class: " << player.playerClass << std::endl;
    std::cout << " ⭐ Level: " << player.playerLevel << std::endl;
    std::cout << " ❤️  HP: " << player.playerHP << " / " << maxHP << std::endl;
    std::cout << " ✨ XP: " << player.playerXP << std::endl;
    std::cout << " 💰 Gold: " << player.playerGold << std::endl;
    std::cout << "══════════════════════════════" << std::endl;

    showInventory(player);
}

void fightMonster(Player& player)
{
    int randomMonster = rand() % 4;
    int damage = monsters[randomMonster].monsterDamage;
    int playerDamage = rand() % 21 + 10;
    int gold = rand() % 16 + 5;
    int randomXP = rand() % 21 + 10;

    monsters[randomMonster].monsterHP = monsters[randomMonster].monsterMaxHP;

    std::cout << "╔══════════════════════════════╗" << std::endl;
    std::cout << "║          ⚔️ BATTLE ⚔️        ║" << std::endl;
    std::cout << "╚══════════════════════════════╝" << std::endl;

    std::cout << "A wild "
              << monsters[randomMonster].nameMonster
              << " appears!" << std::endl;

    std::cout << "You attack the "
              << monsters[randomMonster].nameMonster
              << " for "
              << playerDamage
              << " damage!" << std::endl;

    monsters[randomMonster].monsterHP -= playerDamage;

    if (monsters[randomMonster].monsterHP <= 0)
    {
        std::cout << "💀 The "
                  << monsters[randomMonster].nameMonster
                  << " has been defeated!" << std::endl;

        player.playerGold += gold;
        player.playerXP += randomXP;

        std::cout << "Current HP: "
                  << player.playerHP
                  << std::endl;

        std::cout << std::endl;

        std::cout << "====================" << std::endl;
        std::cout << "REWARDS" << std::endl;
        std::cout << "====================" << std::endl;

        std::cout << "The "
                  << monsters[randomMonster].nameMonster
                  << " dropped "
                  << gold
                  << " gold!" << std::endl;

        std::cout << "You gained "
                  << randomXP
                  << " XP!" << std::endl;

        if (player.playerXP >= 100)
        {
            player.playerLevel += 1;
            player.playerXP -= 100;

            std::cout << std::endl;
            std::cout << "====================" << std::endl;
            std::cout << "LEVEL UP!" << std::endl;
            std::cout << "====================" << std::endl;

            std::cout << "Congratulations!" << std::endl;
            std::cout << "You reached Level "
                      << player.playerLevel
                      << "!" << std::endl;
        }

        return;
    }

    std::cout << "The "
              << monsters[randomMonster].nameMonster
              << " has "
              << monsters[randomMonster].monsterHP
              << " HP remaining!" << std::endl;

    std::cout << "The "
              << monsters[randomMonster].nameMonster
              << " hits you for "
              << damage
              << " damage!" << std::endl;

    player.playerHP -= damage;

    if (player.playerHP <= 0)
    {
        player.playerHP = 0;
        std::cout << "You are dead!" << std::endl;
    }
    else
    {
        player.playerGold += gold;
        player.playerXP += randomXP;

        std::cout << "Current HP: "
                  << player.playerHP
                  << std::endl;

        std::cout << std::endl;

        std::cout << "====================" << std::endl;
        std::cout << "REWARDS" << std::endl;
        std::cout << "====================" << std::endl;

        std::cout << "The "
                  << monsters[randomMonster].nameMonster
                  << " dropped "
                  << gold
                  << " gold!" << std::endl;

        std::cout << "You gained "
                  << randomXP
                  << " XP!" << std::endl;

        if (player.playerXP >= 100)
        {
            player.playerLevel += 1;
            player.playerXP -= 100;

            std::cout << std::endl;
            std::cout << "====================" << std::endl;
            std::cout << "LEVEL UP!" << std::endl;
            std::cout << "====================" << std::endl;

            std::cout << "Congratulations!" << std::endl;
            std::cout << "You reached Level "
                      << player.playerLevel
                      << "!" << std::endl;
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
  else if (option == 5)
{
    int slot;

    showInventory(player);

    std::cout << "Enter inventory slot to remove: ";
    std::cin >> slot;

    removeItem(player, slot);
}
  else if(option == 6){
  
  int slot;

  showInventory(player);

  std::cout << "Enter inventory slot to use:";
  std::cin >> slot;
  
  useItem(player, slot);
}
  else if (option == 7){
    std::cout << "Goodbye!" << std::endl;
  }
else{
    std::cout << "Invalid option!" << std::endl;
}

}
while (option != 7);
return 0;
}
