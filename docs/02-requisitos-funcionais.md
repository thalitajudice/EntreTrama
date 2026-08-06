# 02 - Requisitos Funcionais

> **Versão:** 1.0  
> **Projeto:** EntreTrama  
> **Autora:** Thalita Judice  
> **Última atualização:** 06/08/2026

---

# Objetivo do Documento

Este documento apresenta os requisitos funcionais do sistema **EntreTrama**, descrevendo todas as funcionalidades necessárias para apoiar a gestão de pequenos negócios artesanais.

Os requisitos foram organizados em módulos, seguindo o fluxo operacional do negócio, desde a aquisição da matéria-prima até a análise dos resultados por meio de dashboards.

As prioridades foram definidas da seguinte forma:

- **Alta:** funcionalidade indispensável para o MVP;
- **Média:** funcionalidade importante, mas que pode ser implementada em uma segunda etapa;
- **Baixa:** funcionalidade prevista para futuras versões do sistema.

---

# Fluxo Geral do Sistema

```text
Compras
      ↓
Materiais
      ↓
Ficha Técnica
      ↓
Produção
      ↓
Produtos
      ↓
Clientes
      ↓
Vendas
      ↓
Financeiro
      ↓
Dashboards
```

---

# 1. Gestão de Materiais

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF001 | O sistema deve permitir cadastrar materiais utilizados na produção artesanal. | Alta |
| RF002 | O sistema deve permitir consultar os materiais cadastrados. | Alta |
| RF003 | O sistema deve permitir editar os dados de um material. | Alta |
| RF004 | O sistema deve permitir desativar um material sem apagar seu histórico. | Média |
| RF005 | O sistema deve registrar a unidade de medida de cada material. | Alta |
| RF006 | O sistema deve registrar a quantidade em estoque de cada material. | Alta |
| RF007 | O sistema deve calcular automaticamente a quantidade disponível considerando materiais reservados para produção. | Alta |
| RF008 | O sistema deve permitir definir um estoque mínimo para cada material. | Média |
| RF009 | O sistema deve identificar materiais abaixo do estoque mínimo. | Média |

---

# 2. Gestão de Fornecedores

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF010 | O sistema deve permitir cadastrar fornecedores. | Alta |
| RF011 | O sistema deve permitir consultar fornecedores cadastrados. | Alta |
| RF012 | O sistema deve permitir editar fornecedores. | Alta |
| RF013 | O sistema deve permitir desativar fornecedores preservando seu histórico. | Média |
| RF014 | O sistema deve permitir consultar o histórico de compras por fornecedor. | Média |

---

# 3. Gestão de Compras

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF015 | O sistema deve permitir registrar compras de materiais. | Alta |
| RF016 | O sistema deve associar uma compra a um fornecedor. | Alta |
| RF017 | O sistema deve permitir registrar diversos materiais em uma mesma compra. | Alta |
| RF018 | O sistema deve registrar quantidade e valor unitário dos itens comprados. | Alta |
| RF019 | O sistema deve calcular automaticamente o valor total da compra. | Alta |
| RF020 | O sistema deve atualizar o estoque após a confirmação da compra. | Alta |
| RF021 | O sistema deve registrar compras à vista ou parceladas. | Alta |
| RF022 | O sistema deve gerar automaticamente as parcelas financeiras de compras parceladas. | Alta |
| RF023 | O sistema deve recalcular automaticamente o custo médio do material após novas compras. | Média |
| RF024 | O sistema deve permitir consultar o histórico de compras. | Alta |

---

# 4. Produtos e Fichas Técnicas

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF025 | O sistema deve permitir cadastrar produtos artesanais. | Alta |
| RF026 | O sistema deve permitir consultar produtos cadastrados. | Alta |
| RF027 | O sistema deve permitir editar produtos. | Alta |
| RF028 | O sistema deve permitir desativar produtos mantendo seu histórico. | Média |
| RF029 | O sistema deve permitir cadastrar fichas técnicas para cada produto. | Alta |
| RF030 | O sistema deve associar materiais à ficha técnica. | Alta |
| RF031 | O sistema deve registrar a quantidade utilizada de cada material. | Alta |
| RF032 | O sistema deve registrar o tempo estimado de produção. | Alta |
| RF033 | O sistema deve calcular automaticamente o custo dos materiais da ficha técnica. | Alta |
| RF034 | O sistema deve permitir registrar custos adicionais de produção. | Média |
| RF035 | O sistema deve calcular automaticamente o custo total do produto. | Alta |
| RF036 | O sistema deve registrar o preço de venda. | Alta |
| RF037 | O sistema deve calcular automaticamente a margem estimada de lucro. | Média |
| RF038 | O sistema deve identificar produtos com ficha técnica incompleta. | Média |

---

# 5. Produção

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF039 | O sistema deve permitir registrar ordens de produção. | Alta |
| RF040 | O sistema deve associar uma ordem de produção a um produto. | Alta |
| RF041 | O sistema deve registrar a quantidade a ser produzida. | Alta |
| RF042 | O sistema deve registrar o prazo da produção. | Alta |
| RF043 | O sistema deve registrar a prioridade da produção. | Média |
| RF044 | O sistema deve atualizar o status da produção. | Alta |
| RF045 | O sistema deve calcular automaticamente os materiais necessários para cada produção. | Alta |
| RF046 | O sistema deve verificar se há materiais suficientes disponíveis para iniciar a produção. | Alta |
| RF047 | O sistema deve reservar automaticamente os materiais ao iniciar uma produção. | Alta |
| RF048 | O sistema deve impedir o início da produção caso não exista material suficiente. | Alta |
| RF049 | O sistema deve liberar os materiais reservados caso a produção seja cancelada. | Média |
| RF050 | O sistema deve registrar o consumo definitivo dos materiais ao concluir a produção. | Alta |
| RF051 | O sistema deve permitir consultar produções pendentes, em andamento e concluídas. | Alta |

---

# 6. Gestão de Clientes

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF052 | O sistema deve permitir cadastrar clientes. | Alta |
| RF053 | O sistema deve permitir consultar clientes cadastrados. | Alta |
| RF054 | O sistema deve permitir editar clientes. | Alta |
| RF055 | O sistema deve consultar o histórico de compras de um cliente. | Média |
| RF056 | O sistema deve permitir desativar clientes preservando seu histórico. | Média |

---

# 7. Gestão de Vendas

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF057 | O sistema deve permitir registrar vendas ou pedidos. | Alta |
| RF058 | O sistema deve associar uma venda a um cliente. | Alta |
| RF059 | O sistema deve permitir registrar diversos produtos em uma mesma venda. | Alta |
| RF060 | O sistema deve calcular automaticamente o valor total da venda. | Alta |
| RF061 | O sistema deve registrar descontos, frete e canal de venda. | Alta |
| RF062 | O sistema deve registrar a forma de pagamento. | Alta |
| RF063 | O sistema deve atualizar o status do pedido. | Alta |
| RF064 | O sistema deve gerar automaticamente uma ordem de produção para produtos sob encomenda. | Alta |
| RF065 | O sistema deve permitir consultar o histórico de vendas. | Alta |
| RF066 | O sistema deve pesquisar produtos durante o registro da venda. | Alta |
| RF067 | O sistema deve permitir cadastrar rapidamente um novo produto durante a venda. | Alta |
| RF068 | O sistema deve permitir continuar a venda após o cadastro do novo produto. | Alta |
| RF069 | O sistema deve alertar sobre produtos com nomes semelhantes. | Média |
| RF070 | O sistema deve identificar produtos cadastrados sem ficha técnica completa. | Média |

---

# 8. Gestão Financeira

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF071 | O sistema deve registrar receitas provenientes das vendas. | Alta |
| RF072 | O sistema deve registrar despesas do negócio. | Alta |
| RF073 | O sistema deve registrar contas a pagar. | Alta |
| RF074 | O sistema deve registrar contas a receber. | Alta |
| RF075 | O sistema deve registrar pagamentos de parcelas. | Alta |
| RF076 | O sistema deve consultar parcelas pagas, pendentes e vencidas. | Alta |
| RF077 | O sistema deve calcular receitas, despesas e saldo por período. | Alta |
| RF078 | O sistema deve permitir categorizar receitas e despesas. | Média |
| RF079 | O sistema deve consultar o fluxo de caixa. | Alta |

---

# 9. Indicadores e Dashboards

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF080 | O sistema deve exibir faturamento por período. | Alta |
| RF081 | O sistema deve exibir receitas, despesas e saldo financeiro. | Alta |
| RF082 | O sistema deve exibir produtos mais vendidos. | Média |
| RF083 | O sistema deve exibir produtos mais lucrativos. | Média |
| RF084 | O sistema deve exibir materiais abaixo do estoque mínimo. | Média |
| RF085 | O sistema deve exibir materiais reservados para produção. | Média |
| RF086 | O sistema deve exibir os materiais mais consumidos. | Média |
| RF087 | O sistema deve exibir a evolução das vendas. | Média |
| RF088 | O sistema deve exibir pedidos por status. | Média |
| RF089 | O sistema deve permitir filtrar indicadores por período. | Alta |

---

# 10. Planejamento de Compras *(Versão Futura)*

| Código | Requisito Funcional | Prioridade |
|---|---|---|
| RF090 | O sistema deve calcular automaticamente a necessidade futura de materiais com base nas ordens de produção em aberto. | Baixa |
| RF091 | O sistema deve identificar materiais insuficientes para atender às produções planejadas. | Baixa |
| RF092 | O sistema deve gerar sugestões automáticas de compra indicando materiais e quantidades necessárias. | Baixa |
| RF093 | O sistema deve permitir transformar uma sugestão de compra em um registro de compra. | Baixa |
| RF094 | O sistema deve permitir consultar o histórico de sugestões de compra. | Baixa |

---

# Observações

Os requisitos funcionais apresentados correspondem ao escopo inicial do projeto e poderão ser refinados durante a modelagem e o desenvolvimento do sistema.

As funcionalidades classificadas com prioridade **Baixa** representam evoluções previstas para versões futuras do EntreTrama e não fazem parte do escopo do MVP.