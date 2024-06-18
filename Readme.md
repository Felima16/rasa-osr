# Rasa OSR Readme

Welcome to the Rasa implementation repository. This README file provides instructions and information on setting up, running, and customizing your Rasa chatbot. 

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Training the Model](#training-the-model)
- [Running the Bot](#running-the-bot)
- [License](#license)

## Introduction

This repository contains the implementation of a Rasa chatbot. Rasa is an open-source machine learning framework for building contextual AI assistants and chatbots. This chatbot is designed to provide a flexible and scalable solution for various conversational AI applications and used to OSR game.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or later
- pip (Python package installer)
- Virtual environment tool (optional but recommended, e.g., `virtualenv` or `conda`)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Felima16/rasa-osr.git
   cd rasa-chatbot
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   # On Windows, use `venv\Scripts\activate`
   ```

## Project Structure

```
rasa/
├── actions/
│   ├── __init__.py
│   └── custom_actions.py
├── data/
│   ├── nlu.yml
│   ├── stories.yml
│   └── rules.yml
├── models/
│   └── (trained models will be stored here)
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
├── requirements.txt
└── tests/
    └── conversation_tests.yml
```

- `actions/`: Custom action implementations.
- `data/`: Training data for NLU and core models.
- `models/`: Directory where trained models are stored.
- `config.yml`: Configuration file for the Rasa pipeline and policies.
- `credentials.yml`: Credentials for various channels and services.
- `domain.yml`: Domain file defining intents, entities, slots, and responses.
- `endpoints.yml`: Configuration for connecting to external services.
- `tests/`: Directory for test files.

## Configuration

Ensure the `config.yml`, `domain.yml`, `credentials.yml`, and `endpoints.yml` files are correctly set up according to your requirements. These files define the behavior, responses, and connections for your chatbot.

## Training the Model

To train the Rasa model, run the following command:
```sh
rasa train
```
This will train both the NLU and core models using the data provided in the `data/` directory.

## Running the Bot

To start the Rasa server, use the following commands:

1. **Start the Rasa server:**
   ```sh
   rasa shell
   ```

## Customization

- **Adding intents and entities:** Update the `data/nlu.yml` file.
- **Creating new stories:** Update the `data/stories.yml` file.
- **Defining new responses:** Update the `domain.yml` file.
- **Writing custom actions:** Implement your actions in the `actions/custom_actions.py` file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Thank you for using our Rasa chatbot implementation. If you have any questions or need further assistance, please feel free to contact us. Happy coding!