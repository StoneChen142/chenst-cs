import pygame
import os
from decimal import *
from random import randint

#Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (51,204,51)
ORANGE = (255,153,0)
PURPLE = (102,0,51)
PINK = (255,0,255)
CYAN = (204,255,255)
DBLUE = (51,51,204)
DGREEN = (0,51,0)
LY = (255,255,204)
NICE = (204,204,255)

#Create Level
#Loading Creation
def CreateLoad(loading_list):

    #Loading
    loading = LoadingClass()
    loading_list.add(loading)

#endprocedure

def CreateCharacters1(player_list, playerAnimation_list, playerAttack_list, playerHealth_list, dummyAnimation_list, levelOne_list, tutorial_list, enemy_list, tutorialEnemy_list, dummy_list, dummyAttack_list, dummyHealth_list):

    player = PlayerClass(50, 700)
    player_list.add(player)

    animationPlayer = PlayerAnimation(player.rect.x, player.rect.y)
    playerAnimation_list.add(animationPlayer)

    playerAttack = AttackClass(120, 130, -1000, 0)
    playerAttack_list.add(playerAttack)

    dummy = BanditClass(295, 250)
    tutorialEnemy_list.add(dummy) #Specify Level
    enemy_list.add(dummy) #Specify Class
    dummy_list.add(dummy) #Specify character

    animationDummy = EnemyAnimation(1, 130, 130, dummy.rect.x, dummy.rect.y)
    tutorial_list.add(animationDummy) #Make it visible
    dummyAnimation_list.add(animationDummy) #Assign animation

    dummyAttack = AttackClass(65, 130, -1000, 0)
    dummyAttack_list.add(dummyAttack)

    dummyHealth = HealthClass(1, 3, 100, 20, 290, 225)
    tutorial_list.add(dummyHealth)
    dummyHealth_list.add(dummyHealth)

    playerHealth = HealthClass(1, 5, 100, 20, 25, 675)
    tutorial_list.add(playerHealth)
    levelOne_list.add(playerHealth)
    playerHealth_list.add(playerHealth)

    levelOne_list.add(animationPlayer) #Make the player's animation visible last to make sure it is on the top
    tutorial_list.add(animationPlayer)

#endprocedure

#Currency Creation
def CreateMoney(tutorial_list, levelOne_list, levelTwo_list, levelThree_list, thousand_list, hundred_list, ten_list, one_list):

    coin = ItemClass(1, 50, 50, 15, 10, 2)
    tutorial_list.add(coin)
    levelOne_list.add(coin)
    levelTwo_list.add(coin)
    levelThree_list.add(coin)

    thousand = WordClass(0, 0, 24, 31, 85, 20)
    thousand_list.add(thousand)
    tutorial_list.add(thousand)
    levelOne_list.add(thousand)
    levelTwo_list.add(thousand)
    levelThree_list.add(thousand)

    hundred = WordClass(0, 0, 24, 31, 115, 20)
    hundred_list.add(hundred)
    tutorial_list.add(hundred)
    levelOne_list.add(hundred)
    levelTwo_list.add(hundred)
    levelThree_list.add(hundred)

    ten = WordClass(0, 0, 24, 31, 145, 20)
    ten_list.add(ten)
    tutorial_list.add(ten)
    levelOne_list.add(ten)
    levelTwo_list.add(ten)
    levelThree_list.add(ten)

    one = WordClass(0, 0, 24, 31, 175, 20)
    one_list.add(one)
    tutorial_list.add(one)
    levelOne_list.add(one)
    levelTwo_list.add(one)
    levelThree_list.add(one)

#endprocedure
    
#Menu Creation
def CreateMenu(menu_list, button_list):

    herotale = Title() #Creates title
    menu_list.add(herotale) #Make it visible

    startButton = Button(1, 309, 93, 0, 595.5, 420) #Start
    button_list.add(startButton)
    menu_list.add(startButton)

    settingsButton = Button(2, 615, 93, 0, 442.5, 560) #Settings
    button_list.add(settingsButton)
    menu_list.add(settingsButton)

    tutorialButton = Button(3, 639, 93, 0, 430.5, 700) #Tutorial
    button_list.add(tutorialButton)
    menu_list.add(tutorialButton)

#endprocedure

#Setting Creation
def CreateSettings(setting_list, button_list, easy_list, hard_list):

    easy = Button(6, 411, 120, 0, 544.5, 250) #Easy Button
    easy_list.add(easy)
    setting_list.add(easy)
    button_list.add(easy)

    hard = Button(7, 441, 120, 0, 529.5, 250) #Hard Button
    hard_list.add(hard)
    button_list.add(hard)

    #Back
    back = Button(5, 106, 31 ,0, 50, 820) #Back Button
    button_list.add(back)
    setting_list.add(back)

    #Text
    chooseDiff = BlockClass(4, 1220, 202, 140, 480)
    setting_list.add(chooseDiff)

#endprocedure

#Save Files Creation
def CreateFile(file_list, button_list, item_list, crown_list):

    #File 1
    fileBox1 = BlockClass(2, 333, 639, 163.5, 130.5) #File box 1
    file_list.add(fileBox1)

    select1 = Button(4, 161, 31, 1, 249.5, 680.5) #Select Button 1
    button_list.add(select1)
    file_list.add(select1)

    coin1 = ItemClass(1, 50, 50, 213.5, 200.5, 3) #Coin etc 1
    file_list.add(coin1)
    item_list.add(coin1)

    heart1 = ItemClass(2, 50, 50, 213.5, 300.5, 3)
    file_list.add(heart1)

    flag1 = ItemClass(3, 50, 50, 213.5, 400.5, 3)
    file_list.add(flag1)

    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 293.5, 210, file_list, 3) #Coin1 number
    WriteWords(0, lines[1], 293.5, 310, file_list, 3) #Live1 number
    WriteWords(0, lines[2], 293.5, 410, file_list, 3) #Level1 number
    
    #File 2
    fileBox2 = BlockClass(2, 333, 639, 583.5, 130.5) #File box 2
    file_list.add(fileBox2)

    select2 = Button(4, 161, 31, 2, 669.5, 680.5) #Select Button 2
    button_list.add(select2)
    file_list.add(select2)

    coin2 = ItemClass(1, 50, 50, 633.5, 200.5, 3) #Coin etc 2
    file_list.add(coin2)
    item_list.add(coin2)

    heart2 = ItemClass(2, 50, 50, 633.5, 300.5, 3)
    file_list.add(heart2)

    flag2 = ItemClass(3, 50, 50, 633.5, 400.5, 3)
    file_list.add(flag2)

    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 2
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 713.5, 210, file_list, 3) #Coin2 number
    WriteWords(0, lines[1], 713.5, 310, file_list, 3) #Live2 number
    WriteWords(0, lines[2], 713.5, 410, file_list, 3) #Level2 number
    
    #File 3
    fileBox3 = BlockClass(2, 333, 639, 1003.5, 130.5) #File box 3
    file_list.add(fileBox3)

    select3 = Button(4, 161, 31 ,3, 1089.5, 680.5) #Select Button 3
    button_list.add(select3)
    file_list.add(select3)

    coin3 = ItemClass(1, 50, 50, 1053.5, 200.5, 3) #Coin etc 3
    file_list.add(coin3)
    item_list.add(coin3)

    heart3 = ItemClass(2, 50, 50, 1053.5, 300.5, 3)
    file_list.add(heart3)

    flag3 = ItemClass(3, 50, 50, 1053.5, 400.5, 3)
    file_list.add(flag3)

    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 3
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 1133.5, 210, file_list, 3) #Coin3 number
    WriteWords(0, lines[1], 1133.5, 310, file_list, 3) #Live3 number
    WriteWords(0, lines[2], 1133.5, 410, file_list, 3) #Level3 number

    #Back
    back = Button(5, 106, 31 ,0, 50, 820) #Back Button
    button_list.add(back)
    file_list.add(back)

    #Crown
    crown = BlockClass(3, 333, 140.5, 163.5, 7.5) #Crown
    file_list.add(crown)
    crown_list.add(crown)

    SetCrown(crown_list)

#endprocedure

#LevelOneCreation
def CreateTutorialPlatform(tutorialBlock_list, tutorial_list, background_list, cloud_list, button_list):

    #Files
    f = open("Game_Files/Tutorial.txt","r+") #Open platforms file
    nodes = f.readlines() #All platforms
    nodesNum = len(nodes) #Number of platforms
    f.close() #Close

    mountain1 = BackgroundClass(1, 0, 5120, 800, 0, 0)
    mountain2 = BackgroundClass(1, 1, 2560, 800, 0, 0)
    cloud1_1 = BackgroundClass(1, 2, 2560, 800, 0, 0)
    cloud2_1 = BackgroundClass(1, 3, 2560, 800, 0, 0)
    cloud1_2 = BackgroundClass(1, 2, 2560, 800, 2560, 0)
    cloud2_2 = BackgroundClass(1, 3, 2560, 800, 2560, 0)

    background_list.add(mountain1, mountain2)
    cloud_list.add(cloud1_1, cloud1_2, cloud2_1, cloud2_2)
    tutorial_list.add(cloud2_2, cloud2_1, cloud1_2, cloud1_1, mountain2, mountain1)

    #Nodes
    for i in range(nodesNum): 
        
        line = nodes[i-2] #Skip the last line because it is empty

        #Type of Block
        typeOfBlock = int(line[0])
        #x position
        if line[1] == "0" and line[2] == "0": #If first two numbers are 0, than the number is the last two numbers (0030)
            xpos = int(str(line[3])+str(line[4]))
        elif line[1] == "0" and line[2] != "0": #If first number is 0, the number is the following three numbers (0300)
            xpos = int(str(line[2])+str(line[3])+str(line[4]))
        elif line[4] == str(0) and line[3] == str(0) and line[2] == str(0) and line[1] == str(0) : #If all numbers are 0, the number is (0)
            xpos = 0
        else: #If else, the number is just a four digit number (4300)
            xpos = int(str(line[1])+str(line[2])+str(line[3])+str(line[4]))
        #endif

        #y position
        if line[5] == str(0): #If first number is 0, the number is the last two numbers
            ypos = int(str(line[6])+str(line[7]))
        else:
            ypos = int(str(line[5])+str(line[6])+str(line[7]))
        #endif

        #width
        if line[8] == str(0): #If first number is 0, the number is the last two numbers
            width = int(str(line[9])+str(line[10]))
        else:
            width = int(str(line[8])+str(line[9])+str(line[10]))
        #endif

        #hieght
        if line[11] == str(0): #If first number is 0, the number is the last two numbers
            height = int(str(line[12])+str(line[13]))
        else:
            height = int(str(line[11])+str(line[12])+str(line[13]))
        #endif
                
        if line[0] == str(1): #If it is a normal block, create a normal platform

            block = BlockClass(typeOfBlock, width, height, xpos, ypos) #Creates a block with given width & height
            tutorialBlock_list.add(block) #Used for later collision
            tutorial_list.add(block) #Make it visible

        #endif

    #endfor

    ground = GroundClass(1, 0, 800) #Creates ground
    tutorial_list.add(ground) #Make it visible

    startBlock = BlockClass(0, 10, 800, -10, 0)
    tutorialBlock_list.add(block)

    moveInstruction = InstructionClass(1, 439, 27, 40, 670)
    jumpInstruction = InstructionClass(2, 210, 25, 810, 670)
    attackInstruction = InstructionClass(3, 289, 25, 175.5, 200)
    rollInstruction = InstructionClass(4, 230, 20, 1105, 330)
    dJumpInstruction = InstructionClass(5, 305, 25, 760, 580)
    blockInstruction = InstructionClass(6, 189, 20, 225.5, 120)
    coinInstruction = InstructionClass(8, 487, 27, 240, 26)
    fakeInstruction = InstructionClass(9, 354, 20, 18, 65)
    tutorial_list.add(moveInstruction, jumpInstruction, attackInstruction, rollInstruction, dJumpInstruction, blockInstruction, coinInstruction, fakeInstruction)

    pauseButton = Button(8, 60, 60, 0, 1430, 10) #Pause
    button_list.add(pauseButton)
    tutorial_list.add(pauseButton)
            
#endprocedure

#LevelOneCreation
def CreateLevelOnePlatform(block1_list, levelOne_list, startEnd_list, background_list, cloud_list):

    #Files
    f = open("Game_Files/Blocks.txt","r+") #Open platforms file
    nodes = f.readlines() #All platforms
    nodesNum = len(nodes) #Number of platforms
    f.close() #Close

    back1 = BackgroundClass(1, 0, 5120, 800, 0, 0)
    back2 = BackgroundClass(1, 1, 2560, 800, 0, 0)
    back3 = BackgroundClass(1, 2, 2560, 800, 0, 0)
    back4 = BackgroundClass(1, 3, 2560, 800, 0, 0)
    back5 = BackgroundClass(1, 2, 2560, 800, 2560, 0)
    back6 = BackgroundClass(1, 3, 2560, 800, 2560, 0)

    background_list.add(back1,back2)
    cloud_list.add(back3, back4, back6, back5)
    levelOne_list.add(back6, back4, back5, back3, back2, back1)

    #Nodes
    for i in range(nodesNum): 
        
        line = nodes[i-2] #Skip the last line because it is empty

        #Type of Block
        typeOfBlock = int(line[0])
        #x position
        if line[1] == "0" and line[2] == "0": #If first two numbers are 0, than the number is the last two numbers (0030)
            xpos = int(str(line[3])+str(line[4]))
        elif line[1] == "0" and line[2] != "0": #If first number is 0, the number is the following three numbers (0300)
            xpos = int(str(line[2])+str(line[3])+str(line[4]))
        elif line[4] == str(0) and line[3] == str(0) and line[2] == str(0) and line[1] == str(0) : #If all numbers are 0, the number is (0)
            xpos = 0
        else: #If else, the number is just a four digit number (4300)
            xpos = int(str(line[1])+str(line[2])+str(line[3])+str(line[4]))
        #endif

        #y position
        if line[5] == str(0): #If first number is 0, the number is the last two numbers
            ypos = int(str(line[6])+str(line[7]))
        else:
            ypos = int(str(line[5])+str(line[6])+str(line[7]))
        #endif

        #width
        if line[8] == str(0): #If first number is 0, the number is the last two numbers
            width = int(str(line[9])+str(line[10]))
        else:
            width = int(str(line[8])+str(line[9])+str(line[10]))
        #endif

        #hieght
        if line[11] == str(0): #If first number is 0, the number is the last two numbers
            height = int(str(line[12])+str(line[13]))
        else:
            height = int(str(line[11])+str(line[12])+str(line[13]))
        #endif
                
        if line[0] == str(1): #If it is a normal block, create a normal platform

            block = BlockClass(typeOfBlock, width, height, xpos, ypos) #Creates a block with given width & height
            block1_list.add(block) #Used for later collision
            levelOne_list.add(block) #Make it visible

        #endif

    #endfor

    ground = GroundClass(1, 0, 800) #Creates ground
    levelOne_list.add(ground) #Make it visible

    startBlock = BlockClass(0, 10, 800, -10, 0)
    block1_list.add(block)

    area = BlockClass(0, 717.5, 800, 0, 0)
    startEnd_list.add(area)
            
#endprocedure

#Menu Class ----------------------------------------------------------------------------------------

#Title
class Title(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([1250, 184])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = 125 #Set pos
        self.rect.y = 100
        self.titleImage = [pygame.transform.scale(pygame.image.load('Game_Images/Text/GameTitle.png'), (1250, 184))]
        self.image = self.titleImage[0]
        
    #endprocedure

#endclass

#Button
class Button(pygame.sprite.Sprite):

    def __init__(self, imageNumber, width, height, number, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect() #Get the shape
        self.imageNum = imageNumber
        self.num = number
        self.rect.x = x
        self.rect.y = y

        self.play = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Play1.png'), (309, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Play2.png'), (309, 93))]
        self.set = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Settings1.png'), (615, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Settings2.png'), (615, 93))]
        self.tutorial = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Tutorial1.png'), (639, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Tutorial2.png'), (639, 93))]
        self.select = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Select1.png'), (161, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Select2.png'), (161, 31))]
        self.back = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Back1.png'), (106, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Back2.png'), (106, 31))]
        self.easy = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Easy1.png'), (411, 120)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Easy2.png'), (411, 120))]
        self.hard = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Hard1.png'), (441, 120)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Hard2.png'), (441, 120))]
        self.pause = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Pause1.png'), (60, 60)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Pause2.png'), (60, 60))]

        if self.imageNum == 1:

            self.image = self.play[0]

        elif self.imageNum == 2:

            self.image = self.set[0]

        elif self.imageNum == 3:

            self.image = self.tutorial[0]

        elif self.imageNum == 4:

            self.image = self.select[0]

        elif self.imageNum == 5:

            self.image = self.back[0]

        elif self.imageNum == 6:

            self.image = self.easy[0]

        elif self.imageNum == 7:

            self.image = self.hard[0]

        elif self.imageNum == 8:

            self.image = self.pause[0]

        #endif
        
    #endprocedure

    def Change(self, pos, level):

        if level == 0 and pos[0] >= 595.5 and pos[1] >= 420 and pos[0] <= 904.5 and pos[1] <= 513 and self.imageNum == 1: #Menu
            
            self.image = self.play[1] #Hover on start button
            
        elif level == 0 and pos[0] >= 442.5 and pos[1] >= 560 and pos[0] <= 1057.5 and pos[1] <= 653 and self.imageNum == 2: #Settings
            
            self.image = self.set[1] #Hover on Settings
            
        elif level == 0 and pos[0] >= 430.5 and pos[1] >= 700 and pos[0] <= 1069.5 and pos[1] <= 793 and self.imageNum == 3: #Tutorial
            
            self.image = self.tutorial[1] #Hover on Tutorial

        elif level == 1 and pos[0] >= 544.5 and pos[1] >= 300 and pos[0] <= 955.5 and pos[1] <= 420 and self.imageNum == 6: #Easy
            
            self.image = self.easy[1] #Hover on Easy

        elif level == 1 and pos[0] >= 529.5 and pos[1] >= 300 and pos[0] <= 970.5 and pos[1] <= 420 and self.imageNum == 7: #Hard
            
            self.image = self.hard[1] #Hover on Hard

        elif level == 1 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5: #Back Button on Settings
            
            self.image = self.back[1] #Hover on back

        elif level == 3 and pos[0] >= 249.5 and pos[1] >= 680.5 and pos[0] <= 410.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 1: #Save Files
            
            self.image = self.select[1] #Hover on select file 1
            
        elif level == 3 and pos[0] >= 669.5 and pos[1] >= 680.5 and pos[0] <= 830.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 2:
            
            self.image = self.select[1] #Hover on select file 2

        elif level == 3 and pos[0] >= 1089.5 and pos[1] >= 680.5 and pos[0] <= 1250.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 3:
            
            self.image = self.select[1] #Hover on select file 3
            
        elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5:
            
            self.image = self.back[1] #Hover on back

        elif level == 2 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70 and self.imageNum == 8:
            
            self.image = self.pause[1] #Hover on back
            
        else:

            if self.imageNum == 1:

                self.image = self.play[0]

            elif self.imageNum == 2:

                self.image = self.set[0]

            elif self.imageNum == 3:

                self.image = self.tutorial[0]

            elif self.imageNum == 4:

                self.image = self.select[0]

            elif self.imageNum == 5:

                self.image = self.back[0]

            elif self.imageNum == 6:

                self.image = self.easy[0]

            elif self.imageNum == 7:

                self.image = self.hard[0]

            elif self.imageNum == 8:

                self.image = self.pause[0]

            #endif

        #endif

    #endprocedure

#endclass

#Save Files Class------------------------------------------------------------------------------------------------------------------
#Item Class
class ItemClass(pygame.sprite.Sprite):

    def __init__(self, typeOfItem, width, height, x, y, level):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x #Set position
        self.rect.y = y

        self.item = typeOfItem

        #Attributes
        self.vertSpeed = 0
        self.horiSpeed = 0
        self.finalX = randint(-30,30)
        if self.finalX > 0:
            self.horiSpeed = 1
        elif self.finalX < 0:
            self.horiSpeed = -1
        #endif
        self.moveX = 0
        self.level = level

        #Coin
        self.dropped = False
        self.getCoin = False

        #Counters
        self.coinCounter = 0

        #Timers
        self.startAnimation = 0
        self.endAnimation = 0
        self.startDisappear = 0
        self.endDisappear = 0

        self.coins = []
        for x in range(7):
            add_str = str(x+1)
            self.coins.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Coins/Coin" + add_str + ".png"), (width, height)))
        #endfor

        self.hearts = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Hearts/Heart.png"), (50, 50))] #Hearts
        self.flags = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Flags/Flag.png"), (50, 50))] #Hearts

        if self.item == 1: #Set image

            self.image = self.coins[0]

        elif self.item == 2:

            self.image = self.hearts[0]

        elif self.item == 3:

            self.image = self.flags[0]

        #endif

    def Change(self):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        if self.endAnimation - self.startAnimation >= 120 and self.item == 1 and not self.getCoin:

            self.startAnimation = self.endAnimation #Reset timer

            self.image = self.coins[self.coinCounter]
            if self.coinCounter == 4:
                self.coinCounter = 0
            else:
                self.coinCounter += 1
            #endif

        elif self.endAnimation - self.startAnimation >= 100 and self.item == 1 and self.getCoin:

            if self.coinCounter < 5:
                self.coinCounter = 5
            #endif
            self.startAnimation = self.endAnimation #Reset timer

            self.image = self.coins[self.coinCounter]
            if self.coinCounter == 6:
                self.coinCounter = 6
            elif self.coinCounter == 5:
                self.coinCounter += 1
            #endif

        #endif

    #endprocedure

    def CoinUpdate(self, player_list, block1_list, tutorialBlock_list, tutorial_list, levelOne_list, coin_list, currency):

        if not self.dropped:

            self.dropped = True
            self.vertSpeed = randint(5,6)

        #endif

        if not self.getCoin:

            for player in player_list: #If player touch coin
                if self.rect.colliderect(player.rect):
                    self.getCoin = True
                #endif
            #endfor

            if abs(self.moveX) < abs(self.finalX) and self.horiSpeed != 0:
                self.rect.x += self.horiSpeed
                self.moveX += self.horiSpeed
            #endif

            if self.level == 2:
                for block in tutorialBlock_list:
                    if self.rect.colliderect(block.rect):
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        elif self.horiSpeed < 0:
                            self.rect.left = block.rect.right
                        #endif
                        self.horiSpeed = 0
                    #endif
                #endfor
            elif self.level == 4:
                for block in block1_list:
                    if self.rect.colliderect(block.rect):
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        elif self.horiSpeed < 0:
                            self.rect.left = block.rect.right
                        #endif
                        self.horiSpeed = 0
                    #endif
                #endfor
            #endif

            if self.vertSpeed == 0: #Keep testing if coin hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 780 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 780 #Stands on the ground
                self.vertSpeed = 0

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #coin move vertically

            if self.level == 4:
                
                coinVertBlock_list = pygame.sprite.spritecollide(self, block1_list, False)#If collide
                for block in coinVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If coin is falling

                        self.rect.bottom = block.rect.top

                    elif self.vertSpeed >= 0: #If coin is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop coin

                #endfor

            elif self.level == 2:

                coinVertBlock_list = pygame.sprite.spritecollide(self, tutorialBlock_list, False)#If collide
                for block in coinVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If coin is falling

                        self.rect.bottom = block.rect.top

                    elif self.vertSpeed >= 0: #If coin is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop coin

                #endfor

            #endif

        elif self.getCoin:

            if self.startDisappear == 0: #If start timer has not started yet

                self.startDisappear = pygame.time.get_ticks() #Record current time

            #endif

            self.endDisappear = pygame.time.get_ticks() #Get current time for end time
            if self.endDisappear - self.startDisappear >= 200:

                if self.level == 2:
                    tutorial_list.remove(self)
                elif self.level == 4:
                    levelOne_list.remove(self)
                #endif
                coin_list.remove(self)
                currency[3] += 1
                if currency[3] == 10:
                    currency[2] += 1
                    currency[3] = 0
                #endif
                if currency[2] == 10:
                    currency[1] += 1
                    currency[2] = 0
                #endif
                if currency[1] == 10:
                    currency[0] += 1
                    currency[1] = 0
                #endif
                if currency[0] == 10:
                    currency[0] = 0
                    currency[1] = 0
                    currency[2] = 0
                    currency[3] = 0
                #endif
            #endif
                
        #endif

    #endprocedure

#endclass

#Word
class WordClass(pygame.sprite.Sprite):

    def __init__(self, typeOfWord, wordNum, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x #Set position
        self.rect.y = y

        self.wordType = typeOfWord
        self.num = wordNum

        #Counters

        #Timers
        self.startAnimation = 0
        self.endAnimation = 0

        self.numbers = [] #Numbers
        for x in range(10):
            add_str = str(x)
            if x < 10:
                self.numbers.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Numbers/" + add_str + ".png"), (width, height)))
            #endif
        #endfor

        if self.wordType == 0:
            
            self.image = self.numbers[int(self.num)]

        #endif

    #endprocedure

    def Update(self, num):

        self.image = self.numbers[num]

    #endprocedure

#endclass

#Write Words
def WriteWords(typeOfWord, line, x, y, file_list, level):

    line = line.rstrip("\n") #Get rid of next line (\n)
    length = len(str(line))
    for i in range(length): #Loop

        if typeOfWord == 0: #If type is number
            width = 24
            height = 31
            xIncrement = 29
            if line[i] != " ":
                word = WordClass(0, line[i], width, height, x, y) #Create word
            #endif
            x += xIncrement #Move Further
            
            if level == 3:
                file_list.add(word) #Add to list
            #endif
        #endif     

    #endfor

#endprocedure

def SetCrown(crown_list):

    maxMoney = 0
    xPos = 0

    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close

    if lines[0][0] == "0" and lines[0][1] == "0" and lines[0][2] == "0":
        currency = int(lines[0][3])
    elif lines[0][0] == "0" and lines[0][1] == "0":
        currency = int(lines[0][2] + lines[0][3])
    elif lines[0][0] == "0":
        currency = int(lines[0][1] + lines[0][2] + lines[0][3])
    else:
        currency = int(lines[0].rstrip("\n"))
    #endif

    if currency >= maxMoney:

        maxMoney = currency
        xPos = 163.5

    #endif

    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 2
    lines = f.readlines() #All data
    f.close() #Close

    if lines[0][0] == "0" and lines[0][1] == "0" and lines[0][2] == "0":
        currency = int(lines[0][3])
    elif lines[0][0] == "0" and lines[0][1] == "0":
        currency = int(lines[0][2] + lines[0][3])
    elif lines[0][0] == "0":
        currency = int(lines[0][1] + lines[0][2] + lines[0][3])
    else:
        currency = int(lines[0].rstrip("\n"))
    #endif

    if currency > maxMoney:

        maxMoney = currency
        xPos = 583.5

    #endif

    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 3
    lines = f.readlines() #All data
    f.close() #Close

    if lines[0][0] == "0" and lines[0][1] == "0" and lines[0][2] == "0":
        currency = int(lines[0][3])
    elif lines[0][0] == "0" and lines[0][1] == "0":
        currency = int(lines[0][2] + lines[0][3])
    elif lines[0][0] == "0":
        currency = int(lines[0][1] + lines[0][2] + lines[0][3])
    else:
        currency = int(lines[0].rstrip("\n"))
    #endif

    if currency > maxMoney:

        maxMoney = currency
        xPos = 1003.5

    #endif

    for crown in crown_list:

        crown.rect.x = xPos

    #endfor

#endprocedure

#Loading Class--------------------------------------------------------------------------------------
#Load Animation
class LoadingClass(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([149, 42])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = 1270
        self.rect.y = 800

        self.loading = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading1.png'), (149, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading2.png'), (157, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading3.png'), (165, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading4.png'), (173, 42))]
        self.image = self.loading[0]

    #endprocedure
    
    def Animation(self, num):

        self.image = self.loading[num]

    #endprocedure

#endclass

#Instruction Class----------------------------------------------------------------------------------
class InstructionClass(pygame.sprite.Sprite): #Instruction is a sprite, because I need to create multiple instructions
    
    def __init__(self, typeNum, width, height, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y

        self.move = [pygame.transform.scale(pygame.image.load('Game_Images/Text/MoveInstruction.png'), (439, 27))]
        self.jump = [pygame.transform.scale(pygame.image.load('Game_Images/Text/JumpInstruction.png'), (210, 25))]
        self.dJump = [pygame.transform.scale(pygame.image.load('Game_Images/Text/DoubleJumpInstruction.png'), (305, 25))]
        self.attack = [pygame.transform.scale(pygame.image.load('Game_Images/Text/AttackInstruction.png'), (289, 25))]
        self.roll = [pygame.transform.scale(pygame.image.load('Game_Images/Text/RollInstruction.png'), (230, 20))]
        self.block = [pygame.transform.scale(pygame.image.load('Game_Images/Text/BlockInstruction.png'), (189, 20))]
        self.minus = [pygame.transform.scale(pygame.image.load('Game_Images/Text/-.png'), (18, 8))]
        self.coin = [pygame.transform.scale(pygame.image.load('Game_Images/Text/CoinsInstruction.png'), (487, 27))]
        self.fake = [pygame.transform.scale(pygame.image.load('Game_Images/Text/FakeCoinInstruction.png'), (327, 20))]

        if typeNum == 1:

            self.image = self.move[0]

        elif typeNum == 2:

            self.image = self.jump[0]

        elif typeNum == 3:

            self.image = self.attack[0]

        elif typeNum == 4:

            self.image = self.roll[0]

        elif typeNum == 5:

            self.image = self.dJump[0]

        elif typeNum == 6:

            self.image = self.block[0]

        elif typeNum == 7:

            self.image = self.minus[0]

        elif typeNum == 8:

            self.image = self.coin[0]

        elif typeNum == 9:

            self.image = self.fake[0]

        #endif

    #endprocedure

#endclass

#Gameplay Class ------------------------------------------------------------------------------------
#Convert Image
def loadify(img):
    
    return pygame.image.load(img).convert_alpha()

#endfunction

#Block
class BlockClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    
    def __init__(self, typeOfBlock, width, height, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y

        self.grassBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Background/GroundBlock.png'), (240, 40))]
        self.saveFileBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/SaveFileBox.png'), (333, 639))]
        self.crown = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Crown.png'), (333, 141))]
        self.chooseDifficulty = [pygame.transform.scale(pygame.image.load('Game_Images/Text/ChooseDifficulty.png'), (1220, 202))]

        if typeOfBlock == 1:

            self.image = self.grassBlock[0]

        elif typeOfBlock == 2:

            self.image = self.saveFileBlock[0]

        elif typeOfBlock == 3:

            self.image = self.crown[0]

        elif typeOfBlock == 4:

            self.image = self.chooseDifficulty[0]

        #endif
        
    #endprocedure

#endclass

#Ground
class GroundClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    
    def __init__(self, num, x, y):
        super().__init__()
        
        self.image = pygame.Surface([1500,100])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y

        self.num = num

        self.ground = []
        for x in range(1):
            add_str = str(x+1)
            self.ground.append(pygame.transform.scale(loadify("Game_Images/Background/Ground" + add_str + ".png"), (1500, 100)))
        #endfor

        if self.num == 1:

            self.image = self.ground[0]

        #endif
        
    #endprocedure

    def ChangeSkin(self, num):

        self.image = self.ground[num] #Changes the texture of itself

    #endprocedure

#endclass

#Background Class
class BackgroundClass(pygame.sprite.Sprite): #Class of the background
 
    def __init__(self, typeBackground, picNum, width, height, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.scalex = x*10 #Scaled up x and y position
        self.scaley = y*10

        self.rect.x = self.scalex//10
        self.rect.y = self.scaley//10

        self.typeBack = typeBackground
        self.num = picNum

        self.mountains = [pygame.transform.scale(loadify("Game_Images/Background/Mountains/Mountain1.png"), (5120, 800))] #Mountains
        for x in range(3):
            add_str = str(x+2)
            if x < 3:
                self.mountains.append(pygame.transform.scale(loadify("Game_Images/Background/Mountains/Mountain" + add_str + ".png"), (2560, 800)))
            #endif
        #endfor

        if self.typeBack == 1:

            self.image = self.mountains[self.num]

        #endif

    #endprocedure

    def BackUpdate(self, move):

        neg = 1
        if move < 0:
            neg = -1
        #endif
            
        if self.num == 0:
            
            self.scalex += neg*abs(move)
            if self.scalex <= -36200 and move < 0:
                self.scalex = -36200
            elif self.scalex >= 0 and move > 0:
                self.scalex = 0
            #endif

        elif self.num == 1:

            self.scalex += neg*(abs(move)-2)
            if self.scalex <= -10600 and move < 0:
                self.scalex = -10600
            elif self.scalex >= 0 and move > 0:
                self.scalex = 0
            #endif

        elif self.num == 2:

            self.scalex += neg*(abs(move)-3)

        elif self.num == 3:

            self.scalex += neg*(abs(move)-4)

        #endif
                
        self.rect.x = self.scalex//10

    #endprocedure

    def CloudUpdate(self):

        if self.num == 2:

            self.scalex -= 10

        elif self.num == 3:

            self.scalex -= 5

        #endif
            
        self.rect.x = self.scalex//10

    #endprocedure

#endclass

#Attack Class
class AttackClass(pygame.sprite.Sprite): #Class of Attack

    def __init__(self, width, height, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    #endprocedure

#endclass

#Health Class
class HealthClass(pygame.sprite.Sprite): #Class of Attack

    def __init__(self, healthType, num, width, height, xPos, yPos):
        
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.rect.x = xPos
        self.rect.y = yPos

        self.enemyHealth = [] #Health
        for x in range(6):
            add_str = str(x)
            self.enemyHealth.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Hearts/Health" + add_str + ".png"), (100, 20)))
        #endfor

        if healthType == 1:

            self.image = self.enemyHealth[num]

        #endif

    #endprocedure

    def Update(self,num):

        self.image = self.enemyHealth[num]

    #endprocedure
        
#endclass

#Player Class
class PlayerClass(pygame.sprite.Sprite): #Class of the player
 
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        #Attributes
        self.hp = 5
        self.reduceHealth = False
        self.speedX = 10
        self.horiSpeed = 0
        self.lastHoriSpeed = 4
        self.doubleJump = False
        self.vertSpeed = -0.4
        self.jumped = False
        self.doubleJumped = False
        self.attacked = False
        self.attackStep = 1
        self.stopSelf = False
        self.resetAttack = False
        self.freeze = False
        self.block = False
        self.blocked = False
        self.unblock = False
        self.roll = False
        self.hurt = False
        self.keepMoving = False
        self.death = False

        #Background
        self.backMove = 0

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startCombo = 0
        self.endCombo = 0
        self.startBlocked = 0
        self.endBlocked = 0
        self.startRoll = 0
        self.endRoll = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRest = 0
        self.endRest = 0

        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter1 = 0
        self.attackCounter2 = 0
        self.attackCounter3 = 0
        self.blockCounter = 0
        self.blockedCounter = 0
        self.rollCounter = 0
        self.deathCounter = 0
        self.hurtCounter = 0
        
    #endprocedure

    def Animation(self, playerAnimation_list):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        for animationPlayer in playerAnimation_list:

            self.endAnimation = pygame.time.get_ticks() #Get current time for end time

            animationPlayer.rect.y = self.rect.y - 38
            animationPlayer.rect.x = self.rect.x - 100

            if self.death == False:
            
                if self.hurt == False and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and self.block == False and self.blocked == False:

                    if self.endAnimation - self.startAnimation >= 160: #If next image
                        
                        self.startAnimation = self.endAnimation #If player is idle
                        animationPlayer.PlayerIdle(self.lastHoriSpeed, self.idleCounter)

                        if self.idleCounter != 7: #If reached the end
                            self.idleCounter += 1
                        else:
                            self.idleCounter = 0
                        #endif

                    #endif

                elif not self.hurt and self.attacked == False and self.horiSpeed != 0 and self.jumped == False and self.roll == False:

                    if self.endAnimation - self.startAnimation >= 80:
                        
                        self.startAnimation = self.endAnimation #If player running
                        animationPlayer.PlayerRun(self.lastHoriSpeed, self.runCounter)

                        if self.runCounter != 9: #If reached the end
                            self.runCounter += 1
                        else:
                            self.runCounter = 0
                        #endif

                    #endif

                elif self.jumped == True and self.vertSpeed >= 0:

                    if self.endAnimation - self.startAnimation >= 200:

                        self.startAnimation = self.endAnimation #If player jumping
                        animationPlayer.PlayerJump(self.lastHoriSpeed, self.jumpCounter)

                        if self.jumpCounter != 2: #If reached the end
                            self.jumpCounter += 1
                        else:
                            self.jumpCounter = 2 #Stay at the last frame
                        #endif

                    #endif

                elif self.jumped == True and self.vertSpeed < 0:

                    if self.endAnimation - self.startAnimation >= 200:

                        self.startAnimation = self.endAnimation #If player falling
                        animationPlayer.PlayerFall(self.lastHoriSpeed, self.fallCounter)

                        if self.fallCounter != 3: #If reached the end
                            self.fallCounter += 1
                        else:
                            self.fallCounter = 3 #Stay at the last frame
                        #endif

                    #endif

                elif self.attacked == True and self.attackStep == 1:

                    if self.endAnimation - self.startAnimation >= 50:

                        self.startAnimation = self.endAnimation 
                        animationPlayer.PlayerAttack1(self.lastHoriSpeed, self.attackCounter1)

                        if self.attackCounter1 != 5: 
                            self.attackCounter1 += 1
                        else:
                            self.attackCounter1 = 5
                        #endif

                    #endif

                elif self.attacked == True and self.attackStep == 2:

                    if self.endAnimation - self.startAnimation >= 50:

                        self.startAnimation = self.endAnimation 
                        animationPlayer.PlayerAttack2(self.lastHoriSpeed, self.attackCounter2)

                        if self.attackCounter2 != 5: 
                            self.attackCounter2 += 1
                        else:
                            self.attackCounter2 = 5
                        #endif

                    #endif

                elif self.attacked == True and self.attackStep == 3:

                    if self.endAnimation - self.startAnimation >= 50:

                        self.startAnimation = self.endAnimation 
                        animationPlayer.PlayerAttack3(self.lastHoriSpeed, self.attackCounter3)

                        if self.attackCounter3 != 7: 
                            self.attackCounter3 += 1
                        else:
                            self.attackCounter3 = 7
                        #endif

                    #endif

                elif self.block == True and self.blocked == False:

                    if self.endAnimation - self.startAnimation >= 80:

                        self.startAnimation = self.endAnimation #If player blocking
                        animationPlayer.PlayerBlock(self.lastHoriSpeed, self.blockCounter)

                        if self.blockCounter != 7: #If reached the end
                            self.blockCounter += 1
                        else:
                            self.blockCounter = 0 #Start over
                        #endif

                    #endif

                elif self.blocked:

                    if self.endAnimation - self.startAnimation >= 80:

                        self.startAnimation = self.endAnimation #If player blocking
                        animationPlayer.PlayerBlocked(self.lastHoriSpeed, self.blockedCounter)

                        if self.blockedCounter != 4: #If reached the end
                            self.blockedCounter += 1
                        else:
                            self.blockedCounter = 4 #Stops
                        #endif

                    #endif

                elif self.roll == True:

                    if self.endAnimation - self.startAnimation >= 50:

                        self.startAnimation = self.endAnimation #If player falling
                        animationPlayer.PlayerRoll(self.lastHoriSpeed, self.rollCounter)

                        if self.rollCounter != 8: #If reached the end
                            self.rollCounter += 1
                        else:
                            self.rollCounter = 8 #Stay at the last frame
                        #endif

                    #endif

                #endif

                elif self.hurt == True:

                    if self.endAnimation - self.startAnimation >= 80:

                        self.startAnimation = self.endAnimation #If player is hurt
                        animationPlayer.PlayerHurt(self.lastHoriSpeed, self.hurtCounter)

                        if self.hurtCounter != 2: #If reached the end
                            self.hurtCounter += 1
                        else:
                            self.hurtCounter = 2 #Stay at the last frame
                        #endif

                    #endif

                #endif

            elif self.death == True:

                if self.endAnimation - self.startAnimation >= 75: #If next image
                        
                    self.startAnimation = self.endAnimation #If player is Dead
                    animationPlayer.PlayerDeath(self.lastHoriSpeed, self.deathCounter)

                    if self.deathCounter != 7: #If reached the end
                        self.deathCounter += 1
                    else:
                        self.deathCounter == 7
                    #endif

                #endif

            #endif

        #endfor

    #endprocedure

    def EnemyAttackDetection(self,dummyAttack_list,level):

        if level == 2:
            playerGetHit_list = pygame.sprite.spritecollide(self, dummyAttack_list, False)#If get hit
            for attack in playerGetHit_list:
                if self.hurt == False and not self.death:
                    if self.block:
                        self.blocked = True
                    elif not self.block and not self.roll:
                        self.hurt = True
                        self.reduceHealth = True
                    #endif
                #endif
            #endfor
        elif level == 4:
            playerGetHit_list = pygame.sprite.spritecollide(self, dummyAttack_list, False)#If get hit
            for attack in playerGetHit_list:
                if self.hurt == False and not self.death:
                    if self.block:
                        self.blocked = True
                    elif not self.block and not self.roll:
                        self.hurt = True
                        self.reduceHealth = True
                    #endif
                #endif
            #endfor
        #endif

    #endprocedure

    def Jump(self):

        if self.freeze == False and self.blocked == False and self.hurt == False and self.attacked == False and self.roll == False and not self.death:

            if self.jumped == False: #If player has not jumped yet

                self.block = False
                self.vertSpeed = 15
                self.jumped = True
                self.doubleJumped = False
                self.jumpCounter = 0
                self.fallCounter = 0

            elif self.jumped == True and self.doubleJumped == False: #If double jump

                self.vertSpeed = 12
                self.doubleJumped = True
                self.jumpCounter = 0
                self.fallCounter = 0

            #endif

        #endif

    #endprocedure

    def MoveVert(self, block_list, tutorialBlock_list, level):

        if self.freeze == False:

            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 703 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 703 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #Player move

            if level == 4:
                
                playerVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
                for block in playerVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If player is falling

                        self.rect.bottom = block.rect.top
                        self.jumped = False

                    elif self.vertSpeed >= 0: #If player is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop player

                #endfor

            elif level == 2:

                playerVertBlock_list = pygame.sprite.spritecollide(self, tutorialBlock_list, False)#If collide
                for block in playerVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If player is falling

                        self.rect.bottom = block.rect.top
                        self.jumped = False

                    elif self.vertSpeed >= 0: #If player is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop player

                #endfor

            #endif

        #endif

    #endprocedure

    def RollTrigger(self):

        if self.attacked == False and self.jumped == False and self.blocked == False and self.hurt == False and not self.death:

            self.block = False
            self.roll = True

        #endif

    #endprocedure

    def BlockTrigger(self,num):

        if self.attacked == False and self.jumped == False and num == 1 and self.hurt == False and not self.death:

            self.horiSpeed = 0
            self.block = True
            self.unblock = False

        elif num == 0:

            self.block = False
            self.unblock = True
            if not self.blocked:
                if not self.keepMoving:
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
            #endif

        #endif

    #endprocedure

    def Blocked(self):

        if self.blocked:

            self.horiSpeed = 0
            
            if self.startBlocked == 0:
                self.startBlocked = pygame.time.get_ticks()
            #endif

            self.endBlocked = pygame.time.get_ticks()
            if self.endBlocked - self.startBlocked > 410:
                self.endBlocked = 0
                self.startBlocked = 0
                self.blocked = False
                self.blockedCounter = 0
                if self.unblock:
                    self.block = False
                    self.unblock = False
                #endif
            #endif

        #endif

    #endprocedure

    def Health(self, health_list):

        if self.reduceHealth == True:

            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                for health in health_list:
                    health.Update(self.hp)
                #endfor
            if self.hp == 0:
                self.death = True
            #endif

        #endif

        for health in health_list:

            if self.hp == 5:
                health.rect.x = self.rect.x - 25
            elif self.hp == 4:
                health.rect.x = self.rect.x - 15
            elif self.hp == 3:
                health.rect.x = self.rect.x - 5
            elif self.hp == 2:
                health.rect.x = self.rect.x + 5
            elif self.hp == 1:
                health.rect.x = self.rect.x + 15
            #endif
            health.rect.y = self.rect.y - 25

        #endfor

    #endprocedure

    def Death(self, health_list):
        
        if self.death == True:

            self.horiSpeed = 0
            
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif

            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                self.hp = 5
                for health in health_list:
                    health.Update(self.hp)
                #endfor
            #endif

        #endif

    #endprocedure

    def Revive(self, health_list):
        
        if self.death == True:

            self.horiSpeed = 0
            
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif

            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                self.hp = 5
                for health in health_list:
                    health.Update(self.hp)
                #endfor
            #endif

        #endif

    #endprocedure

    def Hurt(self):
        
        if self.hurt == True and self.death == False:

            self.horiSpeed = 0
            
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif

            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 250:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
                if not self.keepMoving:
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
            #endif

        #endif

    #endprocedure

    def AttackTrigger(self):

        if self.attacked == False and self.jumped == False and self.roll == False and self.hurt == False and self.blocked == False and self.death == False:

            self.endRest = pygame.time.get_ticks()
            if self.endRest - self.startRest >= 100 and self.resetAttack:
                self.block = False
                self.attacked = True
                self.startRest = 0
                self.endRest = 0
            else:
                self.block = False
                self.attacked = True
                self.endRest = 0
                self.startRest = 0
            #endif

        #endif

    #endprocedure

    def KeepMove(self, speed):

        if speed == 0:
            self.keepMoving = False
        else:
            self.keepMoving = True
        #endif

    #endprocedure

    def AttackChecker(self):

        if self.stopSelf: #If the player should stop

            if not self.keepMoving:
                self.horiSpeed = 0
            else:
                if self.lastHoriSpeed < 0:
                    self.horiSpeed = -self.speedX
                elif self.lastHoriSpeed > 0:
                    self.horiSpeed = self.speedX
                #endif
            #endif
            self.stopSelf = False

        #endif

    #endprocedure

    def Roll(self):

        if self.roll == True:

            if self.startRoll == 0:
                self.startRoll = pygame.time.get_ticks()
            #endif
            self.endRoll = pygame.time.get_ticks()
            if self.lastHoriSpeed < 0:
                self.horiSpeed = -12
            else:
                self.horiSpeed = 12
            #endif
            if self.endRoll - self.startRoll > 450:
                self.endRoll = 0
                self.startRoll = 0
                self.roll = False
                if not self.keepMoving: #If keep going
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
                self.rollCounter = 0
            #endif

        #endif

    #endprocedure

    def Attack(self, playerAttack_list):

        if self.attacked == False:
            
            self.endCombo = pygame.time.get_ticks()
            if self.startCombo == 0:
                self.startCombo = pygame.time.get_ticks()
            #endif
            if self.endCombo - self.startCombo >= 500:
                self.attackStep = 1
                self.startCombo = 0
                self.endCombo = 0
            #endif
        
        elif self.attacked == True and self.freeze == False:

            self.horiSpeed = 0
            self.endCombo = 0
            self.startCombo = 0
            if self.attackStep == 1: #Attack 1
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                for attack in playerAttack_list:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x + 25
                        attack.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x - 95
                        attack.rect.y = self.rect.y - 30
                    elif self.hurt:
                        attack.rect.x = -1000
                    #endif
                #endfor
                if self.endAttack - self.startAttack > 300:
                    for attack in playerAttack_list:
                        attack.rect.x = -1000
                    #endfor
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -7
                    else:
                        self.horiSpeed = 7
                    #endif
                    self.stopSelf = True
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackStep = 2
                    self.attacked = False
                    self.attackCounter1 = 0
                #endif
            elif self.attackStep == 2: #Attack 2
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                for attack in playerAttack_list:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x + 25
                        attack.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x - 95
                        attack.rect.y = self.rect.y - 30
                    elif self.hurt:
                        attack.rect.x = -1000
                    #endif
                #endfor
                if self.endAttack - self.startAttack > 300:
                    for attack in playerAttack_list:
                        attack.rect.x = -1000
                    #endfor
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -7
                    else:
                        self.horiSpeed = 7
                    #endif
                    self.stopSelf = True
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackStep = 3
                    self.attacked = False
                    self.attackCounter2 = 0
                #endif
            elif self.attackStep == 3: #Attack 3
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                for attack in playerAttack_list:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x + 25
                        attack.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x - 95
                        attack.rect.y = self.rect.y - 30
                    elif self.hurt:
                        attack.rect.x = -1000
                    #endif
                #endfor
                if self.endAttack - self.startAttack > 400:
                    for attack in playerAttack_list:
                        attack.rect.x = -1000
                    #endfor
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -9
                    else:
                        self.horiSpeed = 9
                    #endif
                    self.stopSelf = True
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackStep = 1
                    self.attacked = False
                    self.attackCounter3 = 0
                    self.startRest = pygame.time.get_ticks()
                    self.resetAttack = True
                #endif
            #endif

        #endif

    #endprocedure     

    def ChangeSpeed(self,num):

        if self.freeze == False and self.attacked == False and self.roll == False and self.hurt == False and self.blocked == False and not self.death:

            if num == 0:

                self.horiSpeed = -self.speedX
                self.block = False
                self.lastHoriSpeed = self.horiSpeed

            elif num == 1:

                self.horiSpeed = self.speedX
                self.block = False
                self.lastHoriSpeed = self.horiSpeed

            elif num == 2:

                self.horiSpeed = 0

            #endif

        #endif

    #endprocedure

    def MoveHori(self, centered, block_list, tutorialBlock_list, startEnd_list, player_list, level, background_list):

        if self.freeze == False:
            
            if centered == False: #If player is not required to be in the center, itself
    #will move instead of the blocks
                self.rect.x += self.horiSpeed

                if level == 2:
                    
                    for block in tutorialBlock_list:
                                
                        if self.rect.colliderect(block.rect): #If player hit block
                            if self.horiSpeed > 0:
                                self.rect.right = block.rect.left
                            else:
                                self.rect.left = block.rect.right
                            #endif
                        #endif

                    #endfor
                                
                elif level == 4:
                    
                    for block in block_list:
                                
                        if self.rect.colliderect(block.rect): #If player hit block
                            if self.horiSpeed > 0:
                                self.rect.right = block.rect.left
                            else:
                                self.rect.left = block.rect.right
                            #endif
                        #endif

                    #endfor
                                
                #endif

                if self.rect.x <= 0: #If player reach the end of screen

                    self.rect.x = 0

                elif self.rect.x >= 1435:

                    self.rect.x = 1435

                #endif

            else: #If player placed in the center, the blocks move instead of the player

                self.rect.x = 717.5

                if level == 4:
                    
                    for block in block_list:

                        block.rect.x -= self.horiSpeed
                        
                        for back in background_list:

                            if self.horiSpeed != 0:

                                if self.horiSpeed < 0:
                                    move = 5
                                else:
                                    move = -5
                                #endif

                                back.BackUpdate(move)

                            #endif

                        #endfor

                        for area in startEnd_list:

                            area.rect.x -= self.horiSpeed

                        #endfor
                        
                        playerBlock_list = pygame.sprite.spritecollide(block, player_list, False)
                        for player in playerBlock_list:

                            for block in block_list:
                                
                                block.rect.x += self.horiSpeed
                                for back in background_list:

                                    if self.horiSpeed != 0:
                                        
                                        if self.horiSpeed < 0:
                                            move = -5
                                        else:
                                            move = 5
                                        #endif

                                    #endif

                                    back.BackUpdate(move)

                                #endfor

                                for area in startEnd_list:

                                    area.rect.x += self.horiSpeed

                                #endfor

                            #endfor

                        #endfor

                    #endfor

                elif level == 2:

                    for block in tutorialBlock_list:

                        block.rect.x -= self.horiSpeed
                        
                        for back in background_list:

                            if self.horiSpeed != 0:

                                if self.horiSpeed < 0:
                                    move = 5
                                else:
                                    move = -5
                                #endif

                                back.BackUpdate(move)

                            #endif

                        #endfor

                        for area in startEnd_list:

                            area.rect.x -= self.horiSpeed

                        #endfor
                        
                        playerBlock_list = pygame.sprite.spritecollide(block, player_list, False)
                        for player in playerBlock_list:

                            for block in tutorialBlock_list:
                                
                                block.rect.x += self.horiSpeed
                                for back in background_list:

                                    if self.horiSpeed != 0:
                                        
                                        if self.horiSpeed < 0:
                                            move = -5
                                        else:
                                            move = 5
                                        #endif

                                    #endif

                                    back.BackUpdate(move)

                                #endfor

                                for area in startEnd_list:

                                    area.rect.x += self.horiSpeed

                                #endfor

                            #endfor

                        #endfor

                    #endfor

                #endif

            #endif

        #endif

    #endprocedure

#endclass

#Player Animation Class
class PlayerAnimation(pygame.sprite.Sprite): #Class of player's animation
 
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()

        self.rect.x = x #Set pos
        self.rect.y = y

        #Animation
        self.playerIdle = [] #Idle
        for x in range(8):
            add_str = str(x+1)
            self.playerIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroIdle" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerRun = [] #Run
        for x in range(10):
            add_str = str(x+1)
            self.playerRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroRun" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerJump = [] #Jump
        for x in range(3):
            add_str = str(x+1)
            self.playerJump.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroJump" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerFall = [] #Fall
        for x in range(4):
            add_str = str(x+1)
            self.playerFall.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroFall" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack1 = [] #Attack 1
        for x in range(6):
            add_str = str(x+1)
            self.playerAttack1.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack1-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack2 = [] #Attack 2
        for x in range(6):
            add_str = str(x+1)
            self.playerAttack2.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack2-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack3 = [] #Attack 3
        for x in range(8):
            add_str = str(x+1)
            self.playerAttack3.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack3-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerBlock = [] #Block
        for x in range(8):
            add_str = str(x+1)
            self.playerBlock.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroBlock" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerBlocked = [] #Blocked
        for x in range(5):
            add_str = str(x+1)
            self.playerBlocked.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroBlocked" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerRoll = [] #Roll
        for x in range(9):
            add_str = str(x+1)
            self.playerRoll.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroRoll" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerHurt = [] #Hurt
        for x in range(3):
            add_str = str(x+1)
            self.playerHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroHurt" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerDeath = [] #Death
        for x in range(8):
            add_str = str(x+1)
            self.playerDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroDeath" + add_str + ".png"), (250, 138)))
        #endfor
        self.image = self.playerIdle[0]
            
        self.image = self.playerIdle[0]
        
    #endprocedure

    def PlayerIdle(self, speed, i): #When player not moving

        if speed > 0:
            self.image = self.playerIdle[i] #Right
        else:
            self.image = pygame.transform.flip(self.playerIdle[i],1,0) #Left
        #endif

    #endprocedure

    def PlayerRun(self, speed, i):

        if speed > 0:
            self.image = self.playerRun[i]
        else:
            self.image = pygame.transform.flip(self.playerRun[i],1,0)
        #endif

    #endprocedure

    def PlayerJump(self, speed, i):

        if speed > 0:
            self.image = self.playerJump[i]
        else:
            self.image = pygame.transform.flip(self.playerJump[i],1,0)
        #endif

    #endprocedure

    def PlayerFall(self, speed, i):

        if speed > 0:
            self.image = self.playerFall[i]
        else:
            self.image = pygame.transform.flip(self.playerFall[i],1,0)
        #endif

    #endprocedure

    def PlayerAttack1(self, speed, i):

        if speed > 0:
            self.image = self.playerAttack1[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack1[i],1,0)
        #endif

    #endprocedure

    def PlayerAttack2(self, speed, i):

        if speed > 0:
            self.image = self.playerAttack2[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack2[i],1,0)
        #endif

    #endprocedure

    def PlayerAttack3(self, speed, i):

        if speed > 0:
            self.image = self.playerAttack3[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack3[i],1,0)
        #endif

    #endprocedure

    def PlayerBlock(self, speed, i):

        if speed > 0:
            self.image = self.playerBlock[i]
        else:
            self.image = pygame.transform.flip(self.playerBlock[i],1,0)
        #endif

    #endprocedure

    def PlayerBlocked(self, speed, i):

        if speed > 0:
            self.image = self.playerBlocked[i]
        else:
            self.image = pygame.transform.flip(self.playerBlocked[i],1,0)
        #endif

    #endprocedure

    def PlayerRoll(self, speed, i):

        if speed > 0:
            self.image = self.playerRoll[i]
        else:
            self.image = pygame.transform.flip(self.playerRoll[i],1,0)
        #endif

    #endprocedure

    def PlayerHurt(self, speed, i):

        if speed > 0:
            self.image = self.playerHurt[i]
        else:
            self.image = pygame.transform.flip(self.playerHurt[i],1,0)
        #endif

    #endprocedure

    def PlayerDeath(self, speed, i):

        if speed > 0:
            self.image = self.playerDeath[i]
        else:
            self.image = pygame.transform.flip(self.playerDeath[i],1,0)
        #endif

    #endprocedure

#endclass

#Enemy Class----------------------------------------------------------------
#Bandit Class
class BanditClass(pygame.sprite.Sprite): #Class of the player
 
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        #Attributes
        self.hp = 3
        self.horiSpeed = 0
        self.lastHoriSpeed = 4
        self.vertSpeed = -0.4
        self.jumped = False
        self.attacked = False
        self.attackPhase = 1
        self.stopSelf = False 
        self.freeze = False
        self.hurt = False
        self.death = False
        self.adle = False
        self.reduceHealth = False
        self.dropCoin = False

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0

        #Counter
        self.idleCounter = 0
        self.adleCounter = 0
        self.runCounter = 0
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        
    #endprocedure

    def Animation(self, animation_list):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        for animation in animation_list:

            self.endAnimation = pygame.time.get_ticks() #Get current time for end time

            animation.rect.y = self.rect.y - 30
            animation.rect.x = self.rect.x - 40

            if self.death == False:
            
                if not self.hurt and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and not self.adle:

                    if self.endAnimation - self.startAnimation >= 160: #If next image
                        
                        self.startAnimation = self.endAnimation #If player is idle
                        animation.Idle(-self.lastHoriSpeed, self.idleCounter)

                        if self.idleCounter != 3: #If reached the end
                            self.idleCounter += 1
                        else:
                            self.idleCounter = 0
                        #endif

                    #endif

                elif not self.hurt and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and self.adle:

                    if self.endAnimation - self.startAnimation >= 160: #If next image
                        
                        self.startAnimation = self.endAnimation #If player is idle
                        animation.Adle(-self.lastHoriSpeed, self.adleCounter)

                        if self.adleCounter != 3: #If reached the end
                            self.adleCounter += 1
                        else:
                            self.adleCounter = 0
                        #endif

                    #endif

                elif not self.hurt and self.attacked == False and self.horiSpeed != 0 and self.jumped == False:

                    if self.endAnimation - self.startAnimation >= 80:
                        
                        self.startAnimation = self.endAnimation #If player running
                        animation.Run(-self.lastHoriSpeed, self.runCounter)

                        if self.runCounter != 7: #If reached the end
                            self.runCounter += 1
                        else:
                            self.runCounter = 0
                        #endif

                    #endif

                elif self.jumped == True:

                    if self.endAnimation - self.startAnimation >= 200:

                        self.startAnimation = self.endAnimation #If player jumping
                        animation.Jump(-self.lastHoriSpeed, self.jumpCounter)

                        self.jumpCounter = 0

                    #endif

                
                elif self.hurt == True:

                    if self.endAnimation - self.startAnimation >= 100:

                        self.startAnimation = self.endAnimation #If player is hurt
                        animation.Hurt(-self.lastHoriSpeed, self.hurtCounter)

                        if self.hurtCounter != 2: #If reached the end
                            self.hurtCounter += 1
                        else:
                            self.hurtCounter = 2
                        #endif

                    #endif
                        
                elif self.attacked == True:

                    if self.endAnimation - self.startAnimation >= 50:

                        self.startAnimation = self.endAnimation 
                        animation.Attack(-self.lastHoriSpeed, self.attackCounter)

                        if self.attackPhase == 1 and self.attackCounter != 3: 
                            self.attackCounter += 1
                        elif self.attackPhase == 3 and self.attackCounter != 7:
                            self.attackCounter += 1
                        #endif

                    #endif

                #endif

            elif self.death:

                if self.endAnimation - self.startAnimation >= 50:

                    self.startAnimation = self.endAnimation 
                    animation.Death(-self.lastHoriSpeed, self.deathCounter)

                    self.deathCounter = 0

                #endif
                        
            #endif

        #endfor

    #endprocedure

    def AttackStance(self,num):

        if num == 1:
            self.adle = True
        else:
            self.adle = False

        #endif

    #endprocedure

    def Health(self, health_list, coin_list, tutorial_list, levelOne_list, level):

        if self.reduceHealth == True:

            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                for health in health_list:
                    health.Update(self.hp)
                #endfor
            if self.hp == 0:
                self.death = True
                if not self.dropCoin:
                    self.dropCoin = False
                    for i in range(2):
                        if level == 2:
                            coin = ItemClass(1, 20, 20, self.rect.x + 10, self.rect.y + 70, 2)
                            tutorial_list.add(coin)
                        elif level == 4:
                            coin = ItemClass(1, 20, 20, self.rect.x + 10, self.rect.y + 70, 4)
                            levelOne_list.add(coin)
                        #endif
                        coin_list.add(coin)
                    #endfor
                #endif
            #endif

        #endif

        for health in health_list:

            if self.hp == 3:
                health.rect.x = self.rect.x - 5
            elif self.hp == 2:
                health.rect.x = self.rect.x + 5
            elif self.hp == 1:
                health.rect.x = self.rect.x + 15
            #endif
            health.rect.y = self.rect.y - 25

        #endfor

    #endprocedure

    def EnemyAttackDetection(self,playerAttack_list,level):

        if level == 2:
            enemyGetHit_list = pygame.sprite.spritecollide(self, playerAttack_list, False)#If get hit
            for attack in enemyGetHit_list:
                if self.hurt == False and not self.death:
                    self.hurt = True
                    self.reduceHealth = True
                #endif
            #endfor
        elif level == 4:
            enemyGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
            for attack in enemyGetHit_list:
                if self.hurt == False and not self.death:
                    self.hurt = True
                    self.reduceHealth = True
                #endif
            #endfor
        #endif

    #endprocedure

    def Death(self,health_list):
        
        if self.death == True:

            self.horiSpeed = 0
            
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif

            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                self.hp = 3
                self.dropCoin = False
                for health in health_list:
                    health.Update(self.hp)
                #endfor
            #endif

        #endif

    #endprocedure

    def Revive(self,health_list):
        
        if self.death == True:

            self.horiSpeed = 0
            
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif

            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                self.hp = 3
                for health in health_list:
                    health.Update(self.hp)
                #endfor
            #endif

        #endif

    #endprocedure

    def Hurt(self):
        
        if self.hurt == True:

            self.horiSpeed = 0
            
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif

            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 400:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
            #endif

        #endif

    #endprocedure

    def Jump(self):

        if self.freeze == False and self.attacked == False and self.death == False:

            if self.jumped == False: #If player has not jumped yet

                self.vertSpeed = 19
                self.jumped = True
                self.jumpCounter = 0
                self.fallCounter = 0

            #endif

        #endif

    #endprocedure

    def MoveVert(self, block_list, tutorialBlock_list, level):

        if self.freeze == False:

            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 703 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 703 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #Player move

            if level == 4:
                
                selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
                for block in selfVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If player is falling

                        self.rect.bottom = block.rect.top
                        self.jumped = False

                    elif self.vertSpeed >= 0: #If player is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop player

                #endfor

            elif level == 2:

                selfVertBlock_list = pygame.sprite.spritecollide(self, tutorialBlock_list, False)#If collide
                for block in selfVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If player is falling

                        self.rect.bottom = block.rect.top
                        self.jumped = False

                    elif self.vertSpeed >= 0: #If player is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop player

                #endfor

            #endif

        #endif

    #endprocedure

    def AttackTrigger(self):

        if self.attacked == False and self.jumped == False and self.death == False:

            self.attacked = True

        #endif

    #endprocedure

    def AttackChecker(self):

        if self.stopSelf: #If the enemy should stop

            self.stopSelf = False
            self.horiSpeed = 0

        #endif

    #endprocedure

    def Attack(self, attack_list):
        
        if self.attacked == True and self.freeze == False:

            self.horiSpeed = 0
            
            if self.startAttack == 0:
                self.startAttack = pygame.time.get_ticks()
            #endif

            if self.attackPhase == 1:
                self.endAttack = pygame.time.get_ticks()
                if self.endAttack - self.startAttack > 200:
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackPhase = 2
                #endif
            elif self.attackPhase == 2:
                self.endAttack = pygame.time.get_ticks()
                if self.endAttack - self.startAttack > 100:
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackPhase = 3
                #endif
            elif self.attackPhase == 3:
                self.endAttack = pygame.time.get_ticks()
                for attack in attack_list:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x + 25
                        attack.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        attack.rect.x = self.rect.x - 40
                        attack.rect.y = self.rect.y - 30
                    elif self.hurt:
                        attack.rect.x = -1000
                    #endif
                #endfor
                if self.endAttack - self.startAttack > 200:
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackPhase = 4
                    for attack in attack_list:
                        attack.rect.x = -1000
                    #endfor
                #endif
            elif self.attackPhase == 4:
                self.endAttack = pygame.time.get_ticks()
                if self.endAttack - self.startAttack > 150:
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attacked = False
                    self.attackPhase = 1
                    self.attackCounter = 0
                #endif
            #endif

        #endif

    #endprocedure     

    def ChangeSpeed(self,num):

        if self.freeze == False and self.attacked == False:

            if num == 0:

                self.horiSpeed = -11
                self.lastHoriSpeed = self.horiSpeed

            elif num == 1:

                self.horiSpeed = 11
                self.lastHoriSpeed = self.horiSpeed

            elif num == 2:

                self.horiSpeed = 0

            #endif

        #endif

    #endprocedure

    def MoveHori(self, block_list, tutorialBlock_list, level):

        if self.freeze == False:
            
            self.rect.x += self.horiSpeed

            if level == 2:
                
                for block in tutorialBlock_list:
                            
                    if self.rect.colliderect(block.rect): #If player hit block
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        else:
                            self.rect.left = block.rect.right
                        #endif
                    #endif

                #endfor
                            
            elif level == 4:
                
                for block in block_list:
                            
                    if self.rect.colliderect(block.rect): #If player hit block
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        else:
                            self.rect.left = block.rect.right
                        #endif
                    #endif

                #endfor
                            
            #endif

            if self.rect.x <= 0: #If player reach the end of screen

                self.rect.x = 0

            elif self.rect.x >= 1435:

                self.rect.x = 1435

            #endif

        #endif

    #endprocedure

#endclass

#Enemy Animation Class
class EnemyAnimation(pygame.sprite.Sprite): #Class of player's animation
 
    def __init__(self, enemyType, width, height, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.rect.x = x #Set pos
        self.rect.y = y

        self.enemy = enemyType

        #Animation
        #Light Bandit
        self.banditIdle1 = [] #Idle 
        for x in range(4):
            add_str = str(x+1)
            self.banditIdle1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditIdle" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAdle1 = [] #Attack Idle 
        for x in range(4):
            add_str = str(x+1)
            self.banditAdle1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditAdle" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditRun1 = [] #Run
        for x in range(8):
            add_str = str(x+1)
            self.banditRun1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditRun" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditJump1 = [] #Jump
        for x in range(1):
            add_str = str(x+1)
            self.banditJump1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditJump" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAttack1 = [] #Attack 1
        for x in range(8):
            add_str = str(x+1)
            self.banditAttack1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditAttack" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditHurt1 = [] #Hurt 1
        for x in range(3):
            add_str = str(x+1)
            self.banditHurt1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditHurt" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditDeath1 = [] #Death 1
        for x in range(1):
            self.banditDeath1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditDeath.png"), (130, 130)))
        #endfor
        self.banditRecover1 = [] #Recover 1
        for x in range(8):
            add_str = str(x+1)
            self.banditRecover1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditRecover" + add_str + ".png"), (130, 130)))
        #endfor

        if self.enemy == 1: #Set
            self.image = pygame.transform.flip(self.banditIdle1[0],1,0)
        #endif
        
    #endprocedure

    def Idle(self, speed, i): #When enemy not moving

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditIdle1[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditIdle1[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Adle(self, speed, i): #When enemy not moving 2

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditAdle1[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditAdle1[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Run(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditRun1[i]
            else:
                self.image = pygame.transform.flip(self.banditRun1[i],1,0)
            #endif
        #endif

    #endprocedure

    def Jump(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditJump1[i]
            else:
                self.image = pygame.transform.flip(self.banditJump1[i],1,0)
            #endif
        #endif

    #endprocedure

    def Fall(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditJump[i]
            else:
                self.image = pygame.transform.flip(self.banditJump[i],1,0)
            #endif
        #endif

    #endprocedure

    def Attack(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditAttack1[i]
            else:
                self.image = pygame.transform.flip(self.banditAttack1[i],1,0)
            #endif
        #endif

    #endprocedure

    def Hurt(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditHurt1[i]
            else:
                self.image = pygame.transform.flip(self.banditHurt1[i],1,0)
            #endif
        #endif

    #endprocedure

    def Recover(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditRecover1[i]
            else:
                self.image = pygame.transform.flip(self.banditRecover1[i],1,0)
            #endif
        #endif

    #endprocedure

    def Death(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditDeath1[i]
            else:
                self.image = pygame.transform.flip(self.banditDeath1[i],1,0)
            #endif
        #endif

    #endprocedure

#endclass
        
#Gameplay
def Game():

    game_over = False #Not finish
    
    clock = pygame.time.Clock()

    #Variables
    currency = [0,0,0,0] #Money
    live = 0 #Player's live
    gameLevel = 1 #Game Level

    #Setting Variables
    difficulty = 0

    #Game Level Variable
    currentSpeed = 0 #Used to determine animation direction
    horiSpeed = 0#Used to determine background move
    centered = False
    level = -1 #Determines level
    tutorialReset = True

    #Tutorial Level Variable
    dummyStartAttack = 0
    dummyEndAttack = 0

    #Level Load Variables
    gameInitiated = False #If game has been intiated
    levelCreated = False #If level has been created
    loadNum = 0 #Animation Count
    startLoadTime = 0 #Timer
    endLoadTime = 0
    currentFile = 0 #The player's file
    fileLoaded = False #If file has been loaded
    crownChecked = False
    levelToGo = 0
    tutorialLevel = False

    block1_list = pygame.sprite.Group() #Blocks list 1

    tutorialBlock_list = pygame.sprite.Group() #Block tutorial list

    player_list = pygame.sprite.Group() #Player's list

    playerHealth_list = pygame.sprite.Group() #Player health's list

    enemy_list = pygame.sprite.Group() #Enemy's list

    dummy_list = pygame.sprite.Group() #Dummy

    tutorialEnemy_list = pygame.sprite.Group() #Enemy's tutorial list

    dummyAttack_list = pygame.sprite.Group() #Dummy's attack

    dummyHealth_list = pygame.sprite.Group() #Dummy's health

    startEnd_list = pygame.sprite.Group() #The area determines the start and end of a level

    levelOne_list = pygame.sprite.Group() #All visible object lists in level one

    levelTwo_list = pygame.sprite.Group() #All visible object lists in level two

    levelThree_list = pygame.sprite.Group() #All visible object lists in level three

    menu_list = pygame.sprite.Group() #All visible objects in menu

    file_list = pygame.sprite.Group() #All visible objects in file

    playerAnimation_list = pygame.sprite.Group() #Player's animation

    playerAttack_list = pygame.sprite.Group() #Player's attack

    dummyAnimation_list = pygame.sprite.Group() #Dummy's animation

    button_list = pygame.sprite.Group() #Buttons

    item_list = pygame.sprite.Group() #Group of items

    crown_list = pygame.sprite.Group() #Crown

    loading_list = pygame.sprite.Group() #Loading screen

    setting_list = pygame.sprite.Group() #Setting screen

    easy_list = pygame.sprite.Group() #Easy

    hard_list = pygame.sprite.Group() #Hard

    background_list = pygame.sprite.Group() #Backgrounds

    cloud_list = pygame.sprite.Group() #Clouds

    tutorial_list = pygame.sprite.Group() #Tutorial

    coin_list = pygame.sprite.Group() #Coins

    thousand_list = pygame.sprite.Group()

    hundred_list = pygame.sprite.Group()

    ten_list = pygame.sprite.Group()

    one_list = pygame.sprite.Group()

    CreateLoad(loading_list)

    while not game_over:
        
    # -- User input and controls
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()#Track Mouse' Position
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN: #Mouse Click
                if level == 0 and pos[0] >= 595.5 and pos[1] >= 420 and pos[0] <= 904.5 and pos[1] <= 513: #Select save files
                    level = 3 #Start game
                    tutorialLevel = False
                elif level == 0 and pos[0] >= 442.5 and pos[1] >= 560 and pos[0] <= 1057.5 and pos[1] <= 653: #Select Settings
                    level = 1 #Settings
                elif level == 0 and pos[0] >= 430.5 and pos[1] >= 700 and pos[0] <= 1069.5 and pos[1] <= 793: #Select tutorial
                    levelToGo = 2
                    level = -1 #Tutorial
                    tutorialLevel = True
                    for dummy in dummy_list:
                        dummy.AttackStance(1)
                    #endfor
                elif level == 1 and pos[0] >= 529.5 and pos[1] >= 300 and pos[0] <= 970.5 and pos[1] <= 420: #Select Difficulty
                    if difficulty == 0:
                        difficulty = 1
                        for easy in easy_list:
                            setting_list.remove(easy)
                        #endfor
                        for hard in hard_list:
                            setting_list.add(hard)
                        #endfor
                    else:
                        difficulty = 0
                        for easy in easy_list:
                            setting_list.add(easy)
                        #endfor
                        for hard in hard_list:
                            setting_list.remove(hard)
                        #endfor
                    #endif
                elif level == 3 and pos[0] >= 249.5 and pos[1] >= 680.5 and pos[0] <= 410.5 and pos[1] <= 711.5: #Select file 1
                    level = -1
                    levelToGo = 4
                    currentFile = 1
                elif level == 3 and pos[0] >= 669.5 and pos[1] >= 680.5 and pos[0] <= 830.5 and pos[1] <= 711.5: #Select file 2
                    level = -1
                    levelToGo = 4
                    currentFile = 2
                elif level == 3 and pos[0] >= 1089.5 and pos[1] >= 680.5 and pos[0] <= 1250.5 and pos[1] <= 711.5: #Select file 3
                    level = -1
                    levelToGo = 4
                    currentFile = 3
                elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851: #Go back to menu
                    level = 0
                elif level == 1 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851: #Go back to menu
                    level = 0
                elif level == 2 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70: #Go back to menu
                    levelToGo = 0
                    level = -1        
                #endif
            elif level >= 2 and event.type == pygame.KEYDOWN: #Press Key Down
                if event.key == pygame.K_SPACE:
                    player.AttackTrigger()
                if event.key == pygame.K_w:
                    player.Jump()
                if event.key == pygame.K_a:
                    player.ChangeSpeed(0)
                    player.KeepMove(1)
                    currentSpeed = -1
                    horiSpeed = -1
                if event.key == pygame.K_d:
                    player.ChangeSpeed(1)
                    player.KeepMove(1)
                    currentSpeed = 1
                    horiSpeed = 1
                if event.key == pygame.K_s:
                    player.BlockTrigger(1)
                if event.key == pygame.K_LSHIFT:
                    player.RollTrigger()
                #endif
            elif level >= 2 and event.type == pygame.KEYUP: #Release Key
                if event.key == pygame.K_a and currentSpeed < 0:
                    player.ChangeSpeed(2)
                    player.KeepMove(0)
                    horiSpeed = 0
                if event.key == pygame.K_d and currentSpeed > 0:
                    player.ChangeSpeed(2)
                    player.KeepMove(0)
                    horiSpeed = 0
                if event.key == pygame.K_s:
                    player.BlockTrigger(0)
                #endif
            #endif
        #endfor

        if level == 0:

            screen.fill(BLACK)

            for button in button_list:
                
                button.Change(pos, level)

            #endfor

            menu_list.draw(screen) #Display all visible objects

        elif level == -1:

            screen.fill(BLACK)

            if startLoadTime == 0: #If start timer has not started yet

                startLoadTime = pygame.time.get_ticks() #Record current time

            #endif

            if gameInitiated == False:

                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 700:

                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:

                        load.Animation(loadNum) #Animation
                        loadNum += 1

                        if loadNum == 4: #If animation finished

                            gameInitiated = True #Reset Loading
                            loadNum = 0
                            load.Animation(loadNum)
                            startLoadTime = 0
                            endLoadTime = 0
                            fileLoaded = False
                            level = 0 #Go to menu

                        #endif

                    #endfor
                            
                #endif
                
                loading_list.draw(screen) #Display objects

                if levelCreated == False:

                    levelCreated = True
                    
                    CreateFile(file_list, button_list, item_list, crown_list)
                    CreateMenu(menu_list, button_list)
                    CreateSettings(setting_list, button_list, easy_list, hard_list)
                    CreateLevelOnePlatform(block1_list, levelOne_list, startEnd_list, background_list, cloud_list) #Call create block function
                    CreateTutorialPlatform(tutorialBlock_list, tutorial_list, background_list, cloud_list, button_list)
                    CreateCharacters1(player_list, playerAnimation_list, playerAttack_list, playerHealth_list, dummyAnimation_list, levelOne_list, tutorial_list, enemy_list, tutorialEnemy_list, dummy_list, dummyAttack_list, dummyHealth_list)
                    CreateMoney(tutorial_list, levelOne_list, levelTwo_list, levelThree_list, thousand_list, hundred_list, ten_list, one_list)

                #endif

            #endif
            elif gameInitiated == True and tutorialLevel == False:

                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 700:

                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:

                        load.Animation(loadNum) #Animation
                        loadNum += 1

                        if loadNum == 4: #If animation finished

                            loadNum = 0
                            load.Animation(loadNum)
                            startLoadTime = 0
                            endLoadTime = 0
                            level = levelToGo #Go to gameplay
                            fileLoaded = False
                            crownChecked = False
                            

                        #endif
                            
                    #endfor

                #endif

                loading_list.draw(screen) #Display objects

                if crownChecked == False: #Crown

                    crownChecked = True
                    SetCrown(crown_list)

                #endif

                if fileLoaded == False:

                    fileLoaded = True
                    
                    if currentFile == 1:

                        #Open File 1
                        f = open("Game_Files/File1.txt","r+") #Open file 1
                        lines = f.readlines() #All data
                        f.close() #Close

                    elif currentFile == 2:

                        #Open File 2
                        f = open("Game_Files/File2.txt","r+") #Open file 2
                        lines = f.readlines() #All data
                        f.close() #Close

                    elif currentFile == 3:

                        #Open File 3
                        f = open("Game_Files/File3.txt","r+") #Open file 3
                        lines = f.readlines() #All data
                        f.close() #Close

                    #endif

                    #Set currency
                    if lines[0][0] == "0" and lines[0][1] == "0" and lines[0][2] == "0":
                        currency = int(lines[0][3])
                    elif lines[0][0] == "0" and lines[0][1] == "0":
                        currency = int(lines[0][2] + lines[0][3])
                    elif lines[0][0] == "0":
                        currency = int(lines[0][1] + lines[0][2] + lines[0][3])
                    else:
                        currency = int(lines[0].rstrip("\n"))
                    #endif

                    #Set live
                    if lines[1][0] == "0":
                        live = int(lines[1][1])
                    else:
                        live = int(lines[1].rstrip("\n"))
                    #endif

                    #Set Level
                    gameLevel = int(lines[2][0])

                #endif

            elif tutorialLevel == True:

                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 500:

                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:

                        load.Animation(loadNum) #Animation
                        loadNum += 1

                        if loadNum == 4: #If animation finished

                            loadNum = 0
                            load.Animation(loadNum)
                            startLoadTime = 0
                            endLoadTime = 0
                            level = levelToGo #Go to gameplay
                            fileLoaded = False
                            crownChecked = False
                            

                        #endif
                            
                    #endfor

                #endif

                loading_list.draw(screen) #Display objects

            #endif

        elif level == 1: #Settings

            screen.fill(BLACK)

            for button in button_list:

                button.Change(pos, level)

            #endfor

            setting_list.draw(screen) #Display objects

        elif level == 2: #Tutorial

            screen.fill(WHITE)

            if tutorialReset == True:
                for cloud in cloud_list:
                    cloud.rect.x = 0
                #endfor
                tutorialReset = False
            #endif

            for thousand in thousand_list:
                thousand.Update(currency[0])
            #endfor
            for hundred in hundred_list:
                hundred.Update(currency[1])
            #endfor
            for ten in ten_list:
                ten.Update(currency[2])
            #endfor
            for one in one_list:
                one.Update(currency[3])
            #endfor

            for button in button_list: #Button Change

                button.Change(pos, level)

            #endfor

            for cloud in cloud_list:

                cloud.CloudUpdate()

                if cloud.rect.x <= -2560:
                    cloud.rect.x = 2560
                #endif

            #endfor

            for coin in coin_list:

                coin.Change()
                coin.CoinUpdate(player_list, block1_list, tutorialBlock_list, tutorial_list, levelOne_list, coin_list, currency)

            #endfor

            #Enemy Movement
            for enemy in tutorialEnemy_list:

                dummyEndAttack = pygame.time.get_ticks()
                if dummyEndAttack - dummyStartAttack > 3000:
                    dummyStartAttack = dummyEndAttack
                    for dummy in dummy_list:
                        dummy.AttackTrigger()
                    #endfor
                #endif

                enemy.Attack(dummyAttack_list)
                enemy.MoveHori(block1_list, tutorialBlock_list, level)
                enemy.AttackChecker()
                enemy.MoveVert(block1_list, tutorialBlock_list, level)
                enemy.Revive(dummyHealth_list)
                enemy.Hurt()
                enemy.EnemyAttackDetection(playerAttack_list,level)
                enemy.Health(dummyHealth_list, coin_list, tutorial_list, levelOne_list, level)
                enemy.Animation(dummyAnimation_list)

            #endfor

            #Player Movement
            for player in player_list:

                centered = False

                #Detection
                player.EnemyAttackDetection(dummyAttack_list,level)
                #Blocked
                player.Blocked()
                #Hurt
                player.Hurt()
                #Attack
                player.Attack(playerAttack_list)
                #Roll
                player.Roll()
                #Horizontal Movement
                player.MoveHori(centered, block1_list, tutorialBlock_list, startEnd_list, player_list, level, background_list) #Player move horizontally
                #Attack Checker
                player.AttackChecker()
                #Vertical Movement
                player.MoveVert(block1_list, tutorialBlock_list, level)
                #Death
                player.Revive(playerHealth_list)
                #Health
                player.Health(playerHealth_list)
                #Animation
                player.Animation(playerAnimation_list)

            #endfor

            tutorial_list.draw(screen) #Display all visible objects

        elif level == 3: #Save Files

            screen.fill(BLACK)

            for button in button_list:

                button.Change(pos, level)

            #endfor

            for item in item_list:

                item.Change()

            #endfor

            file_list.draw(screen) #Display all visible objects

        elif level == 4: #Level 1

            screen.fill(WHITE)

            #Player Movement
            for player in player_list:

                for cloud in cloud_list: #Cloud

                    cloud.CloudUpdate()

                    if cloud.rect.x == -2560:
                        cloud.rect.x = 2560
                    #endif

                #endfor

                #Centered
                for area in startEnd_list:
                    playerStartEnd_list = pygame.sprite.spritecollide(area, player_list, False)
                    for player in playerStartEnd_list:

                        centered = False

                    #endfor
                #endfor

                #Detection
                player.EnemyAttackDetection(dummyAttack_list,level)
                #Blocked
                player.Blocked()
                #Hurt
                player.Hurt()
                #Attack
                player.Attack(playerAttack_list)
                #Roll
                player.Roll()
                #Horizontal Movement
                player.MoveHori(centered, block1_list, tutorialBlock_list, startEnd_list, player_list, level, background_list) #Player move horizontally
                #Attack Checker
                player.AttackChecker()
                #Vertical Movement
                player.MoveVert(block1_list, tutorialBlock_list, level)
                #Death
                player.Death(playerHealth_list)
                #Health
                player.Health(playerHealth_list)
                #Animation
                player.Animation(playerAnimation_list)

            #endfor

            levelOne_list.draw(screen) #Display all visible objects

        #endif

        pygame.display.flip() #Flip the images

        clock.tick(60) #Tick

    #endwhile

#endprocedure

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1500,900)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("HEROTALE")
    
### -- Game Loop

Game() #Calls game

pygame.quit()
