import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from supabase.client import Client, create_client

# https://python.langchain.com/v0.2/docs/integrations/vectorstores/supabase/
# Make sure the vector length is the same as the output of your selected embedding model

load_dotenv(find_dotenv())

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

embedding = HuggingFaceEmbeddings(model_name='BAAI/bge-base-en-v1.5')


text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",
    chunk_size=2000,
    chunk_overlap=200,
)

loader = DirectoryLoader('../data/')
raw_docs = loader.load()
docs = text_splitter.split_documents(raw_docs)

vector_store = SupabaseVectorStore.from_documents(
    docs,
    embedding,
    client=supabase,
    table_name="documents",
    query_name="match_documents",
    chunk_size=500,
)
