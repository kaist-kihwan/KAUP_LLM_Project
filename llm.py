# Import Upstage Solar AI
from langchain_upstage import ChatUpstage

# For chatting
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# For groundedness check
from langchain_upstage import GroundednessCheck

# 
from langchain_upstage import UpstageEmbeddings

# 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt_template = PromptTemplate.from_template(
"""
Please provide most correct answer from the following context. 
If the answer is not present in the context, please write "The information is not present in the context."
---
Question: {Question}
---
Context: {Context}
"""
)


class Robot:
    def __init__(self, key:str):
        llm = ChatUpstage(api_key=key)
        embeddings_model = UpstageEmbeddings(api_key=key, model="solar-embedding-1-large")
        self.chain = prompt_template | llm | StrOutputParser()

    def _req_more_info(self):
        pass

    def start(card_num:int):
        pass

    def run(self, message:str) -> str:

        context = ""

        answer = self.chain.invoke({"Question":"", "Context":context})

    def quit(self):
        pass