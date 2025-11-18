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

### References

I have worked Mostly on data chunking Using Semantic chunking which would be more precise but the speech is small so continued with CharacterTextsplitter 
This blog helped a lot: [Advanced Chunking Strategies](https://mer.vin/2024/03/chunking-strategy/)




