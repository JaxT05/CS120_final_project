#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Jax Tobyas

"""
import simpleGE, pygame, random, characterdata

class ButtonQuit(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 25)
        self.text = "QUIT"
        self.hide()
        self.bgColor = ("black")
        self.fgColor = ("white")
    
    
class ButtonReset(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 25)
        self.text = "RESTART"
        self.hide()
        self.bgColor = ("black")
        self.fgColor = ("white")
    

class SpritelyFellow (simpleGE.BasicSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("spritelyfellow.png")
        self.setSize(200,200)
        self.x = 310
        self.y = 200
        
class Textbox (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 19)
        self.textLines = ["Make your move."]
        self.center = ((320, 340))
        self.size = ((500, 140))
        self.bgColor = ("black")
        self.fgColor = ("white")
        
class PlayerStats(simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 19)
        self.center = ((110,100))
        self.size = ((180, 210))
        self.bgColor = (33, 11, 11,10)
        self.fgColor = ("white")

class EnemyStats(simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 19)
        self.center = ((530,100))
        self.size = ((180, 210))
        self.bgColor = (33, 10, 10,10)
        self.fgColor = ("white")
        
class FightBtn(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 25)
        self.text = "FIGHT"
        self.center = ((180,430))
        self.size = ((100,35))
        self.bgColor = (33, 10, 10)
        self.fgColor = ("white")
class HealBtn(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 25)
        self.text = "HEAL"
        self.center = ((460,430))
        self.size = ((100,35))
        self.bgColor = (33, 10, 10)
        self.fgColor = ("white")

class CastBtn(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 25)
        self.text = "CAST"
        self.center = ((320,430))
        self.size = ((100,35))
        self.bgColor = (33, 10, 10)
        self.fgColor = ("white")

class ContinueBtn(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("VT323-Regular.ttf", 25)
        self.text = "CONTINUE"
        self.center = ((320,430))
        self.size = ((100,35))
        self.hide()
        self.bgColor = (33, 10, 10)
        self.fgColor = ("white")

class BattleScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Survive!")
        
        self.background = pygame.image.load("background.png")
        pygame.mixer.music.load("tiny_swords_duel.ogg")
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)
        
        self.healsound = simpleGE.Sound("health_restore.wav")
        self.castsound = simpleGE.Sound("magic_words.wav")
        self.fightsound = simpleGE.Sound("bing1.wav")
        self.fightmiss = simpleGE.Sound("swordswish.wav")
        self.castmiss = simpleGE.Sound("Doomed.flac")
        self.enemyhit = simpleGE.Sound("hit01.wav")
        self.healmiss = simpleGE.Sound("shortwind.wav")
        
        
        self.background = pygame.transform.scale(self.background, (640,480))
        self.enemy = SpritelyFellow(self)
        self.fightbtn = FightBtn()
        self.healbtn = HealBtn()
        self.castbtn = CastBtn()
        self.continuebtn = ContinueBtn()
        
        self.btnreset = ButtonReset()
        self.btnquit = ButtonQuit()
        
        self.playerstats = PlayerStats()
        self.enemystats = EnemyStats()
        
        self.lblEnemyHP = simpleGE.Label()
        self.lblEnemyHP.font = pygame.font.Font("VT323-Regular.ttf", 18)
        self.lblEnemyHP.text = f"Enemy Hit Points: {enemy.maxHitPoints}/{enemy.maxHitPoints}"
        self.lblEnemyHP.center = (460,50)
        self.lblEnemyHP.size = (200,30)
        
        self.textbox = Textbox()
        
        
        self.sprites = [self.enemy, self.fightbtn, self.healbtn, self.castbtn, self.continuebtn, self.btnreset, self.btnquit, self.textbox, self.enemystats, self.playerstats]
    
    def pauseGame(self):
        self.enemy.hide()
        self.fightbtn.hide()
        self.healbtn.hide()
        self.castbtn.hide()
        self.continuebtn.hide()
        self.enemystats.hide()
        self.playerstats.hide()
        self.btnquit.show((220, 240))
        self.btnreset.show((420, 240))
    
    def resetGame(self):
        enemy.hitPoints = enemy.maxHitPoints
        player.hitPoints = player.maxHitPoints
        enemy.hitChance = 60
        player.hitChance = 60
        enemy.maxDamage = 10
        player.maxDamage = 10
        enemy.armor = 2
        player.armor = 2
        
        self.btnquit.hide()
        self.btnreset.hide()
        
        self.textbox.textLines = ["Make your move."]
        self.enemy.x = 310
        self.enemy.y = 200
        self.fightbtn.show((180,430))
        self.healbtn.show((460,430))
        self.castbtn.show((320,430))
        self.enemystats.show((530,100))
        self.playerstats.show((110,100))
        
        
    
    def EnemyHit(self):
        if random.randint(1,100) < enemy.hitChance:
            self.enemyhit.play()
            origDamage = random.randint(1, enemy.maxDamage) 
            damage = origDamage - player.armor
            if damage < 0: 
                damage = 0 
            player.hitPoints -= damage
            if player.hitPoints < 0:
                player.hitPoints = 0
            self.textbox.textLines = [
                "Enemy hit!",
                f"Dealt {origDamage} damage!",
                f"With armor, that's {damage} damage."
                ]
        else: 
            self.textbox.textLines = ["Enemy missed!"]
    
    def PlayerHit(self):
        if random.randint(1,100) < player.hitChance:
            self.fightsound.play()
            origDamage = random.randint(1, enemy.maxDamage) 
            damage = origDamage - enemy.armor
            if damage < 0: 
                damage = 0 
            enemy.hitPoints -= damage
            if enemy.hitPoints < 0:
                enemy.hitPoints = 0
            self.textbox.textLines = [
                "That's a hit!",
                f"Dealt {origDamage} damage!",
                f"With armor, that's {damage} damage."
                ]
        else:
            self.fightmiss.play()
            self.textbox.textLines = ["That's a miss!"]
    
    def PlayerCast(self):
        if random.randint(1,100) < player.hitChance:
            self.castsound.play()
            castType = random.randint(1,3)
            if castType == 1:
                target = random.randint(1,2)
                if target == 1:
                    changeHitChance = random.randint(1,5)
                    player.hitChance += changeHitChance
                    self.textbox.textLines = [
                        "Player cast for higher hit chance on self.",
                        f"Added {changeHitChance} to hit chance!"]
                if target == 2:
                    changeHitChance = random.randint(1,5)
                    enemy.hitChance -= changeHitChance
                    if enemy.hitChance < 0:
                        enemy.hitChance = 0
                    self.textbox.textLines = [
                        "Player cast for lower hit chance on enemy.",
                        f"Lowered enemy's hit chance by {changeHitChance}."]
                    
                
            if castType == 2:
                target = random.randint(1,2)
                if target == 1:
                    changeArmor = random.randint(1,2)
                    player.armor += changeArmor 
                    self.textbox.textLines = [
                        "Player cast for higher defense on self.",
                        f"Added {changeArmor} to defense!"]
                if target == 2: 
                    changeArmor = random.randint(1,2)
                    enemy.armor -= changeArmor 
                    if enemy.armor < 0:
                        enemy.armor = 0
                    self.textbox.textLines = [
                        "Player cast for lower defense on enemy",
                        f"Lowered enemy's defense by {changeArmor}."]
            if castType == 3:
                target = random.randint(1,2)
                if target == 1:
                    changeMAXDMG = random.randint(1,4)
                    player.maxDamage += changeMAXDMG
                    self.textbox.textLines = [
                        "Player cast for higher max damage on self.",
                        f"Added {changeMAXDMG} to max damage!"]
                if target == 2: 
                    changeMAXDMG = random.randint(1,4)
                    enemy.maxDamage -= changeMAXDMG
                    if enemy.maxDamage < 0:
                        enemy.maxDamage = 0
                    self.textbox.textLines = [
                        "Player cast for lower max damage on enemy.",
                        f"Lowered enemy's max damage by {changeMAXDMG}."]
            
        else:
            evilCastType = random.randint(1,3)
            self.castmiss.play()
            if evilCastType == 1:
                target = random.randint(1,2)
                if target == 1:
                    changeHitChance = random.randint(1,5)
                    player.hitChance -= changeHitChance
                    self.textbox.textLines = [
                        "Misfire!",
                        f"Player's hit chance lowered by {changeHitChance}."]
                    if player.hitChance < 0:
                        player.hitChance = 0
                if target == 2:
                    changeHitChance = random.randint(1,5)
                    enemy.hitChance += changeHitChance
                    self.textbox.textLines = [
                        "Misfire!", 
                        f"Enemy's hit chance increased by {changeHitChance}."]
            
            if evilCastType == 2:
                target = random.randint(1,2)
                if target == 1:
                    changeArmor = random.randint(1,2)
                    player.armor -= changeArmor 
                    self.textbox.textLines = [
                        "Misfire!", 
                        f"Player's defense lowered by {changeArmor}."]
                    if player.armor < 0:
                        player.armor = 0
                if target == 2:
                    changeArmor = random.randint(1,2)
                    enemy.armor += changeArmor 
                    self.textbox.textLines = [
                        "Misfire!", 
                        f"Enemy's defense increased by {changeArmor}."]
            
            if evilCastType == 3:
                target = random.randint(1,2)
                if target == 1:
                    changeMAXDMG = random.randint(1,4)
                    player.maxDamage -= changeMAXDMG
                    if player.maxDamage < 0:
                        player.maxDamage = 0
                    self.textbox.textLines = [
                        "Misfire!", 
                        f"Player's max damage decreased by {changeMAXDMG}."]
                if target == 2:
                    changeMAXDMG = random.randint(1,4)
                    enemy.maxDamage += changeMAXDMG
                    self.textbox.textLines = [
                        "Misfire!",
                        f"Enemy's max damage increased by {changeMAXDMG}."]
                   
    def PlayerHeal(self):
        if random.randint(1,100) < player.hitChance:
            self.healsound.play()
            heal = random.randint(1, player.maxDamage) 
            player.hitPoints += heal
            if player.hitPoints > player.maxHitPoints:
                player.hitPoints = player.maxHitPoints
            self.textbox.textLines = [
                "Successfully healed!",
                f"{heal} points restored."]
            
        else: 
            self.healmiss.play()
            self.textbox.textLines = ["Failed to heal."]
    
    def update(self):
        if self.fightbtn.clicked:
            self.fightbtn.hide()
            self.healbtn.hide()
            self.castbtn.hide()
            self.PlayerHit()
            self.continuebtn.show((320,430))
        
        if self.healbtn.clicked:
            self.fightbtn.hide()
            self.healbtn.hide()
            self.castbtn.hide()
            self.PlayerHeal()
            self.continuebtn.show((320,430))
        
        if self.castbtn.clicked:
            self.fightbtn.hide()
            self.healbtn.hide()
            self.castbtn.hide()
            self.PlayerCast()
            self.continuebtn.show((320,430))
        
        if self.continuebtn.clicked:
            self.continuebtn.hide()
            self.EnemyHit()
            self.fightbtn.show((180,430))
            self.healbtn.show((460,430))
            self.castbtn.show((320,430))
        
        if self.btnreset.clicked:
            self.resetGame()
        if self.btnquit.clicked:
            self.stop()
            
        self.playerstats.textLines = [
            "Player Stats:",
                f"HP: {player.hitPoints}/{player.maxHitPoints}",
                f"Defense: {player.armor}",
                f"Hit Chance: {player.hitChance}",
                f"Max DMG: {player.maxDamage}"
                ]
        self.enemystats.textLines = [
            "Enemy Stats:",
                f"HP: {enemy.hitPoints}/{enemy.maxHitPoints}",
                f"Defense: {enemy.armor}",
                f"Hit Chance: {enemy.hitChance}",
                f"Max DMG: {enemy.maxDamage}"
                ]
        
        self.lblEnemyHP.text = f"Enemy Hit Points: {enemy.hitPoints}/{enemy.maxHitPoints}"
       
        if player.hitPoints <= 0: 
            self.textbox.textLines = ["Player knocked out."]
            self.pauseGame()
        if enemy.hitPoints <= 0:
            self.textbox.textLines = ["Enemy knocked out. You win!"]
            self.pauseGame()

if __name__ == "__main__":
    player = characterdata.Character()
    player.name = "Guardian"
    player.hitPoints = 30
    player.hitChance = 60
    player.maxDamage = 10
    player.maxHitPoints = 30
    player.armor = 2
    enemy = characterdata.Character("Smok", 60, 60, 10, 60, 2)
    game = BattleScene()
    game.start()

    

    