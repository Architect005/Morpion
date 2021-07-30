#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## morpion
## File description:
## morpion's game
##

import pygame

def display_board(case):
    #display the game board
    i = 1
    for i in case:
            print (i)
    return (0)

def win_condition(case):
    #line's condition win
    if case[0] == ['x', 'x', 'x'] or case[0] == ['o', 'o', 'o']:
        print("You win!")
        return (1)
    if case[1] == ['x', 'x', 'x'] or case[1] == ['o', 'o', 'o']:
        print("You win!")
        return (1)
    if case[2] == ['x', 'x', 'x'] or case[2] == ['o', 'o', 'o']:
        print("You win!")
        return (1)
    #column's condition win
    if (case[0][0] == 'x' or case[0][0] == 'o') and (case[1][0] == 'x' or case[1][0] == 'o'):
        if case[2][0] == 'x' or case[2][0] == 'o':
            print("You win!")
            return (1)
    if (case[0][1] == 'x' or case[0][1] == 'o') and (case[1][1] == 'x' or case[1][1] == 'o'):
        if case[2][1] == 'x' or case[2][1] == 'o':
            print("You win!")
            return (1)
    if (case[0][2] == 'x' or case[0][2] == 'o') and (case[1][2] == 'x' or case[1][2] == 'x'):
        if case[2][2] == 'x' or case[2][2] == 'o':
            print("You win!")
            return (1)
    #diagonal's condition win_condition
    if (case[0][0] == 'x' or case[0][0] == 'o') and (case[1][1] == 'x' or case[1][1] == 'o'):
        if case[2][2] == 'x' or case[2][2] == 'o':
            print("You win!")
            return (1)
    if (case[0][2] == 'x' or case[0][2] == 'o') and (case[1][1] == 'x' or case[1][1] == 'o'):
        if case[2][0] == 'x' or case[2][0] == 'o':
            print("You win!")
            return (1)
    return (0)

def game_engine():
    case = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    display_board(case)
    while (1):
        #take player 1's input
        print("player 1: ")
        row = int(input("x?"))
        col = int(input("y?"))
        #verify input
        if (row < 0 or row > 2) or (col < 0 or col > 2):
            print("invalid position! RESTART")
            game_engine()
        #insert cross
        if case[row][col] == ' ':
            case[row][col] = "x"
        else:
            print("nop!")
        display_board(case)

        if win_condition(case) == 1:
            break
        #take player 2's input
        print("player 2: ")
        row = int(input("x?"))
        col = int(input("y?"))
        #verify input
        if (row < 0 or row > 2) or (col < 0 or col > 2):
            print("invalid position! RESTART")
            game_engine()
        #insert circle
        if case[row][col] == ' ':
            case[row][col] = "o"
        else:
            print("nop!")
        display_board(case)
        #verify win_condition's condition
        if win_condition(case) == 1:
            break
    return (0)

background_colour = (255,255,255)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_engine()
    pygame.display.flip()
