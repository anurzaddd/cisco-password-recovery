# 🛡️ Cisco Catalyst 2960 Password Recovery Tool

> **Interactive CLI guide for recovering lost passwords on Cisco Catalyst 2960 switches**

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cisco](https://img.shields.io/badge/Cisco-2960-blue)](https://www.cisco.com/)

---

## ⚠️ DISCLAIMER

**This tool is for AUTHORIZED USE ONLY.**

You must have:
- **Physical access** to the switch
- **Authorization** from the network owner

Unauthorized access to network devices is **illegal** and violates:
- Computer Fraud and Abuse Act (CFAA)
- GDPR / Data Protection laws
- Corporate security policies

---

## 🎯 What This Tool Does

This is an **interactive step-by-step guide** that walks you through the official Cisco password recovery procedure for Catalyst 2960 switches.

**It does NOT "hack" or "crack" passwords.** Instead, it uses Cisco's built-in password recovery mechanism to **reset** the password[reference:31].

### Supported Models
- Catalyst 2960
- Catalyst 2960-S
- Catalyst 2960-X
- Catalyst 2960-CX
- Also works with: 2900XL, 2940, 2950, 2970, 3550, 3560, 3750[reference:32][reference:33]

---

## 🔧 How It Works

The tool guides you through these steps:

1. **Power cycle** with Mode button held → Enter boot loader mode (`switch:`)
2. **Initialize flash** (`flash_init`, `load_helper`)
3. **Rename config file** (`config.text` → `config.text.old`) to bypass password
4. **Boot** the switch without the config
5. **Restore** the original config and set a **new password**
6. **Verify** and save the configuration

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.6+
- Console cable (RJ-45 to DB-9 or USB)
- Terminal emulation software (PuTTY, SecureCRT, minicom, etc.)
- Physical access to the switch

### Terminal Settings
| Setting | Value |
|---------|-------|
| Baud rate | 9600 |
| Data bits | 8 |
| Parity | None |
| Stop bits | 1 |
| Flow Control | Xon/Xoff |

### Installation
```bash
git clone https://github.com/anurzaddd/cisco-2960-password-recovery.git
cd cisco-2960-password-recovery
