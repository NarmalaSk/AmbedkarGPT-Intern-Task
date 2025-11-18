### QA Rag Pipeline 
A Simple Rag Pipeline Using Langchain and chromavectordb , Ollama ,HuggingFace Embedding Models

### Prequesites

Python v3.8
Ollama Mistral Model
HuggingFace all-MiniLM-L6-v2 

### Setup and Installation
Clone Repository
```
git clone https://github.com/NarmalaSk/AmbedkarGPT-Intern-Task.git
```

Create virtual env  and Install Requirements.txt
```
python -m venv env
source /env/bin/activate

pip install -r requirements.txt
```

Pull Ollama Model 
```
ollama pull mistral
```

### Run Q & A System



```
python3 main.py LLM_query text_file
```




