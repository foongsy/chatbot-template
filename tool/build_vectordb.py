import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from supabase.client import Client, create_client

load_dotenv(find_dotenv())

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

embedding = HuggingFaceEmbeddings('BAAI/BAAI/bge-base-en-v1.5')

loader = DirectoryLoader('../data/')
loader.load()

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",
    chunk_size=2000,
    chunk_overlap=200,
)

"""
https://www.info.gov.hk/gia/general/202406/20/P2024062000509.htm
https://www.info.gov.hk/gia/general/202406/18/P2024061800321.htm
https://www.info.gov.hk/gia/general/202406/13/P2024061300581.htm
https://www.info.gov.hk/gia/general/202406/13/P2024061300577.htm
https://www.info.gov.hk/gia/general/202406/11/P2024061100446.htm
https://www.info.gov.hk/gia/general/202406/11/P2024061100020.htm
https://www.info.gov.hk/gia/general/202406/07/P2024060600612.htm
https://www.info.gov.hk/gia/general/202406/06/P2024060600363.htm
https://www.info.gov.hk/gia/general/202406/04/P2024060400339.htm
"""