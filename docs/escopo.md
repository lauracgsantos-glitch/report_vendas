# Escopo e decisões do projeto

## Objetivo

Produzir um report diário de vendas e entregá-lo no Slack, com código e evolução
mantidos no repositório `report_vendas`.

## Base preparada

- Python 3.12 ou superior.
- Ambiente virtual local em `.venv/`.
- Comando inicial: `python -m report_vendas`.
- Modelo de configuração sem credenciais.
- Exclusão de credenciais, dados locais e relatórios do controle de versão.

## Definições pendentes

- Fonte dos dados: BigQuery, planilha, CRM, API ou outra origem.
- Acesso e estrutura dos dados, preferencialmente com exemplo anonimizado.
- Indicadores: receita, pedidos, ticket médio, metas e comparações desejadas.
- Regras de negócio: status considerados, cancelamentos, devoluções e moeda.
- Período do report: dia anterior ou dia corrente, horário de corte e fuso.
- Workspace e canal de destino no Slack.
- Horário de envio, dias de execução e feriados.
- Agente: somente publicar o resumo ou também responder perguntas no Slack.
- Plataforma de execução e armazenamento de segredos.

## Etapas de implementação

1. Conectar a fonte e validar uma consulta de leitura.
2. Implementar os indicadores com testes das regras de negócio.
3. Gerar uma prévia local do report usando dados autorizados.
4. Integrar a publicação no canal definido e testar o envio quando solicitado.
5. Configurar agendamento, registros de execução e prevenção de envios duplicados.
6. Implementar as interações do agente conforme o comportamento escolhido.

## Critérios de conclusão

- Valores reconciliados com a fonte para uma data de referência.
- Período, fuso e moeda explícitos no report.
- Falhas de consulta não apresentadas como vendas zeradas.
- Publicação no canal e horário acordados.
- Reexecuções sem mensagens duplicadas.
- Credenciais fora do repositório e dos registros de execução.
