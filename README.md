# React LangGraph Agent

This project implements a simple AI agent using the LangGraph library. The agent is designed to answer questions by reasoning and using a set of predefined tools.

## How it Works

The agent is built as a state machine using LangGraph. The graph has two main nodes:

1.  **Agent Reasoning**: This node is responsible for taking the user's query and deciding whether to use a tool or to respond directly. It is powered by the `llama-3.3-70b-versatile` model from Groq.
2.  **Action**: If the agent decides to use a tool, this node is executed. It uses the appropriate tool based on the agent's decision and returns the output to the agent for further reasoning.

The agent has access to the following tools:

*   **Tavily Search**: To search the web for information.
*   **Triple**: A custom tool that triples a given number.

The agent will continue to reason and use tools until it has a final answer for the user.

## Technologies Used

*   [LangChain](https://python.langchain.com/)
*   [LangGraph](https://python.langchain.com/docs/langgraph)
*   [Groq](https://groq.com/) for the LLM
*   [Tavily](https://tavily.com/) for web searches
*   Python 3.11

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/reactLangGraph.git
    cd reactLangGraph
    ```

2.  **Install dependencies:**
    This project uses `uv` for package management.
    ```bash
    pip install uv
    uv pip install -r requirements.txt 
    ```
    If you are not using `uv` you can install the dependencies from the `pyproject.toml`
     ```bash
    pip install -e .
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root of the project and add your API keys:
    ```
    GROQ_API_KEY="your-groq-api-key"
    TAVILY_API_KEY="your-tavily-api-key"
    ```

4.  **Run the agent:**
    ```bash
    python main.py
    ```
