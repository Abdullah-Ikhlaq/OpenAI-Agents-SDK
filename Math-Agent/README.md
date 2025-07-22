# Math Expert Agent using Gemini API

This project demonstrates how to create a conversational agent acting as a **Maths Teacher** using the [OpenAI Agent SDK](https://github.com/openai/agent-sdk) and Google's **Gemini 2.0 Flash** model.

---

## Overview

The agent is designed to simulate a helpful math expert. It takes a user input and generates a response using the Gemini model via a custom OpenAI-compatible interface.

---

## Features

- Uses the OpenAI Agent SDK for structured agent workflows.
- Integrates Google's **Gemini API** through a custom `AsyncOpenAI` client.
- Defines a custom agent named **Math Expert**.
- Loads environment variables securely using `python-dotenv`.
- Demonstrates synchronous agent execution with `Runner.run_sync()`.

---

## Project Structure

```bash
├── main.py             # Main script to run the agent
├── .env                # Environment file to store Gemini API key
├── README.md           # Project documentation
```

## Requiremenqts

- Python 3.8+
- openai-agents
- python-dotenv

Install dependencies:
```bash
pip install openai-agents python-dotenv
```

## Setup

1. Clone this repository or copy the script.
2. Create a .env file in the root directory and add your Gemini API key:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```
3. Run the script:
```bash
python main.py
```

<!-- ## How It Works

1. Loads the Gemini API key from .env.
2. Sets up a custom AsyncOpenAI client to connect with Gemini.
3. Wraps it into a model (OpenAIChatCompletionsModel).
4. Uses RunConfig to define execution behavior.
5. Creates an Agent named Frontend Expert.
6. Sends a test message and prints the response. -->
 

## Usage

Run the script using:
```bash
python main.py
```

**Example Output:**
```bash
Hello! I'm here to help you with math. How can I assist you today?
```

## Notes

- tracing_disabled=True is set because OpenAI tracing requires an OpenAI API key.
- You need a valid Gemini API key from Google AI Studio or your Google Cloud Console.
- This script uses gemini-2.0-flash as the model.

