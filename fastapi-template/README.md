# Template FastAPI Hello World para Backstage

Template que aparece em `/create` no Backstage. O usuário preenche um formulário com **nome do serviço**, **descrição** e **dono**, e o Backstage:

1. Copia o projeto base FastAPI "Hello World"
2. Substitui os nomes nos arquivos
3. Cria o repositório no GitHub
4. Adiciona o `catalog-info.yaml`
5. Registra automaticamente o novo serviço no catálogo

## Projeto base FastAPI

- `app = FastAPI()` com título e descrição dinâmicos
- `GET /` retornando `{"message": "Hello World"}`
- Documentação automática em `/docs`

## Como usar

### 1. Publicar o template em um repositório

Faça push deste diretório para o repositório: `https://github.com/LorranOliveiraD/backstage-templates.git`

### 2. Registrar no Backstage

Adicione a localização do template no `app-config.yaml` do seu Backstage:

```yaml
catalog:
  locations:
    - type: url
      target: https://github.com/LorranOliveiraD/backstage-templates/blob/main/fastapi-template/templates/fastapi-hello-world/template.yaml
      rules:
        - allow:
            - kind: Template
```

Ou registre via UI: **Create** → **Register Existing Component** → cole a URL do `templates/fastapi-hello-world/template.yaml`.

### 3. Configuração necessária

- **GitHub integration:** Configure o token no `app-config.yaml` para criar repositórios
- **OwnerPicker:** Certifique-se de ter Groups/Users no catálogo para o campo "Dono"
- **Owner do template:** O `spec.owner` está como `team-platform`. Ajuste para `group:default/seu-time` ou `user:default/guest` se não existir no catálogo
- **Integrations:** Adicione `github.com` em `integrations.github`

### 4. Fluxo do usuário

1. Acesse `/create` no Backstage
2. Selecione "FastAPI Hello World"
3. Preencha: Nome, Descrição, Dono
4. Escolha o local do repositório no GitHub
5. Clique em **Create**
6. O serviço será criado, publicado e registrado no catálogo

## Estrutura

```
fastapi-template/
├── templates/
│   └── fastapi-hello-world/
│       ├── template.yaml      # Definição do template (formulário + steps)
│       └── skeleton/          # Projeto base copiado
│           ├── app/
│           │   ├── __init__.py
│           │   └── main.py    # FastAPI Hello World
│           ├── requirements.txt
│           ├── catalog-info.yaml
│           ├── README.md
│           └── .gitignore
└── README.md
```
