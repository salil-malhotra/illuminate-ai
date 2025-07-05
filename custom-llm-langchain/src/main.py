# filepath: custom-llm-langchain/src/main.py

import os
import json
from chains.chain_setup import setup_chains
from llm.custom_llm import GeminiLLM, ClaudeLLM, OpenAILLM, LlamaLLM
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(filename)s %(name)s %(message)s"
)

def main():
    provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    api_key = (
        os.getenv("OPENAI_API_KEY") if provider == "openai"
        else os.getenv("ANTHROPIC_API_KEY") if provider == "claude"
        else os.getenv("GOOGLE_API_KEY") if provider == "gemini"
        else None
    )
    llama_model_path = os.getenv("LLAMA_MODEL_PATH")

    if provider == "openai":
        model = OpenAILLM(api_key)
    elif provider == "claude":
        model = ClaudeLLM(api_key)
    elif provider == "llama":
        if not llama_model_path:
            raise ValueError("LLAMA_MODEL_PATH environment variable must be set for Llama provider")
        model = LlamaLLM(llama_model_path)
    elif provider == "gemini":
        model = GeminiLLM(api_key)
    else:
        raise ValueError("Unsupported LLM provider")

    chains = setup_chains(model.llm)

    # Step 1: Example prompt to generate text
    prompt = "Once upon a time"
    logging.info(f"Using {provider} model to generate text...")
    # Generate text using the model
    generated_text = chains.invoke({"input_text": "Once upon a time"})
    logging.info(f"Raw Generated Text: {generated_text}")

    # Step 2: Example of adding scructured output handling by adding schema instruction to the prompt
    # If schema is provided, it will instruct the LLM to return output in JSON matching the schema
    schema = {
        "name": "string",
        "email": "string",
        "phone": "string", 
        "location": "string"
    }
    text =  "My name is Sponge Bob, you can reach me at sponge@krustrykrab.com or call me at +1-919-BOB-SPNG. I live in Bikini Bottom."

    from utils.structured_output import LLMOutputHelper
    result = LLMOutputHelper.get_structured_output(chains, text, api_key, schema=schema)
    
    # log the structured output in a readable format
    logging.info(json.dumps(result, indent=2, ensure_ascii=True))
    # Step 3: Example of using OpenAI function calling to extract structured data
    if provider == "openai":
        contact_info = LLMOutputHelper.openai_extract_contact_info(text, api_key=api_key, model="gpt-4-0613")
        logging.info(f"Contact Info: {contact_info}")

if __name__ == "__main__":
    main()