# Mohi's Bot

Mohi's Bot is an intelligent and interactive chatbot project that combines various technologies and frameworks to create a powerful conversational agent. The bot utilizes Python, Flask, Neo4j, Prolog, AIML, sentiment analysis, social networking, named entity recognition (NER), NLTK, WordNet, and web scraping to provide a comprehensive conversational experience.

## Features

- **Natural language processing (NLP)**: Mohi's Bot leverages AIML (Artificial Intelligence Markup Language) for natural language understanding and processing. It enables the chatbot to comprehend and respond appropriately to user queries.
- **Sentiment analysis**: The chatbot incorporates sentiment analysis techniques to analyze the emotional tone of user messages. It can gauge sentiment and tailor its responses accordingly, providing a more personalized interaction.
- **Social networking integration**: Mohi's Bot can seamlessly infer information about a user, establish social networking connections, and create relations. This enables the chatbot to provide more personalized and context-aware responses.
- **Knowledge base creation**: By integrating with Neo4j, a graph database, and Prolog, a logic programming language, the chatbot creates a dynamic knowledge base. It can generate nodes and establish relationships between entities, facilitating efficient information retrieval and enhancing the conversation flow.
- **Live graph visualization**: The chatbot provides a live graph representation of user behavior and their message tones. This feature enables users to visualize the underlying structure of their interactions and how the chatbot interprets their sentiments in real-time.
- **Named Entity Recognition (NER)**: Mohi's Bot incorporates NER techniques to identify and extract named entities from user inputs. This enables the chatbot to understand and respond to specific entities mentioned in user queries.
- **NLTK (Natural Language Toolkit)**: The chatbot utilizes NLTK for various NLP tasks such as tokenization, part-of-speech tagging, and word lemmatization. This enhances the chatbot's language processing capabilities.
- **WordNet**: Mohi's Bot leverages WordNet, a lexical database, to access lexical and semantic information. It helps the chatbot in understanding word meanings, synonyms, and related concepts.
- **Web scraping**: The chatbot includes web scraping capabilities to retrieve information from websites. This allows the chatbot to provide real-time data and relevant information to users based on their queries.

## Prerequisites

To run the Mohi's Bot project, you need to ensure the following prerequisites are met:

- **Python**: Install Python 3.x on your system. You can download the latest version from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
- **Flask**: Install Flask, a lightweight web framework for Python, by running the following command:
  ```
  pip install flask
  ```
- **Neo4j**: Install Neo4j, a graph database, by following the installation instructions provided on the official Neo4j website: [https://neo4j.com/download/](https://neo4j.com/download/).
- **Prolog**: Install a Prolog interpreter, such as SWI-Prolog, on your system. Instructions for different platforms can be found on the official SWI-Prolog website: [http://www.swi-prolog.org/Download.html](http://www.swi-prolog.org/Download.html). Additionally, install the `pyswip` package using the following command:
  ```
  pip install pyswip
  ```
- **NLTK**: Install NLTK by running the following command:
  ```
  pip install nltk
  ```
- **WordNet**: Download the WordNet corpus using NLTK. Launch the Python interpreter and run the following commands:
  ```python
  import nltk


  nltk.download('wordnet')
  ```
- **Other Dependencies**: Install the remaining project dependencies by running the following command in the project directory:
  ```
  pip install -r requirements.txt
  ```

## Getting Started

Follow these steps to get started with Mohi's Bot:

1. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/mohi0017/Mohi-s-Bot.git
   ```

2. Change into the project directory:
   ```
   cd Mohi-s-Bot
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

6. Access the chatbot in your web browser by visiting [http://localhost:5000](http://localhost:5000).

## Configuration

Before running the chatbot, you may need to modify the configuration settings in the `bot.py` file. Adjust the Neo4j server details, AIML files, and any other required settings according to your environment.

## Documentation

For detailed documentation and usage instructions, refer to the [documentation](documentation.md) file in this repository.

## Acknowledgements

The following libraries, frameworks, and technologies are utilized in Mohi's Bot:

- AIML: [https://github.com/AIML-Standard/aiml](https://github.com/AIML-Standard/aiml)
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Neo4j: [https://neo4j.com/](https://neo4j.com/)
- Prolog: [http://www.swi-prolog.org/](http://www.swi-prolog.org/)

Please refer to their respective documentation for more information and usage guidelines.

For any further assistance or inquiries, please contact the project maintainer at [mohi.pk0017@gmail.com](mailto:email@example.com).

Enjoy interacting with Mohi's Bot!
