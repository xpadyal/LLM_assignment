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
- **Handles Incomplete Information** Handles incomplete information by suggesting the user possible outputs but also mentions that the info was incomplete.
- **Langserve and Langchain Ecosystem** Built on using langchain for efficient development and langserve for building API.
- **Docker** Containerised the application using docker for seemless deployment.
- **CORS Support**: The application supports Cross-Origin Resource Sharing (CORS) for frontend integration.

## Using Docker(Recommended)

### Prerequisites

Before running the application, make sure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

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
docker run -d -p 8080:80 sahilpadyal237/deepscribe-llm:latest
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





