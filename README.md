# Backstage Templates

Templates para o Backstage. O template FastAPI aparece em `/create` e permite criar novos serviços com um clique.

## Template FastAPI Hello World

O usuário preenche um formulário com **nome do serviço**, **descrição** e **dono**, e o Backstage:

1. Copia o projeto base FastAPI "Hello World"
2. Substitui os nomes nos arquivos
3. Cria o repositório no GitHub
4. Adiciona o `catalog-info.yaml`
5. Registra automaticamente o novo serviço no catálogo

### Projeto base

- `app = FastAPI()` com título e descrição dinâmicos
- `GET /` retornando `{"message": "Hello World"}`
- Documentação automática em `/docs`
- **Dockerfile** pronto para deploy

## Como usar

### 1. Registrar no Backstage (via config — mais usado em empresa)

Adicione no `app-config.yaml`:

```yaml
catalog:
  locations:
    - type: url
      target: https://github.com/LorranOliveiraD/backstage-templates/blob/main/templates/fastapi-hello-world/template.yaml
      rules:
        - allow:
            - Template
```

**Depois reinicie o Backstage.**

Ou via UI: **Create** → **Register Existing Component** → cole a URL acima.

### 2. Configuração necessária

- **GitHub integration:** Token no `app-config.yaml` para criar repositórios
- **OwnerPicker:** Groups/Users no catálogo para o campo "Dono"
- **Owner do template:** Ajuste `spec.owner` para `group:default/seu-time` se necessário
- **Integrations:** `github.com` em `integrations.github`

### 3. Fluxo do usuário

1. Acesse `/create` no Backstage
2. Selecione "FastAPI Hello World"
3. Preencha: Nome (apenas `a-z`, `0-9`, `-`), Descrição, Dono, Repositório
4. Clique em **Create**
5. Serviço criado, publicado e registrado no catálogo

## Estrutura (padrão de empresa)

```
backstage-templates/
├── templates/
│   └── fastapi-hello-world/
│       ├── template.yaml      # Definição do template
│       └── skeleton/          # Projeto base copiado
│           ├── app/
│           │   ├── __init__.py
│           │   └── main.py
│           ├── requirements.txt
│           ├── catalog-info.yaml
│           ├── Dockerfile
│           ├── .dockerignore
│           ├── README.md
│           └── .gitignore
└── README.md
```

## URL do repositório

```
https://github.com/LorranOliveiraD/backstage-templates.git
```
