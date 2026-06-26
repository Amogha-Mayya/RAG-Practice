from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0, # benefit : no abrupt cut of the text, drawback : more tokens
    separator=''
)

result = splitter.split_documents(docs)

print(result[0])