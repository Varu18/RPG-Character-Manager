#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

std::string playerName;
std::string playerClass;
int playerLevel;
int playerHP;
bool characterCreated = false;

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

void createCharacter(){

    std::cout << "Enter character name: ";
    std::cin >> playerName;

    std::cout << "Enter character class: ";
    std::cin >> playerClass;

    std::cout << "Enter character level: ";
    std::cin >> playerLevel;

    std::cout << "Enter HP: ";
    std::cin >> playerHP;

    std::cout << "Character created!" << std::endl;

    characterCreated = true;
}

void showCharacter(){

    std::cout << "====================" << std::endl;
    std::cout << "Name: " << playerName << std::endl;
    std::cout << "Class: " << playerClass << std::endl;
    std::cout << "Level: " << playerLevel << std::endl;
    std::cout << "HP: " << playerHP << std::endl;
    std::cout << "====================" << std::endl;
}

void fightMonster(){

  int damage = rand() % 71 + 10;

  std::cout << "A wild Goblin appears!" << std::endl;
  std::cout << "The Goblin hits you for " << damage << " damage!" << std::endl;
  
  playerHP -= damage;
  
  if( playerHP <= 0){
    playerHP = 0;
    std::cout << "You are dead!" << std::endl;
  }
  else{
  std::cout << "Current HP: " << playerHP << std::endl;
  }
}

void healCharacter(){
  int oldHP = playerHP;
  std::cout << "Healing.." << std::endl;
  playerHP += 20;

  if( playerHP > 100){
    playerHP = 100;
  }

  int healedAmount = playerHP - oldHP;
  std::cout << "You recovered " << healedAmount << " HP!" << std::endl;
  std::cout << "Current HP: " << playerHP << std::endl;
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
      createCharacter();
    }
  

  }
  else if (option == 2){

    if(!characterCreated){
      std::cout << "No character has been created yet!" << std::endl;
    }
    else{
    showCharacter();
    }
  }
  else if(option == 3){
    
    if(!characterCreated){
      std::cout << "Create a character first!" << std::endl;
    }
    else{

    if(playerHP == 0){
      std::cout << "You are already dead!" << std::endl;
    }
    else{
    fightMonster();
    }
  }
  }
  else if(option==4){
    healCharacter();
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
