# Chat with Open Source LLM Models

This Chainlit app provides a sandbox environment for chatting with various open-source large language models (LLMs) hosted on RunPod. The application leverages Chainlit and OpenAI's API to facilitate interactions with the models.

## Features

- **Streamed Responses**: Get responses from the LLM in real-time as they are generated.
- **Session Management**: Maintains conversation history for context-aware responses.
- **Customization**: Easily switch between different models and adjust parameters such as temperature and maximum tokens.

## Prerequisites

- Python 3.7+
- RunPod API Key

## Installation and Setup

### Using Poetry for Dependency Management

1. **Install pipx**:
   Follow the instructions on the [pipx installation page](https://pipx.pypa.io/stable/installation/).

2. **Install Poetry**:
   Follow the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installing-with-pipx).

3. **Clone the Repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Install Dependencies**:
   ```sh
   poetry install
   ```

5. **Activate the Virtual Environment**:
   ```sh
   poetry shell
   ```

### Alternative: Using Virtual Environment and pip

If you don't want to use poetry, you can manage dependencies manually.

1. **Create Virtual Environment**:
   ```sh
   python -m venv myenv
   source myenv/bin/activate
   ```

2. **Install Dependencies**:
   ```sh
   pip install chainlit openai
   ```

## Configuration

1. **Set Your RunPod API Key**:
   Replace `<YOUR_RUNPOD_API_KEY>` in the script with your actual RunPod API key.

2. **Specify the Model**:
   Update the `model` variable with the desired model name, e.g., `"mistralai/Mistral-7B-Instruct-v0.2"`.

## Running the App

### Using Poetry

1. **Run the Chainlit App**:
   ```sh
   poetry shell
   chainlit run app.py -w
   ```

### Using Virtual Environment and pip

1. **Activate the Virtual Environment**:
   ```sh
   source myenv/bin/activate
   ```

2. **Run the Chainlit App**:
   ```sh
   chainlit run app.py -w
   ```

## Usage

- Once the application is running, open your browser and navigate to the displayed URL.
- Type your message and interact with the LLM model.
- The application maintains the conversation history, providing context-aware responses.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License.

