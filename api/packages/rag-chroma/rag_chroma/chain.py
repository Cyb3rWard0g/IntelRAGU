from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

# Example for document loading (from url), splitting, and creating vectostore

""" 
# Load
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

# Split
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

# Add to vectorDB
vectorstore = Chroma.from_documents(documents=all_splits, 
                                    collection_name="rag-chroma",
                                    embedding=OpenAIEmbeddings(),
                                    )
retriever = vectorstore.as_retriever()
"""

"""
# Define a few variables
import os, glob

current_directory = os.path.dirname("__file__")
documents_directory = os.path.join(current_directory, "documents")
group_files = glob.glob(os.path.join(documents_directory, "*.md"))

# Load Documents
from langchain_community.document_loaders import UnstructuredMarkdownLoader

md_docs = []
for group in group_files:
    print(f' [*] Loading {os.path.basename(group)}')
    loader = UnstructuredMarkdownLoader(group)
    md_docs.extend(loader.load())

print(md_docs[0].page_content)

# Split Documents
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,  # number of tokens overlap between chunks
    separators=['\n\n', '\n', ' ', '']
)
chunks = text_splitter.split_documents(md_docs)

"""

# Download Dataset
from datasets import load_dataset
from langchain.docstore.document import Document

data = load_dataset('Cyb3rWard0g/ATTCKGroups',split='train')
chunks = data.to_list()
documents = []
for chunk in chunks:
    metadata = {"source": chunk['source']}
    new_doc = Document(page_content=chunk['text'], metadata=metadata)
    documents.append(new_doc)

# Create Vector Database
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(
    model_name="all-mpnet-base-v2"
)
vectorstore = Chroma.from_documents(
    documents,
    embedding_function,
    collection_name="rag-chroma",
)
retriever = vectorstore.as_retriever()

# RAG prompt
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# LLM
model = ChatOpenAI()

# RAG chain
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
)


# Add typing for input
class Question(BaseModel):
    __root__: str


chain = chain.with_types(input_type=Question)
