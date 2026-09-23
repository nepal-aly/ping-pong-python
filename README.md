# Ping Pong Game 🎮

A classic two-player arcade Ping Pong game built in Python using the `turtle` graphics library and Object-Oriented Programming (OOP) principles.

---

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3.x
* **GUI Framework:** Turtle Graphics (Standard Library)
* **Paradigm:** Object-Oriented Programming (Classes, Encapsulation, State Management)

---

## 🏗️ Project Architecture

* **main.py** — Entry point, main game loop, screen updates, and key bindings
* **paddle.py** — Paddle creation, positioning, and movement logic
* **ball.py** — Ball movement dynamics, wall collisions, and speed mechanics
* **scoreboard.py** — Real-time score rendering and match winner detection
* **README.md** — Project documentation

---

## 🎮 Game Controls

* **Right Player:**
  * **Up Arrow:** Move Paddle Up
  * **Down Arrow:** Move Paddle Down

* **Left Player:**
  * **W Key:** Move Paddle Up
  * **S Key:** Move Paddle Down

---

## 🌟 Key Features

* **Modular OOP Architecture:** Clean separation of responsibilities across dedicated modules (`Paddle`, `Ball`, `Scoreboard`).
* **Physics & Reflection Engine:** Precise vector calculations for bouncing off horizontal walls and player paddles.
* **Dynamic Speed Acceleration:** Incremental ball speed increase after each successful hit to enhance challenge and engagement.
* **Automated Scoring System:** Instant boundary detection upon a miss, automatically updating scores and resetting the ball toward the opponent.

---

## 🚀 Getting Started

1. **Clone the repository:**
   `git clone https://github.com/nepal-aly/ping-pong-python.git`

2. **Navigate to directory:**
   `cd ping-pong-python`

3. **Run the application:**
   `python main.py`
