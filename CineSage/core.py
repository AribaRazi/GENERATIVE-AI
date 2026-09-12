from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages(
    [("system",
     """
You are a precise information extraction assistant.

Extract information ONLY from the provided text.
Do not guess, assume, or add information that is not explicitly present.

Extract:

- title
- cast
- quick_summary

Rules:
1. "title" should contain the main title mentioned in the text.
2. "cast" should contain names explicitly identified as actors/cast members.
3. If actors are not explicitly mentioned, return an empty list for "cast".
4. "quick_summary" should be a concise 2-3 sentence summary.
5. Return ONLY valid JSON. Do not include markdown or explanations.

Output format:

{{
    "title": "",
    "cast": [],
    "quick_summary": ""
}}
"""
),
('human',
 """
extract infromation from this paragraph:
{paragraph}
""")]
)

# prompt template automatically assigns roles
paragraph = input("Enter your paragraph")
final_prompt = prompt.invoke(
    {"paragraph": paragraph}
)
response = model.invoke(final_prompt)

print(response.content)
