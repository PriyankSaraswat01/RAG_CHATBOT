# from langchain_community.llms import HuggingFacePipeline
# from transformers import pipeline

# def get_llm():
#     pipe = pipeline(
#         "text2text-generation",
#         model="google/flan-t5-base",
#         max_new_tokens=150,
#         temperature=0.7,
#         top_p=0.9,
#         repetition_penalty=1.2,
#         no_repeat_ngram_size=3,
#         do_sample=True
#     )

#     return HuggingFacePipeline(pipeline=pipe)


from langchain_openai import ChatOpenAI

def get_llm():
    llm = ChatOpenAI(
        model="gpt-4o-mini",   # Best cost-effective model
        temperature=0.3
    )
    return llm