# 🤖 Agent Development Kit (ADK) — Learning Repository

A hands-on, progressive learning repository for building AI agents using **Google's Agent Development Kit (ADK)**. Each module builds on the previous one, taking you from a simple greeting agent to a fully stateful, multi-agent customer service system.

> **Built with:** Google ADK • LiteLLM • OpenRouter • Python 3.13

---

## 📚 Modules

### 1️⃣ Basic Agent — `1-basic-agent/`
> Your first AI agent — a simple greeting agent.

- Introduction to the ADK framework
- Creating your first `LlmAgent`
- Running agents with `adk web`

```
1-basic-agent/
└── greeting_agent/
    ├── __init__.py
    └── agent.py
```

---

### 2️⃣ Tool Agent — `2-tool-agent/`
> Giving your agent superpowers with custom tools.

- Defining Python functions as tools
- Connecting tools to an agent
- Understanding how ADK calls tools automatically

```
2-tool-agent/
└── tool-agent/
    ├── __init__.py
    └── agent.py
```

---

### 4️⃣ Structured Output — `4-structured-output/`
> Generating structured, predictable responses from your agent.

- Enforcing output schemas
- Working with structured email-style responses

```
4-structured-output/
└── emal_agent/
    ├── __init__.py
    └── agent.py
```

---

### 5️⃣ Sessions & State — `5-sessions-and-state/`
> Making agents remember things within a conversation.

- Introduction to `InMemorySessionService`
- Managing session state (read/write)
- Building a stateful Q&A agent

```
5-sessions-and-state/
├── basic_stateful_session.py
└── question_answering_agent/
    ├── __init__.py
    └── agent.py
```

---

### 6️⃣ Persistent Storage — `6-persistatt-storage/`
> Persisting agent memory across sessions using a database.

- Switching from `InMemorySessionService` → `DatabaseSessionService`
- SQLite-backed persistence
- Building a reminder/memory agent with CRUD operations
- Using `ToolContext` for state management inside tools

```
6-persistatt-storage/
├── main.py
├── utils.py
└── memory_agent/
    ├── __init__.py
    └── agent.py
```

---

### 7️⃣ Multi-Agent System — `7-multi-agent/`
> Orchestrating multiple specialized agents under a manager.

- Creating a **Manager Agent** that delegates tasks
- Sub-agents: `stock_analyst`, `funny_nerd`, `news_analyst`
- Using `AgentTool` to call agents as tools
- Using `transfer_to_agent` for agent-to-agent handoff
- Custom tools: stock price lookup (`yfinance`), news search (`duckduckgo-search`)

```
7-multi-agent/
└── manager/
    ├── __init__.py
    ├── agent.py              # Root manager agent
    └── sub_agents/
        ├── funny_nerd/
        │   └── agent.py      # Joke-telling agent
        ├── news_analyst/
        │   └── agent.py      # News fetching agent (DuckDuckGo)
        └── stock_analyst/
            └── agent.py      # Stock price agent (yfinance)
```

---

### 8️⃣ Stateful Multi-Agent System — `8-stateful-multi-agent/`
> A production-style customer service system with state management.

- Full customer service workflow with **4 specialized sub-agents**
- Shared state across agents (`purchased_courses`, `interaction_history`)
- XML-style prompt tagging for structured instructions
- Tools that modify session state (purchase, refund)
- Interaction history tracking

```
8-stateful-multi-agent/
├── main.py                           # Entry point with chat loop
├── utils.py                          # State display & agent response processing
└── customer_service_agent/
    ├── __init__.py
    ├── agent.py                      # Root customer service agent
    └── sub_agents/
        ├── course_support_agent/     # Course content help
        ├── order_agent/              # Purchase history & refunds
        ├── policy_agent/             # Community guidelines & policies
        └── sales_agent/              # Course purchases
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- An [OpenRouter](https://openrouter.ai/) API key (free tier available)

### Installation

```bash
# Clone the repository
git clone https://github.com/itsharshitb/agent-development-kit.git
cd agent-development-kit

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the relevant module directory (e.g., `7-multi-agent/manager/.env`):

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### Running an Agent

**Option 1: ADK Web UI** (for modules 1–7)
```bash
cd 7-multi-agent
adk web
# Open http://localhost:8000 in your browser
```

**Option 2: Terminal** (for modules 6 & 8)
```bash
cd 8-stateful-multi-agent
python main.py
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Google ADK](https://github.com/google/adk-python) | Agent framework (agents, tools, sessions, runners) |
| [LiteLLM](https://github.com/BerriAI/litellm) | Unified LLM API interface |
| [OpenRouter](https://openrouter.ai/) | LLM provider (Arcee, Llama, etc.) |
| [yfinance](https://github.com/ranaroussi/yfinance) | Stock market data |
| [DuckDuckGo Search](https://github.com/deedy5/duckduckgo_search) | Web/news search (no API key needed) |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment variable management |

---

## 📖 Key Concepts Covered

- **Agent Creation** — Building agents with `LlmAgent` and custom instructions
- **Tool Integration** — Wrapping Python functions as ADK tools
- **Session Management** — In-memory and persistent (SQLite) session storage
- **State Management** — Reading/writing state via `ToolContext`
- **Multi-Agent Orchestration** — Manager → sub-agent delegation patterns
- **Agent-as-Tool** — Using `AgentTool` to call agents like functions
- **Agent Transfer** — Using `transfer_to_agent` for conversation handoff
- **Prompt Engineering** — XML-style tagging, structured instructions, guard clauses

---

## 📝 License

This project is for educational purposes. Feel free to use and modify the code for your own learning.

---

## 👤 Author

**Harshit Bhatt** — [@itsharshitb](https://github.com/itsharshitb)
