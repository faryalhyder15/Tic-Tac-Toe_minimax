# 🎮 Tic-Tac-Toe AI using Minimax & Alpha-Beta Pruning

This project implements a **Tic-Tac-Toe game** where two intelligent agents compete using the **Minimax algorithm** enhanced with **Alpha-Beta pruning**.

---

## 📌 Features

- ✅ Fully functional Tic-Tac-Toe game (3x3 board)
- 🤖 Two AI agents:
  - **MAX (X)** → Maximizing player
  - **MIN (O)** → Minimizing player
- 🧠 Uses **Minimax Algorithm** for optimal decision making
- ⚡ Optimized using **Alpha-Beta Pruning**
- 📊 Displays:
  - Sequence of moves
  - Utility (score) of each move
  - Alpha (α) and Beta (β) values
  - Alpha-Beta cutoffs
- 🏁 Automatically plays full game until win/draw

---

## 🧠 Algorithms Used

### 🔹 Minimax Algorithm
- Explores all possible game states
- Ensures optimal move selection
- Utility values:
  - `+1` → X wins
  - `-1` → O wins
  - `0` → Draw

### 🔹 Alpha-Beta Pruning
- Reduces unnecessary computations
- Prunes branches where β ≤ α
- Improves performance without affecting result

---

## 🗂️ Project Structure


tictactoe_minimax.py # Main Python file
README.md # Project documentation


## 📊 Results

- Both agents play optimally  
- Game always results in a **Draw**  
- Confirms correctness of Minimax strategy  

---

## 📚 Concepts Covered

- Artificial Intelligence  
- Adversarial Search  
- Game Theory  
- Minimax Algorithm  
- Alpha-Beta Pruning  

---

## 🚀 Future Improvements

- 🎨 Add GUI (Tkinter / Pygame)  
- 👤 Human vs AI mode  
- 📈 Visualization of search tree  
- 🎯 Extend to larger games (e.g., Connect-4)  

---
## ▶️ How to Run

### Step 1: Install Python
Make sure Python is installed on your system.

### Step 2: Clone Repository
```bash
git clone https://github.com/your-username/tictactoe-ai.git
cd tictactoe-ai

---

## 👩‍💻 Author

**Faryal Jafferi**
