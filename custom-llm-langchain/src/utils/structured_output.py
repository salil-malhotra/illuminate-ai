import openai
import json
import logging

class LLMOutputHelper:
    @staticmethod
    def get_structured_output(chain, input_text: str, api_key: str = None, schema: dict = None) -> dict:
        logging.info("Invoking chain for structured output.")
        if schema:
            input_text = (
                f"{input_text}\n\n"
                f"Please extract the following fields and return them as JSON: {list(schema.keys())}"
            )
        result = chain.invoke({"input_text": input_text})
        try:
            parsed = json.loads(result)
            logging.info("Successfully parsed structured output as JSON.")
            return parsed
        except Exception as e:
            logging.warning(f"Failed to parse output as JSON: {e}")
            if isinstance(result, str):
                return {"output": result}
            elif isinstance(result, dict):
                return result
            else:
                return {"output": str(result)}

    @staticmethod
    def openai_extract_contact_info(input_text: str, api_key: str, model: str = "gpt-4-0613") -> dict:
        logging.info("Calling OpenAI function for contact info extraction.")
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": f"Extract contact info from this text:\n\n{input_text}"
                }
            ],
            functions=[
                {
                    "name": "extract_contact_info",
                    "description": "Extracts contact info from user text",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "email": {"type": "string"},
                            "phone": {"type": "string"},
                            "location": {"type": "string"},
                        },
                        "required": ["name", "email", "phone", "location"]
                    }
                }
            ],
            function_call={"name": "extract_contact_info"}
        )
        arguments = response.choices[0].message.function_call.arguments
        try:
            parsed = json.loads(arguments)
            logging.info("Successfully parsed OpenAI function call output as JSON.")
            return parsed
        except Exception as e:
            logging.warning(f"Failed to parse OpenAI function call output as JSON: {e}")
            return {"output": arguments}