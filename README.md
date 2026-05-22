# 2048 (Python Terminal Game)
A terminal-based Python implementation of the classic 2048 puzzle game. Slide tiles across a 4x4 grid, merge matching numbers, and work your way up to the 2048 tile.

---

## How to Play
1. Run the game - the board starts with a single **2** in a random cell
2. Use **W/A/S/D** to slide all tiles in a direction
3. Matching tiles that collide **merge** into one doubled tile
4. A new **2** spawns in a random empty cell after each move
5. Reach the **2048** tile to win - or keep going for a high score!

---

## Controls
| Key | Direction |
|---|---|
| W | Up |
| A | Left |
| S | Down |
| D | Right |

---

## Features
- 4x4 grid rendered in the terminal after every move
- Tiles merge and compress correctly in all four directions
- New 2 spawns in a random empty cell after each valid move
- Win detection when the 2048 tile is reached
- Game over detection when no moves remain
- Invalid key handling for any input outside W/A/S/D

---

## Example
```
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 2, 0]
[0, 0, 0, 0]
Press a key (W/A/S/D): a
[0, 0, 0, 0]
[0, 0, 0, 0]
[2, 0, 0, 0]
[0, 0, 2, 0]
Press a key (W/A/S/D): s
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[2, 0, 2, 2]
Press a key (W/A/S/D): d
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 2, 0, 0]
[0, 0, 2, 4]
```

---

## Tech Stack
| Technology | Purpose |
|---|---|
| Python | Game logic and terminal interface |

---

## Project Structure
| File | Purpose |
|---|---|
| `logic.py` | All game logic (compress, merge, move, state checking) |
| `2048.py` | Main game loop and player input handling |

---

## Getting Started

### Prerequisites
- Python 3 installed

### Installation
```bash
# Clone the repository
git clone https://github.com/kevvvvvz/2048-python.git

# Navigate into the project
cd 2048-python

# Run the game
python 2048.py
```

---

## Future Improvements
- Score tracking that updates as tiles merge
- High score saved across sessions
- Restart option without closing the terminal
- Color-coded tiles for better readability
