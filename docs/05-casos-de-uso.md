
# 05 - Casos de Uso

> **Versão:** 1.0  
> **Projeto:** EntreTrama  
> **Autora:** Thalita Judice  
> **Última atualização:** 24/09/2026

---

## Objetivo do documento

Este documento apresenta os principais casos de uso do sistema EntreTrama, descrevendo as interações entre o usuário e a aplicação para execução dos processos relacionados à gestão de pequenos negócios artesanais.

Os casos de uso foram definidos a partir dos requisitos funcionais e das regras de negócio estabelecidos anteriormente, considerando o escopo inicial do Produto Mínimo Viável (MVP).

O documento busca orientar as etapas de modelagem, implementação e validação das funcionalidades do sistema.

---

## 1. Identificação dos atores

### Ator principal: Usuário

Representa a pessoa responsável pela gestão do negócio artesanal.

No MVP, o EntreTrama será utilizado individualmente, sem necessidade de autenticação ou diferenciação entre perfis de acesso.

O usuário poderá executar operações relacionadas a materiais, estoque, fornecedores, compras, produtos, fichas técnicas, clientes, vendas, produção e financeiro.

A possibilidade de múltiplos usuários e diferentes níveis de permissão está prevista como evolução futura.

---

## 2. Relação dos casos de uso

| Código | Caso de uso | Módulo |
|---|---|---|
| UC001 | Gerenciar materiais | Materiais e estoque |
| UC002 | Ajustar estoque | Materiais e estoque |
| UC003 | Gerenciar fornecedores | Fornecedores |
| UC004 | Registrar compra de materiais | Compras |
| UC005 | Gerenciar produtos | Produtos |
| UC006 | Elaborar ficha técnica | Produtos e fichas técnicas |
| UC007 | Gerenciar clientes | Clientes |
| UC008 | Registrar venda ou pedido | Vendas |
| UC009 | Gerenciar ordem de produção | Produção |
| UC010 | Registrar movimentação financeira | Financeiro |
| UC011 | Consultar fluxo de caixa | Financeiro |
| UC012 | Consultar indicadores e dashboards | Indicadores |

---

# 3. Especificação dos casos de uso

## UC001 - Gerenciar materiais

**Ator:** Usuário

**Objetivo:** Permitir o cadastro, a consulta e a atualização dos materiais utilizados na produção artesanal.

### Pré-condições

- O sistema deve estar disponível para utilização.

### Fluxo principal

1. O usuário acessa o módulo de materiais.
2. O sistema apresenta os materiais cadastrados.
3. O usuário seleciona a opção de cadastrar um novo material.
4. O sistema apresenta o formulário de cadastro.
5. O usuário informa os dados do material, incluindo nome, categoria, unidade de medida e demais informações disponíveis.
6. O usuário confirma o cadastro.
7. O sistema valida os dados informados.
8. O sistema registra o material.
9. O sistema apresenta uma mensagem de confirmação.

### Fluxos alternativos

**FA01 - Consultar material**

O usuário seleciona um material existente e consulta suas informações, incluindo estoque físico, quantidade comprometida, quantidade disponível e custo médio.

**FA02 - Editar material**

O usuário seleciona um material cadastrado, altera suas informações e confirma a atualização.

**FA03 - Material sem estoque**

O usuário pode cadastrar um material com quantidade inicial igual a zero, mesmo que ele ainda não tenha sido adquirido.

**FA04 - Desativar material**

O usuário pode desativar um material sem excluir seu histórico de compras e movimentações.

### Pós-condições

- O material permanece registrado ou atualizado no sistema.
- As informações ficam disponíveis para utilização em compras e fichas técnicas.

---

## UC002 - Ajustar estoque

**Ator:** Usuário

**Objetivo:** Corrigir diferenças entre a quantidade física de um material e a quantidade registrada no sistema.

### Pré-condições

- O material deve estar cadastrado.

### Fluxo principal

1. O usuário acessa o módulo de materiais.
2. O usuário seleciona o material desejado.
3. O sistema apresenta as informações atuais de estoque.
4. O usuário seleciona a opção de ajuste de estoque.
5. O usuário informa a quantidade que deseja adicionar ou retirar.
6. O usuário informa o motivo do ajuste.
7. O sistema apresenta a quantidade resultante.
8. O usuário confirma a operação.
9. O sistema registra a movimentação.
10. O sistema atualiza o estoque físico e recalcula a quantidade disponível.

### Fluxos alternativos

**FA01 - Ajuste positivo**

O usuário registra uma quantidade adicional identificada durante a conferência do estoque.

**FA02 - Ajuste negativo**

O usuário registra uma redução decorrente de consumo adicional, perda, avaria ou divergência de contagem.

**FA03 - Estoque disponível negativo**

O ajuste pode resultar em quantidade disponível negativa, indicando que os materiais comprometidos com produções superam o estoque físico registrado.

### Pós-condições

- O estoque físico é atualizado.
- O ajuste permanece registrado no histórico de movimentações.
- A quantidade disponível é recalculada considerando os compromissos existentes.

---

## UC003 - Gerenciar fornecedores

**Ator:** Usuário

**Objetivo:** Manter informações dos fornecedores utilizados pelo negócio artesanal.

### Pré-condições

- O sistema deve estar disponível.

### Fluxo principal

1. O usuário acessa o módulo de fornecedores.
2. O sistema apresenta os fornecedores cadastrados.
3. O usuário seleciona a opção de novo fornecedor.
4. O sistema apresenta o formulário.
5. O usuário informa os dados disponíveis.
6. O usuário confirma o cadastro.
7. O sistema registra o fornecedor.

### Fluxos alternativos

**FA01 - Editar fornecedor**

O usuário altera informações de um fornecedor existente.

**FA02 - Consultar histórico**

O usuário consulta as compras relacionadas ao fornecedor.

**FA03 - Desativar fornecedor**

O usuário desativa um fornecedor sem excluir o histórico de compras associado.

### Pós-condições

- As informações do fornecedor permanecem disponíveis para associação às compras.

---

## UC004 - Registrar compra de materiais

**Ator:** Usuário

**Objetivo:** Registrar a aquisição de materiais, atualizar o estoque e gerar os registros financeiros correspondentes.

### Pré-condições

- Os materiais adquiridos devem estar cadastrados.
- O usuário deve possuir as informações necessárias para registrar a compra.

### Fluxo principal

1. O usuário acessa o módulo de compras.
2. O usuário seleciona a opção de registrar nova compra.
3. O sistema apresenta o formulário.
4. O usuário informa a data da compra.
5. O usuário seleciona o fornecedor, quando aplicável.
6. O usuário adiciona os materiais adquiridos.
7. O usuário informa a quantidade e o valor unitário de cada material.
8. O sistema calcula o valor de cada item.
9. O usuário informa eventuais descontos e frete.
10. O sistema calcula o valor total da compra.
11. O usuário informa a forma e as condições de pagamento.
12. O usuário confirma a compra.
13. O sistema registra os itens adquiridos.
14. O sistema atualiza o estoque dos materiais.
15. O sistema recalcula o custo médio dos materiais adquiridos.
16. O sistema gera os registros financeiros correspondentes.

### Fluxos alternativos

**FA01 - Compra parcelada**

O usuário informa a quantidade de parcelas, os valores e os vencimentos. O sistema gera as contas a pagar correspondentes.

**FA02 - Compra à vista**

O sistema registra o pagamento conforme a data informada.

**FA03 - Compra sem fornecedor identificado**

O usuário registra a compra sem associá-la a um fornecedor.

**FA04 - Material não cadastrado**

O usuário deve cadastrar o material antes de incluí-lo na compra.

### Pós-condições

- A compra permanece registrada.
- O estoque físico é atualizado.
- O custo médio dos materiais é recalculado.
- As obrigações financeiras correspondentes são registradas.

---

## UC005 - Gerenciar produtos

**Ator:** Usuário

**Objetivo:** Cadastrar e manter os produtos artesanais comercializados pelo negócio.

### Pré-condições

- O sistema deve estar disponível.

### Fluxo principal

1. O usuário acessa o módulo de produtos.
2. O sistema apresenta os produtos cadastrados.
3. O usuário seleciona a opção de novo produto.
4. O usuário informa nome, categoria, preço de venda e tipo de produção.
5. O usuário confirma o cadastro.
6. O sistema valida as informações.
7. O sistema registra o produto.

### Fluxos alternativos

**FA01 - Cadastro rápido**

O usuário cadastra um produto durante o registro de uma venda, sem interromper a operação comercial.

**FA02 - Ficha técnica pendente**

O produto pode ser registrado sem ficha técnica completa, permanecendo identificado como "Ficha Técnica Pendente".

**FA03 - Editar produto**

O usuário altera informações de um produto existente.

**FA04 - Desativar produto**

O usuário desativa um produto, preservando seu histórico de vendas e produções.

### Pós-condições

- O produto permanece disponível para utilização nas operações do sistema.
- Produtos sem ficha técnica completa permanecem identificados como pendentes.

---

## UC006 - Elaborar ficha técnica

**Ator:** Usuário

**Objetivo:** Definir os materiais, as quantidades estimadas, o tempo de trabalho e os custos necessários para produzir uma unidade de determinado produto artesanal.

### Pré-condições

- O produto deve estar cadastrado.
- Os materiais utilizados devem estar cadastrados.

### Fluxo principal

1. O usuário acessa o cadastro de um produto.
2. O usuário seleciona a opção de ficha técnica.
3. O sistema apresenta os campos de composição do produto.
4. O usuário adiciona os componentes e materiais utilizados na produção.
5. O usuário informa as quantidades estimadas de consumo e identifica quais componentes admitem personalização de material, cor ou acabamento.
6. O usuário informa o tempo estimado de produção.
7. O sistema consulta o custo médio dos materiais.
8. O sistema calcula o custo estimado dos materiais.
9. O sistema calcula o custo estimado de mão de obra com base no valor da hora de trabalho.
10. O sistema considera os demais custos de produção informados.
11. O sistema calcula o custo total estimado do produto.
12. O usuário revisa as informações.
13. O usuário confirma a ficha técnica.
14. O sistema registra as informações.

### Fluxos alternativos

**FA01 - Consumo por proporção**

O usuário informa a quantidade total estimada de um grupo de materiais e distribui esse consumo entre diferentes materiais por meio de percentuais.

**FA02 - Margem adicional de consumo**

O usuário define uma margem percentual para materiais sujeitos a variações de consumo durante a produção.

**FA03 - Conversão de unidades**

O sistema converte a quantidade utilizada para uma unidade compatível com a unidade de referência do material.

**FA04 - Alteração da ficha técnica**

O usuário modifica materiais, quantidades ou tempo estimado de produção. O sistema recalcula o custo estimado do produto.

**FA05 - Ficha técnica incompleta**

O usuário mantém o produto identificado como "Ficha Técnica Pendente" até que as informações necessárias sejam preenchidas.

**FA06 - Componente personalizável**

O usuário identifica um componente da ficha técnica como personalizável e define os materiais ou variações compatíveis que poderão ser selecionados em cada produção.

A ficha técnica mantém a quantidade estimada de consumo do componente, sem exigir a criação de um novo produto para cada combinação possível.

### Pós-condições

- A ficha técnica permanece registrada.
- O custo estimado do produto é atualizado quando houver informações suficientes.
- A ficha técnica pode ser utilizada no planejamento das ordens de produção.

---

## UC007 - Gerenciar clientes

**Ator:** Usuário

**Objetivo:** Manter o cadastro e o histórico comercial dos clientes.

### Pré-condições

- O sistema deve estar disponível.

### Fluxo principal

1. O usuário acessa o módulo de clientes.
2. O sistema apresenta os clientes cadastrados.
3. O usuário seleciona a opção de novo cliente.
4. O usuário informa os dados disponíveis.
5. O usuário confirma o cadastro.
6. O sistema registra o cliente.

### Fluxos alternativos

**FA01 - Consultar histórico**

O usuário consulta vendas e pedidos associados ao cliente.

**FA02 - Editar cliente**

O usuário atualiza as informações cadastradas.

**FA03 - Desativar cliente**

O usuário desativa o cadastro, preservando o histórico comercial.

### Pós-condições

- As informações do cliente permanecem disponíveis para associação às vendas e aos pedidos.

---

## UC008 - Registrar venda ou pedido

**Ator:** Usuário

**Objetivo:** Registrar a comercialização de produtos artesanais e, quando necessário, gerar demandas de produção.

### Pré-condições

- O sistema deve estar disponível.
- Os produtos devem estar cadastrados ou poderão ser cadastrados durante a operação.

### Fluxo principal

1. O usuário acessa o módulo de vendas.
2. O usuário seleciona a opção de nova venda.
3. O sistema apresenta o formulário.
4. O usuário informa o cliente, quando aplicável.
5. O usuário seleciona o canal de venda.
6. O usuário adiciona os produtos.
7. O usuário informa a quantidade e o preço praticado de cada item.
8. O sistema calcula o subtotal.
9. O usuário informa descontos e frete, quando aplicável.
10. O sistema calcula o valor total da venda.
11. O usuário informa as condições de pagamento.
12. O usuário confirma a operação.
13. O sistema registra a venda e seus itens.
14. O sistema gera os registros financeiros correspondentes.
15. Quando houver produtos sob encomenda, o sistema gera as necessidades de produção vinculadas ao pedido.

### Fluxos alternativos

**FA01 - Produto não cadastrado**

O usuário inicia o cadastro rápido do produto e retorna à venda sem perder as informações preenchidas.

**FA02 - Venda sem cliente identificado**

O usuário registra a venda sem associar um cliente.

**FA03 - Pagamento parcial**

O usuário informa o valor recebido e o sistema mantém registrado o saldo a receber.

**FA04 - Pagamento parcelado**

O usuário informa as condições de parcelamento e o sistema gera as contas a receber.

**FA05 - Produto para pronta entrega**

O produto é incluído na venda sem gerar automaticamente uma nova ordem de produção.

### Pós-condições

- A venda permanece registrada.
- Os valores praticados são preservados historicamente.
- As informações financeiras são registradas.
- As necessidades de produção são geradas quando aplicável.

---

## UC009 - Gerenciar ordem de produção

**Ator:** Usuário

**Objetivo:** Planejar, acompanhar e registrar a produção de peças artesanais.

### Pré-condições

- O produto deve estar cadastrado.
- Para calcular a necessidade de materiais e registrar seu comprometimento, a ficha técnica deve possuir informações suficientes.
- Os materiais ou variações selecionados para os componentes personalizáveis devem estar cadastrados.

### Fluxo principal

1. O usuário acessa o módulo de produção.
2. O usuário seleciona uma ordem existente ou registra uma nova ordem.
3. O usuário informa o produto e a quantidade a produzir.
4. O usuário informa o prazo previsto.
5. O sistema calcula os materiais necessários com base na ficha técnica.
6. O sistema verifica a disponibilidade dos materiais.
7. O sistema registra o comprometimento previsto dos materiais.
8. O sistema identifica o status inicial da produção.
9. O usuário acompanha a ordem de produção.
10. O usuário registra o início da produção.
11. O sistema altera o status para "Em produção".
12. Após finalizar a peça, o usuário registra a conclusão.
13. O sistema registra o consumo previsto dos materiais.
14. O sistema atualiza o estoque físico e libera os compromissos correspondentes.
15. O sistema altera o status para "Concluída".

### Fluxos alternativos

**FA01 - Materiais insuficientes**

O sistema permite registrar a ordem de produção e identifica o déficit de materiais.

A ordem permanece com status "Aguardando material".

**FA02 - Materiais disponíveis**

A ordem assume o status "Aguardando produção" até que o usuário registre seu início.

**FA03 - Compra de materiais pendentes**

Após o registro de uma compra, o usuário pode verificar novamente a disponibilidade dos materiais e atualizar o status da ordem.

**FA04 - Cancelamento da produção**

O usuário cancela uma ordem e o sistema libera os compromissos de materiais que ainda não tenham sido consumidos.

**FA05 - Diferença entre consumo previsto e real**

O usuário pode registrar um ajuste de estoque para corrigir diferenças identificadas durante ou após a produção.

**FA06 - Ficha técnica pendente**

Quando o produto não possuir ficha técnica completa, o sistema permite registrar a necessidade de produção vinculada ao pedido, mantendo-a pendente de planejamento.

O cálculo da necessidade de materiais e seu comprometimento no estoque somente devem ocorrer após a conclusão das informações necessárias na ficha técnica.

**FA07 - Configuração personalizada da produção**

O usuário seleciona os materiais, cores ou acabamentos dos componentes personalizáveis da peça.

O sistema utiliza essa configuração para calcular a necessidade de materiais e o custo estimado da produção, considerando as quantidades previstas na ficha técnica.

**FA08 - Produção para pronta entrega**

O usuário registra uma ordem de produção sem vinculá-la a um pedido de cliente.

Ao concluir a produção, o sistema registra a peça produzida e sua configuração, permitindo identificá-la como disponível para pronta entrega.

### Pós-condições

- A ordem de produção permanece registrada com seu status atualizado.
- Os materiais comprometidos e consumidos são refletidos no controle de estoque.
- O histórico da produção é preservado.

---

## UC010 - Registrar movimentação financeira

**Ator:** Usuário

**Objetivo:** Registrar entradas e saídas financeiras do negócio, incluindo pagamentos e recebimentos associados a compras e vendas.

### Pré-condições

- O sistema deve estar disponível.

### Fluxo principal

1. O usuário acessa o módulo financeiro.
2. O usuário seleciona a opção de nova movimentação.
3. O usuário informa o tipo da movimentação.
4. O usuário informa a categoria.
5. O usuário informa o valor e a data.
6. O usuário informa a situação do pagamento ou recebimento.
7. O usuário confirma o registro.
8. O sistema valida as informações.
9. O sistema registra a movimentação.

### Fluxos alternativos

**FA01 - Pagamento de compra**

O usuário registra o pagamento de uma obrigação financeira relacionada a uma compra.

**FA02 - Recebimento de venda**

O usuário registra um recebimento relacionado a uma venda.

**FA03 - Pagamento parcial**

O sistema atualiza o saldo pendente sem considerar a obrigação integralmente quitada.

**FA04 - Movimentação independente**

O usuário registra uma despesa ou receita que não esteja diretamente associada a uma compra ou venda.

### Pós-condições

- A movimentação permanece registrada.
- Os saldos financeiros relacionados são atualizados.
- Os dados ficam disponíveis para consultas e indicadores.

---

## UC011 - Consultar fluxo de caixa

**Ator:** Usuário

**Objetivo:** Acompanhar as entradas e saídas financeiras efetivamente realizadas pelo negócio.

### Pré-condições

- O sistema deve possuir registros financeiros.

### Fluxo principal

1. O usuário acessa o módulo financeiro.
2. O usuário seleciona a opção de fluxo de caixa.
3. O usuário informa o período desejado.
4. O sistema consulta as movimentações financeiras.
5. O sistema identifica os valores efetivamente recebidos e pagos no período.
6. O sistema calcula o total de entradas.
7. O sistema calcula o total de saídas.
8. O sistema calcula o saldo correspondente.
9. O sistema apresenta os resultados.

### Fluxos alternativos

**FA01 - Período sem movimentações**

O sistema apresenta os valores zerados e informa que não existem movimentações para o período selecionado.

**FA02 - Consulta de obrigações pendentes**

O usuário consulta separadamente contas a pagar e contas a receber.

### Pós-condições

- O usuário visualiza a situação financeira do negócio no período consultado.
- Nenhuma movimentação financeira é alterada pela consulta.

---

## UC012 - Consultar indicadores e dashboards

**Ator:** Usuário

**Objetivo:** Consultar informações consolidadas para acompanhar o desempenho do negócio e apoiar a tomada de decisão.

### Pré-condições

- O sistema deve possuir dados registrados nos módulos correspondentes.

### Fluxo principal

1. O usuário acessa o módulo de indicadores.
2. O sistema apresenta os dashboards disponíveis.
3. O usuário seleciona o período desejado.
4. O sistema consulta os dados dos módulos correspondentes.
5. O sistema calcula os indicadores.
6. O sistema apresenta os resultados por meio de valores consolidados, tabelas e gráficos.

### Fluxos alternativos

**FA01 - Indicadores comerciais**

O usuário consulta faturamento, quantidade de vendas e produtos comercializados.

**FA02 - Indicadores financeiros**

O usuário consulta receitas, despesas e saldo financeiro.

**FA03 - Indicadores de produção**

O usuário consulta a quantidade de ordens de produção por status.

**FA04 - Indicadores de estoque**

O usuário consulta materiais com estoque disponível inferior ao mínimo definido.

**FA05 - Ausência de dados**

O sistema informa que não existem dados suficientes para apresentar determinado indicador.

### Pós-condições

- O usuário visualiza informações consolidadas do negócio.
- Os dados originais permanecem inalterados.

---

# 4. Observações sobre o MVP

Os casos de uso apresentados correspondem às principais interações previstas para a primeira versão funcional do EntreTrama.

O sistema será inicialmente desenvolvido para utilização individual, considerando os processos reais de um pequeno negócio artesanal.

Funcionalidades como autenticação, múltiplos usuários, integração com plataformas de comércio eletrônico, leitura automática de documentos fiscais e previsão de vendas por inteligência artificial permanecem fora do escopo inicial.

Os casos de uso poderão ser refinados durante a modelagem e implementação, desde que as alterações sejam refletidas nos requisitos funcionais e nas regras de negócio correspondentes.