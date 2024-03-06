from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class create_embaddings:
    def __init__(self):
        model_name = "BAAI/bge-large-en"
        model_kwargs = {'device':'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        self.embeddings = HuggingFaceBgeEmbeddings(
            model_name = model_name,
            model_kwargs = model_kwargs,
            encode_kwargs = encode_kwargs
        )
        self.url = "http://localhost:6333"

    def loadfile(self,file,emb_name):
        #loader = PyPDFLoader("Best.pdf")
        self.file = file
        print(file)
        #print(file.file_path)
        loader = TextLoader(file)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 300,
            chunk_overlap = 50
        )
        texts = text_splitter.split_documents(documents)

        print("embeddings being created")

        collection_name = emb_name

        qdrant = Qdrant.from_documents(
            texts,
            self.embeddings,
            url = self.url,
            prefer_grpc = False,
            collection_name = collection_name
        )
        print("vectors created")

emb = create_embaddings()
try:
    file_path = r"C:\Users\srinivasc\OneDrive - Zenoti India Private Limited\Desktop\Qdrant\collections\SQL_Examples.txt"
    emb.loadfile(file_path,"SQL Examples")
except:
    print("invalid file")