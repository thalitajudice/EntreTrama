# 🧶 EntreTrama

> Sistema de Informação Integrado para Apoio à Gestão de Pequenos Negócios Artesanais.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-F4B400)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791)
![License](https://img.shields.io/badge/license-MIT-green)

---

# 📖 Sobre o projeto

O **EntreTrama** é um sistema de informação desenvolvido especificamente para atender às necessidades de gestão de pequenos negócios artesanais.

Diferentemente de sistemas de gestão tradicionais, o EntreTrama foi concebido considerando as particularidades da produção artesanal, como o controle de materiais, fichas técnicas, custos de produção, produção sob encomenda e gestão financeira.

O projeto nasceu da necessidade de substituir diversas planilhas utilizadas no controle diário por uma única plataforma capaz de integrar todas as etapas do negócio, desde a compra da matéria-prima até a venda do produto final.

Além da gestão operacional, o sistema disponibilizará dashboards e indicadores para apoiar a tomada de decisão, permitindo que o empreendedor acompanhe a saúde financeira, produtiva e comercial do negócio.

Este projeto está sendo desenvolvido como Trabalho de Conclusão de Curso (TCC) do curso de **Gestão da Informação** da Universidade Federal de Uberlândia (UFU).

---

# 🎯 Objetivos

- Centralizar todas as informações do negócio em uma única plataforma;
- Gerenciar materiais, fornecedores e fichas técnicas;
- Automatizar o cálculo dos custos de produção;
- Controlar compras, produção, estoque, vendas e financeiro;
- Disponibilizar indicadores e dashboards para apoio à tomada de decisão;
- Reduzir a dependência de planilhas eletrônicas.

---

# ✨ Principais Funcionalidades

## 🧶 Gestão de Materiais

- Cadastro de materiais
- Controle de estoque
- Movimentações
- Estoque mínimo
- Fornecedores

### 📋 Fichas Técnicas

- Cadastro de fichas técnicas
- Materiais utilizados
- Quantidade de cada material
- Tempo estimado de produção
- Cálculo automático do custo

### 🏭 Produção

- Ordens de produção
- Status de produção
- Prioridades
- Consumo de materiais
- Controle de prazos

### 📦 Produtos

- Cadastro de produtos
- Categorias
- Precificação
- Custos
- Tempo de produção

### 👥 Clientes

- Cadastro de clientes
- Histórico de pedidos
- Dados de contato

### 🛒 Vendas

- Registro de vendas
- Itens da venda
- Forma de pagamento
- Canal de venda
- Status do pedido

### 💰 Financeiro

- Receitas
- Despesas
- Compras
- Parcelamentos
- Contas a pagar
- Contas a receber
- Fluxo de caixa

### 📊 Business Intelligence

- Dashboard Executivo
- Dashboard Financeiro
- Dashboard Comercial
- Dashboard de Produção
- Custos de produção
- Produtos mais lucrativos
- Curva ABC
- Giro de estoque
- Evolução das vendas

---

# 🛠️ Tecnologias

- Python
- PostgreSQL
- SQLAlchemy
- Streamlit
- Pandas
- Plotly
- Git
- GitHub

---

# 🏗️ Arquitetura

```text
Usuário
      │
      ▼
Interface Web (Streamlit)
      │
      ▼
Camada de Serviços (Python)
      │
      ▼
Banco de Dados (PostgreSQL)
      │
      ▼
Dashboards e Indicadores
```

---

# 📂 Estrutura do Projeto

```text
EntreTrama/
│
├── docs/
├── src/
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# 🚀 Status do Projeto

🚧 Em desenvolvimento

Atualmente o projeto encontra-se na fase de levantamento de requisitos, modelagem do banco de dados e documentação.

O desenvolvimento seguirá a seguinte ordem:

- Documentação
- Banco de Dados
- Backend
- Interface
- Dashboards

---

# 🌱 Evoluções Futuras

Algumas funcionalidades planejadas para versões futuras:

- Leitura automática de notas fiscais e cupons utilizando Inteligência Artificial (OCR);
- Cadastro automático de materiais a partir de notas fiscais;
- Integração com marketplaces (Shopee, Elo7 e outros);
- Aplicativo mobile;
- Controle de múltiplos usuários;
- Planejamento da produção;
- Sugestão automática de compras de materiais;
- Previsão de vendas utilizando Inteligência Artificial.

---

# 📚 Documentação

Toda a documentação técnica do projeto encontra-se na pasta `docs`.

- Visão Geral
- Requisitos Funcionais
- Requisitos Não Funcionais
- Regras de Negócio
- Casos de Uso
- Modelagem
- Arquitetura
- Roadmap

---

# 👩‍💻 Desenvolvido por

**Thalita Judice**

Graduanda em Gestão da Informação — Universidade Federal de Uberlândia (UFU)

Projeto desenvolvido como Trabalho de Conclusão de Curso (TCC).