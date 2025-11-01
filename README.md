🩺 CliniSense
AI-Powered Clinical Note Summarizer & Diagnostic Assistant

CliniSense is a next-generation diagnostic support system that leverages OpenAI's large language model (LLM) and semantic retrieval pipelines to convert unstructured clinical narratives into structured, actionable insights.
Powered by a LangChain-based architecture, the system integrates:

HuggingFace MiniLM embeddings for high-dimensional semantic representation of clinical notes.
FAISS vector search for context-aware retrieval of the most relevant evidence chunks.
Prompt-tuned OpenAI GPT-4o-mini as the core reasoning engine, optimized for factual summarization and differential diagnosis generation.


🚀 Features
✅ Converts long and messy clinical notes into clear summaries
✅ Suggests top probable diagnoses with confidence levels (High / Medium / Low)
✅ Provides justification for each diagnosis, backed by cited evidence from the input text
✅ Ensures structured, readable, and factual medical output

⚙️ Tech Stacks
🔵Python for backend
🔵LLM: 	OpenAI GPT-4o-mini (with medical prompt tuning)
🔵LangChain framework
🔵Embeddings	Sentence Transformers (MiniLM)
🔵Vector Search	FAISS (Facebook AI Similarity Search)
🔵Parsin & output: JSON, Regex
🔵Flask for backend and deployment
🔵HTML, Tailwind CSS and JS for frontend


The workflow involves recursive text chunking, embedding, and semantic retrieval to ensure fine-grained contextual understanding. Retrieved evidence is passed through a structured medical prompt, yielding:

1. Factual clinical summaries 
2. Prioritized differential diagnoses with
   * Confidence levels (High / Medium / Low)
   * Short clinical justifications
  


CliniSense enforces structured JSON reasoning, then post-processes results into human-readable medical text, ensuring best explanation and interpretation with EMR systems.

This architecture delivers high interpretability, reduces diagnostic workload, and enables data-driven clinical decision support, contributing to the welfare of public healthcare
     
