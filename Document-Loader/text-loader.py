from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()
prompt = PromptTemplate(
    template = 'Summarize the follwing text in 5 sentences: {text}',
    input_variables = ['text']
)

loader = TextLoader("document.txt")


docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'text': docs[0].page_content}))
