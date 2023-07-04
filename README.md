# Mohi's Bot

Mohi's Bot is a chatbot project that combines various technologies and frameworks to create an interactive and intelligent conversational agent. It utilizes Python, Flask, Neo4j, Prolog, AIML, sentiment analysis, social networking, and knowledge base creation to provide a rich conversational experience.

The chatbot leverages the power of natural language processing and sentiment analysis to understand and respond to user queries. By integrating with Neo4j, a graph database, and Prolog, a logic programming language, Mohi's Bot can create a knowledge base and establish relationships between different entities for enhanced conversation flow.

## Features

- Natural language processing: The chatbot utilizes AIML (Artificial Intelligence Markup Language) to understand and process user inputs.
- Sentiment analysis: Mohi's Bot employs sentiment analysis techniques to determine the emotional tone of user messages and respond accordingly.
- Social networking: The chatbot can integrate with social media platforms, enabling users to interact with it through popular messaging apps.
- Knowledge base creation: By leveraging Neo4j and Prolog, the bot can build a knowledge base, create nodes, and establish relationships for efficient information retrieval.
- Live graph visualization: The chatbot provides a live graph representation of the knowledge base, allowing users to visualize relationships and understand connections in real-time.

## Prerequisites

To run the Mohi's Bot project, you will need the following prerequisites:

- Python: Install Python 3.x on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Flask: Install Flask, a lightweight web framework for Python, by running the following command:
  ```
  pip install flask
  ```
- Neo4j: Install Neo4j, a graph database, by following the installation instructions provided on the official Neo4j website: [https://neo4j.com/download/](https://neo4j.com/download/)
- Prolog: Install a Prolog interpreter, such as SWI-Prolog, on your system. You can find installation instructions for different platforms on the official SWI-Prolog website: [http://www.swi-prolog.org/Download.html](http://www.swi-prolog.org/Download.html) then install pyswip using command pip install pyswip

## Getting Started

1. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/mohi0017/Mohi-s-Bot.git
   ```

2. Change into the project directory:
   ```
   cd Mohi's Bot
   ```

3. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the Neo4j server and ensure it is running.

5. Run the Flask application:
   ```
   python bot.py
   ```

6. Access the chatbot in your web browser by visiting [http://localhost:5000](http://localhost:8000)

## Configuration

Before running the chatbot, you may need to modify the configuration settings in the `bot.py` file. Adjust the Neo4j server details, AIML files, and any other required settings according to your environment.


## Acknowledgements

- AIML: [https://github.com/AIML-Standard/aiml](https://github.com/AIML-Standard/aiml)
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Neo4j: [https://neo4j.com/](https://neo4j.com/)
- Prolog: [http://www.swi-prolog.org/](http://www.swi-prolog.org/)
