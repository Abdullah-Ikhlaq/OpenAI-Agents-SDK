# Frontend Expert Agent using Gemini API

This project demonstrates how to use the [OpenAI Agent SDK](https://github.com/openai/agent-sdk) to run a conversational agent powered by Google's **Gemini 2.0 Flash** model.

---

## 🚀 Features

- Utilizes the OpenAI Agent SDK framework.
- Integrates Google’s **Gemini** model via a custom `AsyncOpenAI` client.
- Loads API credentials securely using environment variables (`.env`).
- Defines and runs a frontend expert agent.
- Provides a synchronous execution flow with `Runner.run_sync()`.

---

## 📁 Project Structure

```bash
├── main.py             # Main script to run the agent
├── .env                # Environment file (contains your Gemin
