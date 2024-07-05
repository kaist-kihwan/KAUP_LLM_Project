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
As a helpful assistant,
please use your best judgment to determine proper code for human's repond based on the following context.
Please answer simple as you can.
If you need more information to determine, please write "I need more explanation. Can you explain it more specifically?"
---
Context: {Context}
---
Respond: It seems like a cat.
Output: Human's respond is cat. Cat is an animal. The proper coding for cat is 'A'. Therfore, the output is 'A'.

Respond: {Respond}
Output:
"""
)

context = """
'H' means human. If human's respond is similar to human, then proper coding of content must be 'H'.
'A' means animal. If human's respond is similar to animal, then proper coding of content must be 'A'.
'Fd' means food. If human's respond is similar to food, then proper coding of content must be 'Fd'.
"""


class Robot:
    def __init__(self, key:str):
        llm = ChatUpstage(api_key=key)
        #embeddings_model = UpstageEmbeddings(api_key=key, model="solar-embedding-1-large")
        self.chain = prompt_template | llm | StrOutputParser()

    def _req_more_info(self):
        pass

    def run(self, message:str):

        answer = self.chain.invoke({"Respond":message, "Context":context})
        return answer


    def quit(self):
        pass