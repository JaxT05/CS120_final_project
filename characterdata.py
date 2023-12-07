#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Jax Tobyas

"""
class Character(object):       
    def __init__(self, name = "Guardian", hitChance = 50, hitPoints = 10, maxDamage = 5, maxHitPoints = 10, armor = 2):
        super().__init__()
        self.name = name 
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.maxHitPoints = maxHitPoints
        self.armor = armor 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value
    
    @property 
    def hitPoints(self):
         return self._hitPoints
    
    
    @hitPoints.setter
    def hitPoints(self,value):
        if type(value) == int:
            self._hitPoints = value
        else: 
            print("Hit points must be an integer.")
            self._hitPoints = 10
        
    @property 
    def hitChance(self):
        return self._hitChance 
    
    @hitChance.setter 
    def hitChance(self,value):
        if type(value) == int:
            if value in range(1,100):
                self._hitChance = value 
            else:
                print("Hit chance must be between 0 and 100.")
                self._hitChance = 50
        else: 
            print("Hit chance must be an integer.")
     
    @property 
    def maxDamage(self):
        return self._maxDamage
    
    @maxDamage.setter
    def maxDamage(self,value):
        if type(value) == int:
            if value >= 0: 
                self._maxDamage = value
            else: 
                print("MAX DMG must be a positive number.")
                self._maxDamage = 5
        else: 
            print("MAX DMG must be an integer.")
            self._maxDamage = 5       
    
    @property
    def maxHitPoints(self):
        return self._maxHitPoints
    
    @maxHitPoints.setter
    def maxHitPoints(self,value):
        if type(value) == int:
            if value >= 0:
                self._maxHitPoints = value 
            else: 
                print("MAX HITPOINTS most be a positive number.")
                self._maxHitPoints = 10
        else:
            print("MAX HITPOINTS must be an integer.")
            self._maxHitPoints = 10
    @property 
    def armor(self):
        return self._armor
    
    @armor.setter
    def armor(self,value):
        if type(value) == int:
            if value >= 0: 
                self._armor = value
            else: 
                self._armor = 0
        else:
            self._armor = 0