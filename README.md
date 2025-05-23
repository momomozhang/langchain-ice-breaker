# Ice Breaker 🤝
Built this while taking Eden Marco's LangChain course. It finds LinkedIn profiles and generates conversation starters. Added some extra features because it's fun!

It's an AI-powered web application that helps you prepare for meetings by generating conversation starters based on LinkedIn profiles. Simply enter someone's name, and get personalized ice breakers, interesting facts, and conversation topics!

![Ice Breaker Screenshot](<Screenshot 2025-05-23 at 15.59.21.png>)

### 🎯 Learning Goals Achieved

1. **Environment Setup**: Configured Python virtual environments and secure API key management with `.env`
2. **LangChain Framework**: Built my first LangChain application with chains, prompts, and output parsers
3. **Agentic Flows**: Implemented a ReAct agent that autonomously searches for LinkedIn profiles
4. **LLM Integration**: Worked with both OpenAI GPT-4 and local Ollama models
5. **Observability**: Set up LangSmith for monitoring LLM calls and debugging
6. **Web Development**: Created a Flask web app with interactive UI
7. **Type Safety**: Used Pydantic for robust data validation and typing

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- API keys for OpenAI(you can use any LLM of your choice), Tavily, and Scrapin.io

### Installation

```bash
# Clone the repository
git clone https://github.com/momomozhang/langchain-ice-breaker
cd ice_breaker

# Install dependencies
pipenv install

# Set up environment variables
cp .env.example .env
# Edit .env with your own API keys
```

### Running the Application

```bash
# Activate virtual environment
pipenv shell

# Start the Flask server
python app.py
```

Visit `http://localhost:5000` and enter a name to generate ice breakers!

## 💡 How It Works

1. **Name Input**: User enters a person's name
2. **Profile Discovery**: ReAct agent searches for their LinkedIn URL
3. **Data Extraction**: Scrapin.io API fetches profile information
4. **AI Processing**: the chosen llm generates:
   - Professional summary
   - Interesting facts
   - Ice breaker questions *(my addition)*
   - Topics of interest *(also mine)*
5. **Display Results**: Clean web interface shows all information

## 📁 Project Structure

```
.
├── agents/
│   └── linkedin_lookup_agent.py    # ReAct agent for finding profiles
├── third_parties/
│   └── linkedin.py                 # LinkedIn scraping logic
├── tools/
│   └── tools.py                    # Tavily search integration
├── templates/
│   └── index.html                  # Web UI
├── output_parsers.py               # Pydantic models for structured output
├── ice_breaker.py                  # Core application logic
├── app.py                          # Flask server
└── Pipfile                         # Dependencies
```

## 📝 Notes

This is a learning project focused on understanding LangChain concepts. For production use, consider:
- Rate limiting
- Error handling
- Caching mechanisms
- User authentication