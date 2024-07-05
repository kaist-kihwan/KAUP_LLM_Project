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

#
from langchain_upstage import UpstageLayoutAnalysisLoader

#
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('SECRET_KEY')

layzer = UpstageLayoutAnalysisLoader(
    "manual/HOW_TO_CODE_THE_RORSCHACH.pdf", output_type="html", api_key=API_KEY
)
# For improved memory efficiency, consider using the lazy_load method to load documents page by page.
docs = layzer.load()
context = docs[0].page_content

prompt_template = PromptTemplate.from_template(
"""
As a helpful assistant,
please use your best judgment to determine proper code for human's reponse based on the following context.
If you need more information to determine, please write "I need more explanation. Can you explain it more specifically?"
---
Context: {Context}
---
Respond: It seems like a cat.
Output: Human's response is cat. Cat is an animal. The proper coding for cat is 'A'. Therfore, the output is 'A'.

Respond: {Respond}
Output:
"""
)


class Robot:
    def __init__(self):
        llm = ChatUpstage(api_key=API_KEY)
        #embeddings_model = UpstageEmbeddings(api_key=API_KEY, model="solar-embedding-1-large")
        self.chain = prompt_template | llm | StrOutputParser()

    def _req_more_info(self):
        pass

    def run(self, message:str):

        answer = self.chain.invoke({"Respond":message, "Context":context})
        return answer


    def quit(self):
        pass