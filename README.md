# My-Advanced-RAG

# 🤖 Advanced PDF Chatbot (RAG System)

![Python](https://img.shields.io/badge/Language-Python_3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/Framework-LangChain-orange?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google_Gemini_1.5-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-76B900?style=for-the-badge&logo=database&logoColor=white)

## 📌 Overview
Ye ek advanced **Retrieval-Augmented Generation (RAG)** system hai jo Python 3.11 aur LangChain ka istemal karte hue banaya gaya hai. Ye project kisi bhi PDF file ko parh kar uska ek "Vector Knowledge Base" tyar karta hai, jis se aap baad mein Gemini AI ke zariye sawal-jawab kar sakte hain.

---

## 🚀 Key Features
* **Intelligent PDF Parsing**: PDF se text extract karke chunks mein divide karta hai.
* **Persistent Vector Store**: ChromaDB ka istemal karte hue `db_storage` folder mein data save karta hai taake baar baar PDF na parhni paray.
* **Semantic Retrieval**: HuggingFace embeddings ke zariye sawal se sab se relevant context dhoondta hai.
* **AI Generation**: Google Gemini 1.5 Flash model ka istemal behtareen aur accurate jawab daine ke liye.

---

## 📂 Project Structure
```bash
My-Advanced-RAG/
├── db_storage/         # 🧠 Vector Database (AI Memory)
├── main.py             # ⚙️ PDF Data Processing & Vector Creation
├── chat_bot.py         # 💬 Interactive Chat Interface
├── .env                # 🔑 API Keys & Secret Variables
├── .gitignore          # 🛡️ Git Security (Ignores secrets & heavy files)
└── requirements.txt    # 📋 Dependencies List

# 1. Purani khichri saaf karke naye versions install karne ke liye
py -3.11 -m pip install -U --force-reinstall langchain-google-genai google-generativeai pydantic

# 2. Path ki yellow warnings ko ignore karke libraries ko refresh karna
py -3.11 -m pip install -q -U google-genai

# 3. Pehle database (dimagh) ko dobara refresh karna (Optional but recommended)
py -3.11 main.py

# 4. Final Bot ko run karna
py -3.11 chat_bot.py