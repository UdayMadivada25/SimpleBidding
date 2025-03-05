# 🏆 Secret Auction Program

A simple **secret auction** program implemented in Python. This program allows multiple participants to place their bids **anonymously**, and once all bids are collected, it determines and announces the **highest bidder**.

## 🚀 Features
- 🎨 **ASCII Art Logo** for a fun auction experience.
- 👥 **Multiple Bidders** can participate.
- 🧹 **Clears Console** between bids to maintain secrecy.
- 🏆 **Determines the Highest Bidder** and announces the winner.

## 🛠️ Files Overview
- **`main.py`** → Contains the main auction logic, including user input handling and bid calculations.
- **`art.py`** → Includes ASCII art for the auction logo.

## 📜 How the Auction Works
1. The program starts by displaying an **auction logo**.
2. Users enter their **name** and **bid amount**.
3. The program asks if there are more bidders:
   - If **"yes"**, the next participant enters their details.
   - If **"no"**, the program determines the highest bidder.
4. The winner is determined using two different methods:
   - **Method 1**: Using Python’s `max()` function.
   - **Method 2**: A custom function `find_highest_bidder()`.

## 🏗️ Installation & Running the Program
1. **Clone the repository**:
   ```sh
   git clone https://github.com/UdayMadivada25/SimpleBidding.git

