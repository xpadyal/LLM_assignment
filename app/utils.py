from typing import List, Dict, Union
from langchain_core.messages import HumanMessage, AIMessage

def convert_messages(messages: List[Dict[str, str]]) -> List[Union[HumanMessage, AIMessage]]:
    """
    Convert dictionary messages to LangChain message objects.
    """
    converted = []
    for msg in messages:
        role = msg.get("role")
        content = msg.get("content", "")
        if role == "user":
            converted.append(HumanMessage(content=content))
        elif role == "assistant":
            converted.append(AIMessage(content=content))
    return converted
