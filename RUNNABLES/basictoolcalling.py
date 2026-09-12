from langchain.tools import tool
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

@tool #decorator for creating tool 
def get_greeting(name : str) -> str: #type hints
    """Generate a greeting message for a user""" #docstring

    # return f"Hello {name}, Welcome to the AI world"


# inserting llm
llm = ChatMistralAI(
    model ="ministral-14b-2512"
)

llms_with_tools = llm.bind_tools([get_greeting])

response = llms_with_tools.invoke(
    "Please greet Ariba very sweetly"
)

result = get_greeting.invoke({"name":"ariba"})
# print(result)

# print(get_greeting.name)
# print(get_greeting.description)
# print(get_greeting.args)

print(response)