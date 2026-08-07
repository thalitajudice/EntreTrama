# 03 - Requisitos Não Funcionais

> **Versão:** 1.0  
> **Projeto:** EntreTrama  
> **Autora:** Thalita Judice  
> **Última atualização:** 06/08/2026

---

# Objetivo do Documento

Este documento apresenta os requisitos não funcionais do sistema **EntreTrama**, especificando as características de qualidade que deverão ser atendidas durante o desenvolvimento da aplicação.

Os requisitos estão organizados por categorias, contemplando aspectos como usabilidade, desempenho, segurança, confiabilidade, manutenibilidade, portabilidade e escalabilidade.

---

# 1. Usabilidade

| Código | Requisito Não Funcional |
|---|---|
| RNF001 | O sistema deverá possuir uma interface simples, intuitiva e de fácil utilização. |
| RNF002 | O sistema deverá manter um padrão visual em todas as telas. |
| RNF003 | As principais operações deverão ser executadas com o menor número possível de interações. |
| RNF004 | O sistema deverá apresentar mensagens claras para erros e confirmações de operações. |
| RNF005 | O sistema deverá permitir navegação entre os módulos sem perda das informações já preenchidas. |

---

# 2. Desempenho

| Código | Requisito Não Funcional |
|---|---|
| RNF006 | As consultas simples deverão ser respondidas em até 2 segundos. |
| RNF007 | Os dashboards deverão ser carregados em até 5 segundos. |
| RNF008 | O sistema deverá suportar centenas de registros sem perda perceptível de desempenho. |

---
# 3. Segurança e Proteção de Dados

| Código | Requisito Não Funcional |
|---|---|
| RNF009 | O sistema deverá impedir a publicação de credenciais e informações sensíveis no repositório do GitHub. |
| RNF010 | As credenciais de acesso ao banco de dados deverão ser armazenadas em variáveis de ambiente. |
| RNF011 | Os dados reais de clientes não deverão ser disponibilizados publicamente no repositório. |
| RNF012 | O sistema deverá solicitar confirmação antes de excluir ou cancelar registros importantes. |

---

# 4. Confiabilidade

| Código | Requisito Não Funcional |
|---|---|
| RNF013 | O sistema deverá garantir a integridade das informações armazenadas. |
| RNF014 | O sistema deverá evitar perda de dados durante operações críticas. |
| RNF015 | O sistema deverá registrar erros relevantes para facilitar futuras correções. |

---

# 5. Manutenibilidade

| Código | Requisito Não Funcional |
|---|---|
| RNF015 | O sistema deverá possuir código organizado e modular. |
| RNF016 | O sistema deverá seguir boas práticas de desenvolvimento em Python. |
| RNF017 | O projeto deverá possuir documentação técnica atualizada. |

---

# 6. Portabilidade

| Código | Requisito Não Funcional |
|---|---|
| RNF018 | O sistema deverá ser executado em ambiente Windows. |
| RNF019 | O sistema deverá ser acessado por navegador web. |
| RNF020 | O banco de dados deverá utilizar PostgreSQL. |

---

# 7. Escalabilidade

| Código | Requisito Não Funcional |
|---|---|
| RNF021 | O sistema deverá permitir a inclusão de novos módulos sem necessidade de reestruturação completa. |
| RNF022 | O banco de dados deverá suportar o crescimento do volume de informações do negócio. |

---

# 8. Tecnologias

| Código | Requisito Não Funcional |
|---|---|
| RNF023 | A aplicação deverá ser desenvolvida utilizando Python. |
| RNF024 | A interface deverá ser desenvolvida utilizando Streamlit. |
| RNF025 | O acesso ao banco deverá utilizar SQLAlchemy. |
| RNF026 | Os dashboards deverão utilizar Plotly. |
| RNF027 | O versionamento deverá ser realizado utilizando Git e GitHub. |

---

# Observações

Os requisitos não funcionais apresentados correspondem às características técnicas esperadas para o desenvolvimento do EntreTrama e poderão ser refinados conforme a evolução do projeto.