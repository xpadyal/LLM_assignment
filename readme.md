# DeepScribe Chat Assistant

### Demo Link
```bash
https://deepscribe-llm-latest.onrender.com
```

## Overview

The DeepScribe Chat Assistant is a FastAPI application designed to facilitate querying patient transcripts using LangChain. It leverages advanced natural language processing techniques to assist medical providers in answering patient-related queries based on transcripts and SOAP notes.

## Features

- **Chat Interface**: Interact with the API to ask context aware questions about patient transcripts.
- **Dynamic Context**: The API intelligently retrieves relevant information using similarity search from transcripts and SOAP notes.
- **Hightlight Information** The application highlights important keywords regarding the paitient and you can further click on the highlighted text to view where the info is coming from.
- **GROQ** Used Groq API for Faster inference. Used llama3-70B as LLM model.
- **VectorDB**: Used chunking and similarity search for handling large information like long transcript.
- **Conversation Memory**: Passing message history as context for multiturn conversation and getting context-aware response for follow up questions.
- **Handles Incomplete Information** Handles incomplete information by gracefully declining to answer while also providing as much as possible detail about it.
- **Langserve and Langchain Ecosystem** Built on using langchain for efficient development and langserve for building API.
- **Docker** Containerised the application using docker for seemless deployment.
- **CORS Support**: The application supports Cross-Origin Resource Sharing (CORS) for frontend integration.

## Using Docker(Recommended)

### Prerequisites

Before running the application, make sure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- **API Keys**: You need valid API keys for both the GROQ and OpenAI APIs to run the application.

   - [Get a GROQ API key](https://groq.com/)
   - [Get an OpenAI API key](https://platform.openai.com/)

## Quick Start

To get the app running with Docker, follow these steps:

## Option 1: Pull from docker Hub

### 1. **Pull the Docker Image**

To pull the Docker image from Docker Hub, run the following command:

```bash
docker pull sahilpadyal237/deepscribe-llm:latest
```

## 2. Run the Docker Container

After the image is downloaded, you can run the Docker container. To do this, use the following command:

```bash
docker run -d -p 8000:8000 \
  -e GROQ_API_KEY=<your_groq_api_key> \
  -e OPENAI_API_KEY=<your_openai_api_key> \
  sahilpadyal237/deepscribe-llm:latest

```

For macOS (ARM64/Apple Silicon)
```bash
docker run --platform linux/arm64 -d -p 8000:8000 \
  -e GROQ_API_KEY=<your_groq_api_key> \
  -e OPENAI_API_KEY=<your_openai_api_key> \
  sahilpadyal237/deepscribe-llm:latest
```

For macOS (Intel x86_64)
```bash
docker run --platform linux/amd64 -d -p 8000:8000 \
  -e GROQ_API_KEY=<your_groq_api_key> \
  -e OPENAI_API_KEY=<your_openai_api_key> \
  sahilpadyal237/deepscribe-llm:latest
```

## Option 2: Run from Github

### 1. **Clone the Repository**

```bash
   git clone https://github.com/xpadyal/LLM_assignment.git
   cd LLM_assignment
```

### 2. **Build the Docker Image**
```bash
docker build -t deepscribe-llm .
```
### 3. **Run the Docker Image**
```bash
docker run -d -p 8080:80 deepscribe-llm
```

### 4. **Access the APP**'

```bash
http://localhost:8080
```


## Local Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xpadyal/LLM_assignment.git
   cd app
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r app/requirements.txt
   ```

4. Set up environment variables. Create a `.env` file in the `app` directory with the following content:

   ```env
   GROQ_API_KEY
   OPENAI_API_KEY
   ```
3. Setup the API routes:

   ```bash
   <add_localhosturl>/ask/invoke  in static/script.js sendrequest funtion
   ```

   ```bash
   <add_localhosturl>/notes  in static/script.js fetchNotes funtion
   ```

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
   
   ```

## Using Docker(Suggested)

### Prerequisites

Before running the application, make sure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Quick Start

To get the app running with Docker, follow these steps:

### 1. **Clone the Repository**

```bash
   git clone https://github.com/xpadyal/LLM_assignment.git
   cd LLM_assignment
```

### 2. **Build the Docker Image**
```bash
docker build -t deepscribe-llm .
```
### 3. **Run the Docker Image**
```bash
docker run -d -p 8080:80 deepscribe-llm
```

### 4. **Access the APP**'

```bash
http://localhost:8080
```


## API Endpoints

- **GET /**: Serves the frontend application.
- **POST /ask**: Queries the patient transcripts and SOAP notes.
- **GET /notes**: Retrieves the transcript and SOAP notes.

## File Structure

```
app/
│
├── chain.py               # Contains the custom chain for processing chat messages
├── chunking.py            # Handles splitting transcripts into manageable chunks
├── config.py              # Configuration settings loaded from environment variables
├── endpoints.py           # API endpoint definitions
├── main.py                # Entry point for the FastAPI application
├── middleware.py          # CORS middleware setup
├── notes.py               # Contains sample transcript and SOAP note data
├── requirements.txt       # Python dependencies
├── utils.py               # Utility functions for message conversion
└── vector_store.py        # Manages the vector store for transcript chunks
static/
│
├── index.html             # Main HTML file for the chat interface
├── script.js              # JavaScript for handling chat interactions
└── style.css              # CSS for styling the chat interface
```

## Approach

## LLM Integration Approach

In my implementation of the Large Language Model (LLM) within the DeepScribe Chat API, I followed a structured approach that utilizes the capabilities of LangChain and the ChatGroq model. Here are the key components of this integration:

1. **Model Initialization**:
   - I initialized the LLM using the `ChatGroq` class from the `langchain_groq` library. This model is configured with specific parameters, such as the model type (`"llama3-70B-8192"`) and the temperature setting (0.2), which controls the randomness of the model's responses.
   ```python
   model = ChatGroq(model="llama3-70B-8192", temperature=0.2)
   ```

2. **Vector Store Initialization**:
   - I set up a vector store using the `init_vector_store` function, which prepares the model to retrieve relevant chunks of text based on user queries. This vector store is essential for providing context to the LLM, allowing it to generate informed responses.
   ```python
   vector_store = init_vector_store()
   ```

3. **Custom Chain Function**:
   - The `custom_chain` function processes incoming chat messages. I extract the user's query from the last message and retrieve relevant context from the vector store using the `get_relevant_chunks` function.
   ```python
   def custom_chain(messages: list) -> dict:
       query = messages[-1]["content"]
       dynamic_context = get_relevant_chunks(query, vector_store)
   ```

4. **Prompt Construction**:
   - I constructed a system prompt to guide the LLM's behavior. This prompt includes instructions on how to respond to the user's query, emphasizing the importance of using the provided transcript and SOAP note. The prompt also instructs the model to highlight important information and ask follow-up questions if necessary.
   ```python
   system_template = """
   You are a medical assistant helping providers answer questions about a patient. 
   Use ONLY the following transcript and SOAP note.
   Intelligently bold the important information if the user asks for a particular information...
   """
   ```

5. **Message Handling**:
   - I prepared the messages for the LLM by creating a `ChatPromptTemplate` that combines the system prompt with the user's messages. This structured input is crucial for the LLM to generate coherent and contextually relevant responses.
   ```python
   prompt = ChatPromptTemplate.from_messages([
       ("system", system_template),
       MessagesPlaceholder(variable_name="messages")
   ])
   ```

6. **Chain Invocation**:
   - The constructed chain, which consists of the prompt and the model, is invoked with the prepared inputs. The model processes the input and generates a response based on the context provided by the relevant transcript chunks and the SOAP note.
   ```python
   chain = prompt | model
   result = chain.invoke(inputs)
   ```

7. **Response Handling**:
   - I extract the output from the model and return it in a structured format. This response is then sent back to the user, providing them with concise and relevant information based on their query.
   ```python
   return {"output": {"content": response_str}}
   ```

## LangServe Integration

In addition to the LLM integration, I also utilized LangServe to enhance the deployment and scalability of the language model. LangServe is a framework that allows for serving language models as APIs, making it easier to integrate them into applications. Here’s how I incorporated LangServe into my project:

1. **Model Serving**:
   - I used LangServe to deploy the ChatGroq model as a service. This allows the model to be accessed via HTTP requests, enabling seamless integration with the FastAPI application. By serving the model through LangServe, I can handle multiple requests concurrently, improving the responsiveness of the application.

2. **Configuration**:
   - I configured LangServe to specify the model parameters and the endpoint for accessing the model. This setup ensures that the FastAPI application can communicate effectively with the model service, allowing for efficient processing of user queries.

3. **Asynchronous Processing**:
   - LangServe supports asynchronous processing, which I leveraged to ensure that the API remains responsive while handling potentially long-running model inference tasks. This is particularly important in a medical context, where timely responses are crucial.

4. **Scalability**:
   - By using LangServe, I can easily scale the model service as needed. If the demand for the application increases, I can deploy additional instances of the model service without significant changes to the application code.

### Summary
The integration of the LLM in the DeepScribe Chat API is designed to facilitate intelligent interactions with users by leveraging contextual information from patient transcripts and SOAP notes. My approach emphasizes modularity, allowing for easy updates and maintenance while ensuring that the LLM can provide accurate and relevant responses based on the user's queries. Additionally, the use of LangServe enhances the deployment and scalability of the model, ensuring that the application can handle varying loads while maintaining performance. This setup not only enhances the user experience but also ensures that the responses are grounded in the provided medical context.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://langchain.readthedocs.io/en/latest/)

# THANK YOU



