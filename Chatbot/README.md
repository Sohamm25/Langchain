# LangChain AI Chatbot

A simple yet powerful AI chatbot implementation using LangChain, supporting both cloud-based (OpenAI) and local (Ollama/LLaMA2) models.

## 🚀 Features

- **Dual Implementation**: Choose between cloud-based or local AI models
- **Simple UI**: Clean Streamlit interface for asking questions
- **LangSmith Integration**: Track and analyze your prompts and responses
- **Easy Setup**: Minimal configuration required

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key (for app.py)
- Ollama installed locally (for localama.py)
- LangSmith API key (optional, for tracing)

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/langchain-ai-chatbot.git
   cd langchain-ai-chatbot
   ```

2. Install required packages:
   ```bash
   pip install langchain langchain-openai langchain-core python-dotenv streamlit
   
   # For the Ollama implementation
   pip install langchain-community
   ```

3. Create a `.env` file in the project root:
   ```
   # Required for app.py
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Optional for LangSmith tracing
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_API_KEY=your_langsmith_api_key_here
   ```

## ▶️ Usage

### OpenAI Version
Run the OpenAI-based chatbot:
```bash
streamlit run app.py
```

> **Note:** Using the OpenAI version requires an OpenAI API key and will incur charges based on your usage. Check [OpenAI's pricing page](https://openai.com/pricing) for current rates.

### Local LLaMA Version
1. First, install Ollama from [https://ollama.ai/](https://ollama.ai/)
2. Pull the LLaMA2 model:
   ```bash
   ollama pull llama2
   ```
3. Run the local chatbot:
   ```bash
   streamlit run localama.py
   ```

> **Note:** The local version runs entirely on your machine and doesn't require internet connection after setup. Performance depends on your hardware.

## ⚙️ How It Works

The application uses LangChain to create a processing pipeline:
1. User input is captured via the Streamlit interface
2. The input is formatted using a predefined prompt template
3. The formatted prompt is sent to the selected AI model
4. The response is parsed and displayed back to the user

## 🔍 LangSmith Integration

This project includes LangSmith integration for monitoring and debugging your AI interactions. To use this feature:

1. Create an account at [LangSmith](https://smith.langchain.com/)
2. Get your API key from the LangSmith dashboard
3. Add the key to your `.env` file

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/langchain-ai-chatbot/issues).

## 📜 License

This project is [MIT](LICENSE) licensed.

---

Made with ❤️ using LangChain
