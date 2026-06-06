# 🔑 Cryptographically Secure Password Generator

A CLI security application built to generate password strings using kernel-level entropy pools rather than standard algorithmic pseudo-random calculations.

---

## ✨ Features

* 🔐 **True CSPRNG Integration:** Rejects standard deterministic PRNG structures, leveraging Python's `secrets` library to call underlying OS system parameters (`/dev/urandom`).
* 🛡️ **Guaranteed Category Inclusion:** Explicitly forces at least one selected parameter type into the initialization matrix array prior to full allocation expansion.
* 📊 **Entropy Complexity Evaluation:** Audits generated length constraints and character pool sizes to measure strength metrics natively.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.x
* **Core Libraries utilized:** `secrets` (CSPRNG Engine), `string` (Pre-compiled character arrays), `sys`, `time`
* **Security Compliance:** Designed to produce high-entropy keys capable of mitigating brute-force dictionary attacks.