#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:34:24 2020

@author: katherinekane
"""

## Instructions

#Using a while loop, ask the user "How many numbers?", then print out a chain of ascending numbers, starting at 0.

#After the results have printed ask the user if they would like to continue.

  #If "y", restart the process, starting at 0 again.

  # If "n", exit the chain.

## Bonus

#Rather than just displaying numbers constantly starting at 0, have the numbers begin at the end of the previous chain.

run = "y"

while run == "y":

    user_input = int(input("How many numbers? "))


    for x in range(0, user_input + 1):
        print(x)

    run = input("Would you like to continue? (y or n) ")

    if run == "n":
        exit

    
    
    
    

    
    
    