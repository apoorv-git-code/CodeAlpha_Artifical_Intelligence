# 🎀 Real-Time Language Translator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/UI-Gradio-orange.svg)](https://gradio.app/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A lightweight, production-ready Python translation desktop application. Features a modern user interface, real-time API text processing, and on-the-fly audio pronunciation synthesis.

---

## 🚀 Core Features

- **Interactive User Workspace:** Clean input fields for source text and explicit output displays for translations.
- **Dynamic Language Selection:** Dropdown configuration supporting high-utility global language pairings (English, Spanish, French, German, Italian, Japanese).
- **Live API Integration:** Asynchronous communication with external translation layers for instant text computation.
- **Text-to-Speech (TTS) Playback:** Fulfills advanced usability criteria by converting translated text arrays into clear local `.mp3` speech audio.

---

## 🛠️ System Architecture

This tool uses a decoupled logical pipeline built entirely inside the **Python** ecosystem, separating network operations from client views.

```text
┌─────────────────┐             Text & Target Codes            ┌────────────────┐
│                 │ ─────────────────────────────────────────> │                │
│   Gradio UI     │                                            │ Python Backend │
│  (Client View)  │ <───────────────────────────────────────── │    Engine      │
└─────────────────┘             Text & .mp3 Payloads           └────────────────┘
         │                                                             ▲
         │ HTTP REST Request                                           │ API JSON Response
         ▼                                                             │
┌────────────────┐                                                     │
│  Translation   │ ────────────────────────────────────────────────────┘
│   Cloud API    │
└────────────────┘

```
## ⚙️ Prerequisites & Tech Stack

Ensure you have **Python 3.8+** installed. The core service dependencies include:

- **UI Blueprint:** `Gradio` — Handles state lifecycle rendering and client layouts.
- **Network Interface:** `Requests` — Handles robust HTTP communication protocols.
- **Audio Pipeline:** `gTTS` — Compiles string data pipelines directly into playable audio buffers.

---

## 💻 Getting Started

Follow these steps to spin up the translation engine pipeline on your local environment.

### 1. Installation

Clone this repository and install the project dependencies via pip:

```bash
pip install gradio requests gtts python-dotenv

```
### 2. Execution

Initialize the application server by executing the core script:

```bash
python app.py

```
### 3. Application Access

Once live, the local development server initializes a loopback socket. Open your browser and navigate to:

```bash
[http://127.0.0.1:7860](http://127.0.0.1:7860)

```
### 📁 Repository Structure & Modules

```text
├── app.py              # Main application file containing engine logic and UI layout
├── README.md           # Project documentation and architectural overview
└── requirements.txt    # Tracking file for software dependencies

```
<p align="center">
  <img width="498" height="498" alt="MeTranslatingEverythingCatComputerGIF (2)" src="https://github.com/user-attachments/assets/73a6a440-eec8-479a-a04b-9e77815f048b" />
</p>
