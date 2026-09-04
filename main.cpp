#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <exception>

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

Monster goblin{"Goblin", 50, 50, 10};
Monster skeleton{"Skeleton", 60, 60, 12};
Monster orc{"Orc", 80, 80, 15};
Monster slime{"Slime", 40, 40, 8};

Monster monsters[4] = {goblin, skeleton, orc, slime};

bool characterCreated = false;
bool inBattle = false;
int currentMonster = -1;
int maxHP = 100;

void resetInventory()
{
    for (int i = 0; i < 5; i++)
    {
        player.inventory[i] = Item{};
    }
}

bool addItem(Player& player, const Item& item)
{
    for (int i = 0; i < 5; i++)
    {
        if (!player.inventory[i].occupied)
        {
            player.inventory[i] = item;
            player.inventory[i].occupied = true;
            return true;
        }
    }

    return false;
}

void createCharacter(const std::string& name, const std::string& playerClass)
{
    player.playerName = name;
    player.playerClass = playerClass;
    player.playerLevel = 1;
    player.playerHP = 100;
    player.playerGold = 0;
    player.playerXP = 0;
    inBattle = false;
    currentMonster = -1;

    resetInventory();

    addItem(player, healthPotion);
    addItem(player, ironSword);
    addItem(player, manaPotion);

    characterCreated = true;
}

void sendState()
{
    std::cout
        << "STATE|"
        << player.playerName << "|"
        << player.playerClass << "|"
        << player.playerLevel << "|"
        << player.playerHP << "|"
        << maxHP << "|"
        << player.playerGold << "|"
        << player.playerXP
        << std::endl;
}

void sendInventory()
{
    std::cout << "INVENTORY";

    for (int i = 0; i < 5; i++)
    {
        std::cout << "|";

        if (player.inventory[i].occupied)
        {
            std::cout << player.inventory[i].nameItem
                      << ","
                      << player.inventory[i].typeItem
                      << ","
                      << player.inventory[i].valueItem;
        }
        else
        {
            std::cout << "EMPTY";
        }
    }

    std::cout << std::endl;
}

void sendBattleState()
{
    if (!inBattle || currentMonster < 0)
    {
        std::cout << "BATTLE|NONE" << std::endl;
        return;
    }

    Monster& monster = monsters[currentMonster];

    std::cout
        << "BATTLE|"
        << monster.nameMonster << "|"
        << monster.monsterHP << "|"
        << monster.monsterMaxHP << "|"
        << player.playerHP << "|"
        << maxHP
        << std::endl;
}

void startBattle()
{
    if (inBattle)
    {
        std::cout << "ERROR|A battle is already in progress!" << std::endl;
        return;
    }

    currentMonster = rand() % 4;
    monsters[currentMonster].monsterHP =
        monsters[currentMonster].monsterMaxHP;

    inBattle = true;

    std::cout
        << "BATTLE_STARTED|"
        << monsters[currentMonster].nameMonster
        << std::endl;

    sendBattleState();
}

void attack()
{
    if (!inBattle || currentMonster < 0)
    {
        std::cout << "ERROR|Start a battle before attacking!" << std::endl;
        return;
    }

    Monster& monster = monsters[currentMonster];

    int playerDamage = rand() % 21 + 10;

    monster.monsterHP -= playerDamage;

    if (monster.monsterHP <= 0)
    {
        monster.monsterHP = 0;

        int gold = rand() % 16 + 5;
        int xp = rand() % 21 + 10;

        player.playerGold += gold;
        player.playerXP += xp;

        bool levelUp = false;

        while (player.playerXP >= 100)
        {
            player.playerXP -= 100;
            player.playerLevel++;
            levelUp = true;
        }

        inBattle = false;

        std::cout
            << "ATTACK_RESULT|"
            << playerDamage << "|"
            << "DEFEATED|"
            << gold << "|"
            << xp << "|"
            << (levelUp ? 1 : 0)
            << std::endl;

        sendState();
        return;
    }

    int damage = monster.monsterDamage;

    player.playerHP -= damage;

    if (player.playerHP <= 0)
    {
        player.playerHP = 0;
        inBattle = false;

        std::cout
            << "ATTACK_RESULT|"
            << playerDamage << "|"
            << "GAME_OVER|0|0|0"
            << std::endl;

        sendState();
        return;
    }

    std::cout
        << "ATTACK_RESULT|"
        << playerDamage << "|"
        << "CONTINUE|0|0|0"
        << std::endl;

    sendBattleState();
    sendState();
}

void useItem(int slot)
{
    if (slot < 1 || slot > 5)
    {
        std::cout << "ITEM_RESULT|ERROR|Invalid inventory slot!" << std::endl;
        return;
    }

    Item& item = player.inventory[slot - 1];

    if (!item.occupied)
    {
        std::cout << "ITEM_RESULT|ERROR|Inventory slot is empty!" << std::endl;
        return;
    }

    if (item.typeItem != "Consumable")
    {
        std::cout << "ITEM_RESULT|ERROR|This item is not consumable!" << std::endl;
        return;
    }

    std::string itemName = item.nameItem;

    player.playerHP += item.valueItem;

    if (player.playerHP > maxHP)
        player.playerHP = maxHP;

    item.occupied = false;

    std::cout
        << "ITEM_RESULT|SUCCESS|"
        << itemName
        << std::endl;

    sendState();

    if (inBattle)
        sendBattleState();

    sendInventory();
}

void removeItem(int slot)
{
    if (slot < 1 || slot > 5)
    {
        std::cout << "REMOVE_RESULT|ERROR|Invalid inventory slot!" << std::endl;
        return;
    }

    Item& item = player.inventory[slot - 1];

    if (!item.occupied)
    {
        std::cout << "REMOVE_RESULT|ERROR|Inventory slot is empty!" << std::endl;
        return;
    }

    item.occupied = false;

    std::cout << "REMOVE_RESULT|SUCCESS" << std::endl;
    sendInventory();
}

void healCharacter()
{
    if (!characterCreated)
    {
        std::cout << "ERROR|Create a character first!" << std::endl;
        return;
    }

    int oldHP = player.playerHP;

    player.playerHP += 20;

    if (player.playerHP > maxHP)
        player.playerHP = maxHP;

    int healedAmount = player.playerHP - oldHP;

    std::cout
        << "HEAL_RESULT|"
        << healedAmount
        << std::endl;

    sendState();
}

void runFromBattle()
{
    if (!inBattle)
    {
        std::cout << "ERROR|There is no battle to run from!" << std::endl;
        return;
    }

    inBattle = false;
    currentMonster = -1;

    std::cout << "RUN_RESULT|SUCCESS" << std::endl;
}

int main()
{
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    std::string command;

    while (std::getline(std::cin, command))
    {
        if (command == "CREATE")
        {
            std::string name;
            std::string playerClass;

            std::getline(std::cin, name);
            std::getline(std::cin, playerClass);

            createCharacter(name, playerClass);

            std::cout << "CREATE_RESULT|SUCCESS" << std::endl;
            sendState();
            sendInventory();
        }
        else if (command == "STATE")
        {
            sendState();
        }
        else if (command == "INVENTORY")
        {
            sendInventory();
        }
        else if (command == "BATTLE_START")
        {
            if (!characterCreated)
            {
                std::cout << "ERROR|Create a character first!" << std::endl;
            }
            else if (player.playerHP <= 0)
            {
                std::cout << "ERROR|You are already dead!" << std::endl;
            }
            else
            {
                startBattle();
            }
        }
        else if (command == "ATTACK")
        {
            attack();
        }
        else if (command == "USE_ITEM")
        {
            if (!std::getline(std::cin, command))
                break;

            try
            {
                useItem(std::stoi(command));
            }
            catch (const std::exception&)
            {
                std::cout << "ITEM_RESULT|ERROR|Inventory slot must be a number!" << std::endl;
            }
        }
        else if (command == "REMOVE_ITEM")
        {
            if (!std::getline(std::cin, command))
                break;

            try
            {
                removeItem(std::stoi(command));
            }
            catch (const std::exception&)
            {
                std::cout << "REMOVE_RESULT|ERROR|Inventory slot must be a number!" << std::endl;
            }
        }
        else if (command == "HEAL")
        {
            healCharacter();
        }
        else if (command == "RUN")
        {
            runFromBattle();
        }
        else if (command == "EXIT")
        {
            break;
        }
    }

    return 0;
}
