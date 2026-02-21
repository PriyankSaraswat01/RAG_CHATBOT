from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def get_llm():
    pipe = pipeline(
        "text2text-generation",   # correct for flan-t5
        model="google/flan-t5-base",
        max_new_tokens=1000,
        temperature=0.3
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm