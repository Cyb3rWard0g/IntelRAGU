# Intel Retrieval Augmented Generation (RAG) Utilities

## Build Docker Image

```
docker build . -t rag-chroma
```

## Define .ENV File

Add your OpenAI Key for the OpenAI Chat Template

```
OPENAI_API_KEY=XXXXXXXXX
```

## Run Docker Image

```
docker run -it --rm --name rag-chroma --env-file .env -p 8080:8080 rag-chroma
```