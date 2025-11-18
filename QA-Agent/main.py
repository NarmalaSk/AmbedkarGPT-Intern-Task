from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
import argparse




def rag_pipeline(query,txtfile):

    

    with open(f"{txtfile}.txt", "r") as f:
        data = f.read()


    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separator='.',
        strip_whitespace=True
    )
    chunks = text_splitter.create_documents([data])


    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="speech_store"
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}  
    )


    prompt = PromptTemplate.from_template("""
        Use the following context to answer the question:
        {context}
    
        Question: {question}
        Answer:
    """)


    llm = OllamaLLM(model="mistral") 
    chain = (
        {"context": retriever, "question": lambda x: x}
        | prompt
        | llm
        | StrOutputParser()
    )

    result = chain.invoke(f"{query}")

    print(result)


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("query", help="Query for LLM")
    parser.add_argument("speechfile", help="Txt file for data")
    args=parser.parse_args()

    if args.query and args.speechfile:
        rag_pipeline(args.query,args.speechfile)
