# 07 — Roadmap de desenvolvimento do EntreTrama

> **Versão:** 1.0
> **Projeto:** EntreTrama
> **Autor:** Thalita Judice
> **Última Atualização:** 19/10/2026

## 1. Objetivo

Definir uma sequência viável de implementação do EntreTrama, priorizando funcionalidades que permitam utilizar o sistema na gestão real de um pequeno negócio artesanal antes da conclusão de todos os módulos previstos.

## 2. Escopo e premissas

- Aplicação inicialmente destinada ao uso por uma única pessoa, sem autenticação no MVP.
- Implementação com Python, Streamlit, PostgreSQL e SQLAlchemy; Pandas e Plotly para consultas e indicadores quando necessários.
- Os dados operacionais serão persistidos em banco de dados; não dependerão de planilhas como fonte principal.
- Cada etapa deverá resultar em um fluxo funcional, testável e utilizável.
- A modelagem documentada em `06-modelagem-de-dados.md` orienta a implementação, mas poderá ser refinada quando surgirem necessidades concretas.
- Integrações externas, emissão de notas fiscais e automações com IA ficam fora do MVP inicial.

## 3. Critérios gerais de conclusão

Uma funcionalidade é considerada concluída quando:

1. Pode ser executada pela interface Streamlit, com entradas e mensagens compreensíveis.
2. Persiste e recupera corretamente os dados no PostgreSQL, quando aplicável.
3. Aplica as regras de negócio correspondentes e valida os dados obrigatórios.
4. Foi testada com ao menos um cenário comum e um cenário de erro ou limite.
5. Não compromete registros existentes nem produz movimentos duplicados em operações repetidas.
6. Seu cartão no Trello contém o registro do que foi entregue e das pendências conhecidas.

A conclusão de uma etapa depende dos fluxos descritos em seus critérios específicos, e não apenas da criação das tabelas ou telas.

## 4. Etapas de desenvolvimento

### Etapa 0 — Fundação técnica

**Objetivo:** preparar a base executável da aplicação.

**Entregáveis:**
- Estrutura inicial do repositório e organização dos módulos.
- Ambiente Python e dependências configurados.
- Banco PostgreSQL e conexão SQLAlchemy configurados.
- Estratégia inicial de criação e evolução do esquema definida.
- Aplicação Streamlit executando com navegação mínima e teste de conexão.

**Concluída quando:** a aplicação inicia localmente e consegue registrar e consultar um dado de teste no banco.

### Etapa 1 — MVP operacional: materiais, estoque, compras, vendas e financeiro

**Objetivo:** substituir controles fragmentados nos processos mais urgentes.

**Sequência sugerida:**
1. Materiais, variações e unidades de controle (gramas e unidades).
2. Registro de estoque inicial, consulta de saldos e ajustes manuais auditáveis.
3. Fornecedores e compras com itens, conversão de embalagens, atualização do estoque e custo médio ponderado.
4. Produtos básicos e clientes.
5. Vendas e itens, com valores, descontos, frete e taxas de plataforma quando aplicáveis.
6. Contas a pagar e a receber, vinculadas ou não a compras e vendas.
7. Lançamentos de pagamentos e recebimentos parciais; saldos pendentes calculados.
8. Consultas e indicadores essenciais de estoque e financeiro.

**Entregáveis:** cadastros operacionais, registros de compras e vendas, movimentação de estoque, controle de obrigações e recebimentos, e painel simples.

**Concluída quando:** é possível cadastrar material e estoque inicial, registrar compra com entrada de estoque, cadastrar produto e venda, registrar recebimento parcial, registrar uma despesa e seu pagamento parcial, e consultar os saldos corretos sem recorrer a planilhas externas.

**Limite explícito:** nesta etapa, uma venda pode ser registrada sem que a aplicação gerencie automaticamente a produção, a reserva ou a baixa física de produtos acabados. Essas funções pertencem às etapas posteriores; o sistema deve deixar essa limitação clara.

### Etapa 2 — Produção, personalização e custos

**Objetivo:** conectar modelos de produtos aos materiais efetivamente utilizados.

**Entregáveis:**
- Fichas técnicas com componentes fixos e personalizáveis.
- Seleção de variações de material por componente, inclusive combinação de cores.
- Ordens de produção por configuração e quantidade de unidades idênticas.
- Cálculo de necessidades, compromissos de materiais e custos estimados.
- Baixa física de materiais na conclusão da produção, sem duplicação de movimentos.

**Concluída quando:** uma ordem com configuração definida calcula materiais necessários, registra compromissos, permite acompanhar o status e, ao concluir, reduz o estoque físico e libera os compromissos corretamente.

### Etapa 3 — Produtos acabados, reservas e entregas

**Objetivo:** acompanhar o destino das peças produzidas até a entrega.

**Entregáveis:**
- Lotes de produtos acabados identificados por configuração.
- Controle de quantidade física, reservada e disponível.
- Alocação de peças prontas a vendas e combinação com produção sob encomenda.
- Registro de entregas completas e parciais.
- Baixa do estoque de produtos acabados no envio ou entrega, independente do pagamento.

**Concluída quando:** uma venda pode ser atendida por peças disponíveis, por nova produção ou por ambos, e entregas parciais atualizam reservas e estoque sem inconsistências.

### Evoluções futuras — Fora do escopo inicial

Integração com Shopee e outros marketplaces, múltiplos usuários e autenticação, emissão de notas fiscais, notificações, leitura automática de documentos com IA e previsões de vendas.

## 5. Ordem de execução no Trello

1. Concluir `07-roadmap.md` e `08-arquitetura.md`.
2. Preparar a fundação técnica e configurar PostgreSQL.
3. Implementar os cartões da Etapa 1 em ordem de dependência, trazendo cada um do Backlog para a Sprint Atual quando iniciar.
4. Validar a Etapa 1 com dados reais antes de priorizar as Etapas 2 e 3.
5. Atualizar documentação e modelagem apenas quando mudanças concretas exigirem.

## 6. Gestão de mudanças

O Roadmap expressa a ordem planejada, não um cronograma com datas fixas. Prioridades podem mudar diante de problemas encontrados no uso real. Mudanças que afetem escopo ou regras de negócio devem ser registradas no Trello e refletidas nos documentos relevantes, sem interromper o desenvolvimento por ajustes exclusivamente estéticos.
