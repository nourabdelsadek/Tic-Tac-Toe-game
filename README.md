# **Tic-Tac-Toe Game (Python OOP)**  

## **Overview**  
This is a Python implementation of the classic **Tic-Tac-Toe** game using **Object-Oriented Programming (OOP) principles**, including **encapsulation** and **inheritance**. The game allows two players to compete in a turn-based format, ensuring a fair and interactive experience.

## **Features**  
✅ **Encapsulation:** Player names and symbols are private attributes to prevent modification.  
✅ **Inheritance:**  
- `HumanPlayer` inherits from `Player` (extensible for AI players in the future).  
- `TicTacToeBoard` extends `Board`, making it adaptable for different board sizes.  
- `TicTacToeGame` extends `Game`, allowing modifications for additional rules.  
✅ **Validation Checks:** Prevents invalid moves and duplicate selections.  
✅ **Interactive Console-Based Play:** Players take turns choosing their moves.  
✅ **Win Condition Checks:** Identifies row, column, and diagonal victories.  

## **How to Run the Game**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-python.git
   cd tic-tac-toe-python
   ```
2. Run the script:  
   ```bash
   python tic_tac_toe.py
   ```
3. Follow the on-screen instructions to play.  

## **Future Improvements**  
🚀 Add AI-based opponent using **Minimax Algorithm**.  
🎨 Implement a **GUI version** using Tkinter or Pygame.  
📱 Convert into a **web-based game** using Flask/Django.  

