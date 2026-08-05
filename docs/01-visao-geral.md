# 01 - Visão Geral 

> **Versão:** 1.0
> **Projeto:** EntreTrama
> **Autor:** Thalita Judice
> **Última Atualização:** 05/08/2026

---

## Objetivo do Documento

Este documento apresenta uma visão geral do projeto EntreTrama, contextulizando o problema, a solução proposta, o público alvo, os objetivos e o escopo inicial do sistema. 

---

# Sobre o Projeto

O **EntreTrama** é um sistema de informação integrado desenvolvido para atender às necessidades de gestão de pequenos negócios artesanais.

Diferentemente de sistemas comerciais tradicionais, o EntreTrama foi concebido considerando as particularidades da produção artesanal, onde cada produto possui uma ficha técnica composta por materiais, quantidades, tempo de produção e custo de fabricação.

O sistema busca centralizar informações de produção, materiais, compras, vendas, clientes e financeiro em uma única plataforma, permitindo que o artesão acompanhe todo o ciclo do produto, desde a aquisição da matéria-prima até a venda ao cliente final.

Além da organização operacional, o EntreTrama fornecerá indicadores e dashboards que auxiliam o empreendedor na tomada de decisões e no planejamento do negócio.

---

# Contexto

Grande parte dos artesãos administra seu negócio utilizando diversas planilhas independentes para controlar materiais, custos, produção, vendas e fluxo financeiro.

Embora esse método funcione durante as primeiras vendas, ele se torna cada vez mais complexo conforme o negócio cresce, dificultando a organização das informações, o cálculo correto dos custos, o controle de estoque de materiais e o acompanhamento da produção.

Além disso, a maioria dos sistemas de gestão disponíveis no mercado foi desenvolvida para empresas comerciais tradicionais e não contempla necessidades específicas da produção artesanal, como o controle de receitas, consumo de materiais por produto e cálculo automático do custo de fabricação.

---

# Problema

Pequenos negócios artesanais enfrentam dificuldades para controlar de forma integrada todas as etapas da produção e gestão do negócio.

A utilização de múltiplas planilhas aumenta a possibilidade de erros, dificulta o controle de materiais, torna o cálculo dos custos mais trabalhoso e reduz a capacidade do empreendedor de acompanhar indicadores importantes para a tomada de decisão.

---

# Solução Proposta

O EntreTrama propõe o desenvolvimento de um sistema de informação integrado voltado especificamente para a gestão de pequenos negócios artesanais.

O sistema permitirá cadastrar materiais, fornecedores, fichas técnicas dos produtos, compras, produção, clientes, vendas e informações financeiras em um único banco de dados.

A partir dessas informações, será possível calcular automaticamente os custos de produção, acompanhar o consumo de materiais, controlar o andamento da produção e disponibilizar dashboards com indicadores estratégicos do negócio.

---

# Público-Alvo

O EntreTrama é destinado principalmente a:

- Artesãos;
- Pequenos ateliês;
- Microempreendedores Individuais (MEI);
- Negócios que trabalham com produtos feitos sob encomenda;
- Pequenos fabricantes de produtos artesanais.

---

# Objetivo Geral

Desenvolver um sistema de informação integrado para apoiar a gestão de pequenos negócios artesanais, centralizando informações operacionais e fornecendo indicadores que auxiliem a tomada de decisão.

---

# Objetivos Específicos

- Centralizar os dados do negócio em uma única plataforma;
- Gerenciar materiais, fornecedores e compras;
- Controlar fichas técnicas dos produtos artesanais;
- Automatizar o cálculo do custo de produção;
- Gerenciar clientes, pedidos e vendas;
- Organizar o controle financeiro;
- Disponibilizar dashboards para acompanhamento do desempenho do negócio;
- Reduzir a dependência de planilhas eletrônicas.

---

# Escopo do MVP

A primeira versão do EntreTrama contemplará os seguintes módulos:

- Cadastro de Materiais;
- Cadastro de Fornecedores;
- Cadastro de Produtos;
- Cadastro de Fichas Técnicas;
- Controle de Compras;
- Controle de Produção;
- Cadastro de Clientes;
- Controle de Vendas;
- Controle Financeiro;
- Dashboard Executivo;
- Dashboard Financeiro;
- Dashboard Comercial.

---

# Funcionalidades Futuras

As funcionalidades abaixo não fazem parte do MVP, mas poderão ser implementadas em versões futuras:

- Leitura automática de notas fiscais e cupons por Inteligência Artificial (OCR);
- Cadastro automático de materiais a partir de notas fiscais;
- Controle de múltiplos usuários;
- Aplicativo mobile;
- Integração com marketplaces (Shopee, Elo7 e outros);
- Controle de metas e indicadores personalizados;
- Previsão de vendas utilizando Inteligência Artificial;
- Sugestão automática de compras de materiais com base no estoque e na produção prevista.

---

# Tecnologias Previstas

- Python
- Streamlit
- PostgreSQL
- SQLAlchemy
- Pandas
- Plotly
- Git
- GitHub