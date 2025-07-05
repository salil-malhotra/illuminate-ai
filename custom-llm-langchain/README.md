# Custom Language Model with LangChain

This project demonstrates how to integrate multiple large language model (LLM) providers—such as OpenAI, Anthropic Claude, Google Gemini, and local Llama models—using the [LangChain](https://python.langchain.com/) framework. It provides a modular and extensible approach for experimenting with different LLMs in a unified interface.

## Project Structure

```
custom-llm-langchain
├── src
│   ├── main.py              # Entry point of the application
│   ├── llm
│   │   ├── custom_llms.py   # LLM provider wrappers (OpenAI, Claude, Llama, Gemini)
│   ├── chains
│   │   └── chain_setup.py   # Prompt template and chain configuration
│   └── utils
│       └── helpers.py       # Utility functions for data processing and evaluation
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd custom-llm-langchain
   ```

2. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables for your chosen provider:**
   - For **OpenAI**:  
     `export OPENAI_API_KEY=your-openai-key`
   - For **Anthropic Claude**:  
     `export ANTHROPIC_API_KEY=your-anthropic-key`
   - For **Google Gemini**:  
     `export GOOGLE_API_KEY=your-google-api-key`
   - For **Llama (local)**:  
     `export LLAMA_MODEL_PATH=/path/to/your/llama-model.gguf`

4. **Choose your provider:**  
   Set the provider with  
   `export LLM_PROVIDER=openai`  
   (or `claude`, `gemini`, `llama`)

## Usage

To run the application, execute:
```sh
python -m src.main
```
or, if you prefer:
```sh
PYTHONPATH=src python src/main.py
```

## Overview

- The `custom_llms.py` file in `src/llm/` contains wrapper classes for each supported LLM provider.
- The `setup_chains` function in `src/chains/chain_setup.py` uses a prompt template and combines it with the selected LLM using LangChain's RunnableSequence (`prompt_template | llm`).
- The main script (`src/main.py`) selects the provider based on environment variables, initializes the appropriate LLM, and runs a sample prompt through the chain.

## Supported Providers

- **OpenAI GPT** (`openai`)
- **Anthropic Claude** (`claude`)
- **Google Gemini** (`gemini`)
- **Llama (local, via llama.cpp)** (`llama`)

## Example Prompt

The default prompt is:
```
Once upon a time
```
You can modify this in `src/main.py` as needed.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.

---

**Note:**  
- Ensure you comply with each provider's terms of service and usage policies.
- For Llama, you must obtain the model weights from [Meta](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) or [Hugging Face](https://huggingface.co/models?search=llama) and convert them to `.gguf` format
- [openai migrate](https://github.com/openai/openai-python/discussions/742) is very useful to update the code with newer versions.