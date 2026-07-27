# Project 01: Rule-Based Chatbot

**DecodeLabs Internship — Project 01**
**Author:** Rayyan Aamir

## Description

A simple rule-based chatbot built in Python using basic control flow (if-else / dictionary lookup) logic. The chatbot, named **RayBot**, matches keywords in user input against a predefined knowledge base and responds accordingly. It runs in an interactive command-line loop until the user chooses to exit.

## Features

- Keyword-based response matching (e.g. "hello", "joke", "weather")
- Graceful fallback response for unrecognized input
- Multiple exit commands supported (`quit`, `exit`, `end`, `stop`, `bye`, `goodbye`)
- Handles empty input and keyboard interrupts (`Ctrl+C`) without crashing

## How It Works

The `RuleBasedChatbot` class stores a `knowledge_base` dictionary mapping trigger phrases to responses. For each user message:

1. Input is normalized (stripped and lowercased).
2. The bot checks if any exit command is present and ends the session if so.
3. Otherwise, it searches the knowledge base for a matching keyword substring and returns the associated response.
4. If no match is found, a default fallback message is shown.

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script from the terminal:

```bash
python ray-chatbot.py
```

Example session:

```
[RayBot]: Online and ready! (Type 'exit' to end session)
----------------------------------------------------------------------
You: hello
[RayBot]: Hello! I'm RayBot, a rule-based chatbot. How can I help you today?
----------------------------------------------------------------------
You: tell me a joke
[RayBot]: Why do programmers prefer dark mode? Because light attracts bugs xD
----------------------------------------------------------------------
You: exit
[RayBot]: Time to rest. Goodbye!
```

## Project Structure

```
Project-01/
└── ray-chatbot.py
```

## Possible Improvements

- Add more keywords/topics to the knowledge base
- Support natural language processing (NLP) for better intent matching
- Add persistent conversation logging