import logging

def setup_chains(custom_llm):
    from langchain.prompts import PromptTemplate

    logging.info("Setting up prompt template and chain.")

    # Define a prompt template
    prompt_template = PromptTemplate(
        input_variables=["input_text"],
        template="Generate a response based on the following input: {input_text}"
    )

    # Combine prompt template and LLM using RunnableSequence
    chain = prompt_template | custom_llm

    logging.info("Chain setup complete.")
    return chain