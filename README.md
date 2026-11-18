# Report diário de vendas

Projeto para gerar um relatório diário de vendas e disponibilizá-lo no Slack,
com código versionado no GitHub.

## Estado atual

Base de desenvolvimento em Python 3.12 ou superior, sem dependências externas.
O comando inicial verifica a versão do Python e confirma que o projeto pode ser
executado. Ainda não consulta vendas, não envia mensagens e não executa um agente.

## Executar no Windows (PowerShell)

Na pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m report_vendas
```

Não é necessário ativar o ambiente virtual ou alterar a política do PowerShell.
Para novas execuções, use somente a segunda linha.

## Configuração futura

`.env.example` documenta as configurações iniciais previstas. Quando as integrações
forem implementadas, usaremos variáveis de ambiente e, se necessário, um carregador
de `.env`. Atualmente, nenhum arquivo `.env` é carregado.

Credenciais devem ficar apenas no ambiente local ou no gerenciador de segredos da
plataforma de execução. Não inclua tokens, chaves de serviço nem dados reais de
clientes em commits. As pastas locais `data/`, `reports/` e `logs/` são ignoradas pelo Git.

## Fluxo previsto

Fonte de vendas → consulta e validação → cálculo dos indicadores → resumo → Slack.

A fonte de dados, as regras de cálculo, o horário e o comportamento do agente
serão definidos antes de implementar esse fluxo. Veja [o escopo](docs/escopo.md).

## Desenvolvimento

Repositório: https://github.com/lauracgsantos-glitch/report_vendas

Para começar uma alteração após o primeiro commit:

```powershell
git switch -c codex/nome-da-alteracao
git status
```

Adicione dependências ao `pyproject.toml` quando houver uma necessidade concreta.
Adicione testes para os cálculos e integrações conforme forem implementados.
