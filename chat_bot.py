import os
import warnings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Warnings chupane ke liye
warnings.filterwarnings("ignore")
load_dotenv()

def start_chatting():
    print("🤖 AI Bot ko jagaya ja raha hai...")

    # 1. Database load karein
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="db_storage", embedding_function=embeddings)

    # 2. Gemini AI setup
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    print("\n✅ AI Bot Tayyar Hai! Aap PDF ke bare mein kuch bhi puch sakte hain.")
    print("(Exit karne ke liye 'exit' ya 'quit' likhein)\n")

    while True:
        query = input("👉 Aapka Sawal: ")
        
        if query.lower() in ['exit', 'quit']:
            print("Khuda Hafiz! 👋")
            break
        
        if query.strip() == "":
            continue

        print("🔍 AI Soch raha hai...")
        try:
            # 3. Asaan Tareeka: Direct similarity search + LLM
            # Pehle database se relevant tukre dhoondo
            docs = db.similarity_search(query, k=3)
            context = "\n".join([d.page_content for d in docs])
            
            # AI ko prompt bhejo
            prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer based on context:"
            response = llm.invoke(prompt)
            
            print(f"\n🤖 AI Jawab: {response.content}\n")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Kuch ghalat ho gaya: {e}")

if __name__ == "__main__":
    start_chatting()