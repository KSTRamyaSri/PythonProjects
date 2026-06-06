# 🎯 Number Guessing Game

A clean, modular, and highly interactive terminal logic game built entirely using Python's standard libraries. This project focuses on structured execution flows, explicit data type parsing, and custom text-based visual rendering patterns to deliver a clean gaming terminal UI.

---

## ✨ Features

* 🎮 **Dynamic Difficulty Matrices:** Features three operational modes—Easy (1-10), Medium (1-50), and Hard (1-100)—with varying attempt constraints.
* 📊 **Stateful Scoreboard Tracking:** Tracks total round counts, cumulative wins, and losses accurately throughout the execution runtime.
* ⚡ **Sleek UI Layout Design:** Implements custom ASCII boundary blocks and structured layouts using automated string configuration methods.
* 🔄 **Custom Loading Animation:** Simulates data parsing latency by printing progressive text-based loading loading frames (`▰▱▱▱...`) to enhance terminal immersion.
* 🛡️ **Robust Input Exception Handling:** Uses structural `try/except ValueError` safety guards to process input string mismatches without crashing the system thread.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.x
* **Core Libraries utilized:** `random` (for pseudorandom seed picking), `sys`, `time` (for system stream flushes and time gaps).
* **Programming Paradigm:** Object-Oriented utility separation using `@staticmethod` decorator configurations.

---

## 📈 Future Scope & Roadmap

To transition this basic logic utility from a console playground into a production-grade gaming application, the following updates are planned:

### 1. Web Deployment Migration
* **Objective:** Wrap the core mathematical tracking structures inside a dynamic web application.
* **Architecture:** Rebuild the client experience using **React.js** or vanilla **JavaScript (Canvas API)** to build fluid, graphics-based interface states with smooth user transition states.

### 2. High-Score Leaderboard Integration
* **Objective:** Introduce local or global persistence mechanisms to record user accomplishments permanently.
* **Tech Stack:** Link the backend execution endpoints to a **SQLite** or **PostgreSQL** relational tracking entity. 
* **Schema Plan:** Maintain a structural table tracking fields like `username`, `score_points`, `difficulty_tier`, and `timestamp_completed`.

### 3. Network Multiplayer Matchmaking
* **Objective:** Allow dual-client execution contexts where players can compete concurrently over network sockets.
* **Tech Stack:** Implement custom connection handlers using Python's native **`socket`** library or modern asynchronous **WebSockets**.