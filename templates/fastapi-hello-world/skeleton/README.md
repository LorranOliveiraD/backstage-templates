# ${{ values.name }}

${{ values.description }}

## Executar localmente

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- **API:** http://localhost:8000
- **Documentação:** http://localhost:8000/docs

## Executar com Docker

```bash
docker build -t ${{ values.name }} .
docker run -p 8080:8080 ${{ values.name }}
```
