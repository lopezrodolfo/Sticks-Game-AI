# Game of Sticks AI

A Python implementation of the Game of Sticks with an AI opponent that learns from its games.

## Author

Rodolfo Lopez

## Date

Fall 2019

## Description

This program allows users to play the Game of Sticks against another player, an untrained AI, or a trained AI. The AI uses a learning algorithm to improve its strategy over multiple games.

## Features

- Player vs Player mode
- Player vs AI mode (untrained)
- Player vs AI mode (pre-trained)
- AI training through self-play
- Persistent AI learning (saves and loads hat contents)

## How to Play

1. Run `game_of_sticks.py`
2. Choose the initial number of sticks (10-100)
3. Select a game mode:
   1. Play against a friend
   2. Play against the computer (untrained)
   3. Play against the trained computer

## AI Learning

The AI uses a "hat and ball" system to learn:

- Each possible game state has a "hat" containing "balls" representing possible moves
- The AI selects moves randomly from the appropriate hat
- After each game, balls are added or removed based on the game's outcome

The `hat-contents.txt` file shows the current state of the AI's learning.
