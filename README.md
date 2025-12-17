# Quoridor Game

A Python implementation of the classic Quoridor board game with AI opponents of varying difficulty levels.

## Game Description

Quoridor is a strategic board game where players race to reach the opposite side of a 9×9 grid while placing walls to block their opponent's path. The first player to reach their goal row wins!

## Features

**Complete Game Logic**
- Full rule implementation
- Path validation using BFS
- Jump mechanics and diagonal moves

**Graphical User Interface**
- pygame-based interface
- Interactive board with visual feedback
- Wall placement preview
- Valid move highlighting
- Player info sidebar

**Three AI Difficulty Levels**
- **Easy AI**: Random valid moves
- **Medium AI**: Path-based strategy using BFS
- **Hard AI**: Minimax with alpha-beta pruning

**Game Features**
- Undo/Redo functionality
- Save/Load game states
- Reset game
- Return to main menu

## Screenshots

> _Add your screenshots here after taking them from the game_

## Controls

### Mouse Controls
- **Left Click on Cell**: Move pawn to that position
- **Left Click Between Cells**: Place wall (if valid)
- **Hover Between Cells**: Preview wall placement

### Keyboard Shortcuts
- **R**: Reset game
- **U**: Undo last move
- **Y**: Redo undone move
- **S**: Save game
- **L**: Load game (coming soon)
- **ESC**: Return to main menu

### UI Buttons
- **Reset (R)**: Start a new game
- **Undo (U)**: Undo the last move
- **Redo (Y)**: Redo an undone move
- **Save (S)**: Save current game state
- **Load (L)**: Load saved game
- **Main Menu**: Return to game mode selection

## Installation

### Prerequisites
- Python 3.11 or higher
- pygame library

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Mayar0311/AIProject.git
cd AIProject/quoridor
```

2. **Install dependencies**
```bash
pip install pygame
```

## How to Run

### Running the Game

```bash
python src/main.py
```

Or navigate to the src directory:
```bash
cd src
python main.py
```

### Game Modes

From the main menu, select:
1. **Human vs Human** - Play against another person
2. **Human vs AI (Easy)** - Play against random AI
3. **Human vs AI (Medium)** - Play against path-based AI
4. **Human vs AI (Hard)** - Play against minimax AI

## Demo

> https://drive.google.com/drive/folders/1sfLYaLLkk7Chp4FHlZUIdbgsmYvVHZws

**Enjoy playing Quoridor!**
