# AI Agent Project

This project implements an AI Agent using Google's Agent Development Kit (ADK) and Gemini models.

## Prerequisites

- **Python 3.10+**: Ensure you have Python installed. The project has been tested with Python 3.13.
- **Git**: To clone the repository.
- **Google Cloud Project**: You need a Google Cloud project with the Gemini API enabled and an API Key.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd AI-Agent
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    Run the following command to download and install all necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    This will install:
    - `google-adk`: The core framework for building agents.
    - `python-dotenv`: For managing environment variables.
    - `google-generativeai`: The Google Gemini API client.

## Configuration

1.  **Set up Environment Variables:**
    Create a file named `.env` in the root directory of the project (same level as `requirements.txt`).
    
2.  **Add your API Key:**
    Open the `.env` file and add your Gemini API Key:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```
    *Note: The application internally sets `GOOGLE_API_KEY` based on `GEMINI_API_KEY`.*

## Running the Agent

You can run the agent using the provided batch script.

### Start the Web Interface
To start the ADK web interface:
```bash
./run_adk.bat web
```
This will launch a local server where you can interact with the `root_agent`.

### Run via Command Line (ADK CLI)
To use other ADK commands:
```bash
./run_adk.bat --help
```
