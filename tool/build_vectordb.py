import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import SupabaseVectorStore
# 使用FAISS作最基本的vector DB
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# 使用supabase + postgres + pg_vector作為vector DB
# from supabase.client import Client, create_client

# https://python.langchain.com/v0.3/docs/integrations/vectorstores/supabase/
# Make sure the vector length is the same as the output of your selected embedding model

load_dotenv(find_dotenv())
"""
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)
"""
embedding = HuggingFaceEmbeddings(model_name='BAAI/bge-base-en-v1.5')

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",
    chunk_size=2000,
    chunk_overlap=200,
)

loader = TextLoader('../data/bipartisan_debates/bipartisan_debates/trump_harris_debate.txt')
raw_docs = loader.load()
docs = text_splitter.split_documents(raw_docs)
"""
vector_store = SupabaseVectorStore.from_documents(
    docs,
    embedding,
    client=supabase,
    table_name="documents",
    query_name="match_documents",
    chunk_size=500,
)
"""
vector_store = FAISS.from_documents(docs,embedding)
vector_store.save_local("faiss_index")
"""
new_vector_store = FAISS.load_local(
    "faiss_index", embeddings, allow_dangerous_deserialization=True
)
"""
