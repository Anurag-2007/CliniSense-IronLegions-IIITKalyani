# 🩺 CliniSense  
**AI-Powered Clinical Note Summarizer & Diagnostic Assistant**

CliniSense transforms chaotic clinical narratives into structured, actionable insights—empowering healthcare professionals with fast, accurate, and explainable decision support.

Built on a robust LangChain-powered pipeline, CliniSense combines semantic retrieval, medical prompt tuning, and LLM reasoning to deliver high-precision summaries and differential diagnoses.

---

## 🚀 Key Features
- ✅ **Summarizes messy clinical notes** into clean, structured medical text  
- ✅ **Generates differential diagnoses** with confidence levels: High / Medium / Low  
- ✅ **Justifies each diagnosis** with cited evidence from the input  
- ✅ **Outputs readable, EMR-compatible summaries** in JSON and human text  

---

## 🧠 How It Works

CliniSense follows a multi-stage pipeline for deep contextual understanding:

1. **Recursive Chunking** → Breaks long clinical notes into manageable segments  
2. **Semantic Embedding** → Uses MiniLM (HuggingFace) for high-dimensional representation  
3. **Contextual Retrieval** → FAISS vector search finds the most relevant evidence chunks  
4. **Prompt-Tuned Reasoning** → GPT-4o-mini generates summaries and diagnoses  
5. **Structured Output** → JSON + Regex post-processing for EMR integration  

---



---

## ⚙️ Tech Stack

| Layer            | Tools & Frameworks                            |
|------------------|-----------------------------------------------|
| **Backend**      | Python, Flask                                 |
| **LLM Engine**   | OpenAI GPT-4o-mini (medical prompt tuned)     |
| **Framework**    | LangChain                                     |
| **Embeddings**   | Sentence Transformers (MiniLM)                |
| **Vector Search**| FAISS (Facebook AI Similarity Search)         |
| **Parsing**      | JSON, Regex                                   |
| **Frontend**     | HTML, Tailwind CSS, JavaScript                |

---

## 🌐 Why CliniSense?

- 🧩 **Modular & Scalable**: Easily integrates with EMR systems and other healthcare tools  
- 🧠 **Interpretable AI**: Every diagnosis comes with evidence and reasoning  
- ⏱️ **Time-Saving**: Reduces manual workload for clinicians  
- 🏥 **Healthcare Impact**: Supports better outcomes through data-driven decisions  

---

## 📦 Deployment

CliniSense runs as a Flask-based microservice. You can deploy it on:

- ☁️ Cloud platforms (AWS, GCP, Azure)  
- 🖥️ Local servers for hospital intranets  

---

## 💡 Future Enhancements

- 🔍 OCR prescription reader
- 🧬 Integration with lab results and imaging reports  
- 📊 Dashboard for diagnosis trends and analytics  

---


