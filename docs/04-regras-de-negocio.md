# 04 - Regras de Negócio

> **Versão:** 1.0  
> **Projeto:** EntreTrama  
> **Autora:** Thalita Judice  
> **Última atualização:** 24/09/2026

---

# Objetivo do Documento

Este documento apresenta as regras de negócio do sistema **EntreTrama**, estabelecendo condições, restrições e critérios que orientam o funcionamento dos processos relacionados à gestão de pequenos negócios artesanais.

As regras foram organizadas de acordo com os principais módulos do sistema e complementam os requisitos funcionais ao definir como determinadas operações devem ocorrer.

---

# 1. Materiais e Estoque

| Código | Regra de Negócio |
|---|---|
| RN001 | Todo material deve possuir uma unidade de medida definida. |
| RN002 | A quantidade disponível de um material pode assumir valores negativos quando a quantidade necessária para as produções for superior à quantidade existente em estoque. |
| RN003 | O estoque disponível de um material deve corresponder à quantidade em estoque menos a quantidade comprometida com produções. |
| RN004 | Um valor negativo no estoque disponível deve representar uma necessidade de reposição do material. |
| RN005 | Materiais que possuam movimentações registradas não devem ser excluídos permanentemente, podendo apenas ser desativados. |
| RN006 | Um material deve ser identificado como abaixo do estoque mínimo quando sua quantidade disponível for inferior ao limite definido para ele. |
| RN007 | Um material pode ser cadastrado no sistema mesmo que nunca tenha sido adquirido e sua quantidade inicial em estoque seja zero. |
| RN104 | O sistema deve permitir ajustes positivos e negativos na quantidade física dos materiais, para corrigir diferenças identificadas entre o estoque registrado e o estoque real. |
| RN105 | Todo ajuste manual de estoque deve registrar o material, a quantidade ajustada, a data e o motivo da operação, preservando o histórico de movimentações. |
| RN106 | Após um ajuste manual, o sistema deve recalcular a quantidade disponível do material considerando o estoque físico atualizado e as quantidades comprometidas com produções. | 

# 2. Fornecedores e Compras

| Código | Regra de Negócio |
|---|---|
| RN008 | Uma compra pode conter um ou mais materiais. |
| RN009 | Cada item de uma compra deve registrar o material adquirido, a quantidade e o valor correspondente. |
| RN010 | Uma compra pode estar associada a um fornecedor cadastrado. |
| RN011 | A confirmação de uma compra deve aumentar a quantidade em estoque dos materiais adquiridos. |
| RN012 | Uma compra pode ser realizada à vista ou parcelada. |
| RN013 | O parcelamento de uma compra deve ser registrado no módulo financeiro, considerando o valor total da compra e a quantidade de parcelas. |
| RN014 | O custo dos materiais deve ser registrado independentemente da forma de pagamento utilizada na compra. |
| RN015 | O cancelamento de uma compra já confirmada deve reverter as movimentações de estoque geradas por ela. |
| RN016 | Compras que possuam movimentações de estoque ou registros financeiros associados não devem ser excluídas permanentemente, devendo ter seu histórico preservado. |
| RN017 | O custo utilizado para valorar um material deve corresponder ao seu custo médio de aquisição. |
| RN018 | O custo médio de um material deve ser recalculado sempre que uma nova compra desse material for confirmada. |
| RN019 | O valor do frete deve ser registrado separadamente do valor dos materiais adquiridos. |
| RN020 | O frete deve compor o valor financeiro da compra, mas não deve ser incorporado ao custo médio dos materiais no MVP. |
| RN021 | Descontos aplicados diretamente a um item devem reduzir o custo de aquisição daquele item. |
| RN022 | Descontos aplicados ao valor total da compra devem ser registrados separadamente e não devem alterar o custo médio dos materiais no MVP. |

# 3. Produtos e Fichas Técnicas

| Código | Regra de Negócio |
|---|---|
| RN023 | Todo produto pode possuir uma ficha técnica contendo os materiais e as quantidades estimadas necessárias para produzir uma unidade. |
| RN024 | Cada item da ficha técnica deve estar associado a um material previamente cadastrado. |
| RN025 | A quantidade de material utilizada na ficha técnica deve ser registrada em uma unidade de medida compatível com o material. |
| RN026 | Quando a unidade de compra for diferente da unidade utilizada na produção, o sistema deve considerar a conversão entre as unidades para calcular o consumo e o custo do material. |
| RN027 | O custo de cada material na ficha técnica deve ser calculado proporcionalmente à quantidade utilizada e ao custo médio vigente do material. |
| RN028 | O custo dos materiais de um produto deve corresponder à soma dos custos dos materiais presentes em sua ficha técnica. |
| RN030 | Alterações no custo médio de um material devem refletir no custo estimado dos produtos que utilizam esse material. |
| RN031 | Um produto pode ser cadastrado sem ficha técnica completa, devendo ser identificado como "Ficha Técnica Pendente". |
| RN032 | Produtos com ficha técnica pendente podem ser utilizados em vendas, mas não devem possuir custo de produção calculado automaticamente até que a ficha seja concluída. |
| RN033 | Produtos que possuam histórico de vendas ou produção não devem ser excluídos permanentemente, podendo apenas ser desativados. |
| RN034 | O sistema deve permitir definir um valor de mão de obra por hora de trabalho. |
| RN035 | Cada ficha técnica deve permitir informar o tempo estimado necessário para produzir uma unidade do produto. |
| RN036 | O custo estimado de mão de obra de um produto deve ser calculado com base no tempo estimado de produção e no valor da hora de trabalho. |
| RN037 | O custo total estimado do produto deve corresponder à soma do custo dos materiais, do custo de mão de obra e dos demais custos de produção definidos para o produto. |
| RN101 | As quantidades de materiais informadas nas fichas técnicas devem representar estimativas de consumo, podendo apresentar diferenças em relação ao consumo efetivo durante a produção artesanal. |
| RN102 | O sistema deve permitir distribuir a quantidade total estimada de um material entre diferentes variações cadastradas, como cores de fio, utilizando percentuais cuja soma corresponda a 100%. |
| RN103 | O sistema deve permitir definir uma margem percentual adicional para o consumo estimado de materiais sujeitos a variações, considerando essa margem no cálculo da necessidade de materiais e do custo estimado de produção. |
| RN107 | Um produto deve representar um modelo artesanal, podendo ser produzido em diferentes cores, materiais e acabamentos sem exigir um novo cadastro de produto para cada combinação. |
| RN108 | A ficha técnica deve permitir identificar os componentes necessários à produção, suas quantidades estimadas e quais deles admitem escolha de material ou variação no momento da produção. |
| RN109 | Os componentes não personalizáveis devem manter os materiais definidos na ficha técnica, enquanto os componentes personalizáveis devem permitir a seleção entre materiais ou variações compatíveis previamente cadastrados. |


# 4. Produção

| Código | Regra de Negócio |
|---|---|
| RN038 | Toda ordem de produção deve estar associada a pelo menos um produto. |
| RN039 | A quantidade de materiais necessária para uma ordem de produção deve ser calculada com base na ficha técnica do produto e na quantidade a ser produzida. |
| RN040 | Ao registrar uma necessidade de produção, o sistema deve verificar a disponibilidade dos materiais necessários. |
| RN041 | A falta de materiais não deve impedir o registro da ordem de produção. |
| RN042 | Quando a necessidade de materiais for superior ao estoque disponível, o sistema deve registrar o déficit como necessidade de reposição. |
| RN043 | Os materiais necessários para uma produção devem ser considerados comprometidos para aquela produção, reduzindo a quantidade disponível para novas produções. |
| RN044 | A quantidade disponível de um material pode assumir valor negativo quando as necessidades das produções forem superiores à quantidade existente em estoque. |
| RN046 | Ao concluir uma ordem de produção, o sistema deve registrar o consumo definitivo dos materiais, reduzir suas quantidades no estoque físico e liberar as quantidades anteriormente comprometidas com aquela produção, garantindo que cada material seja baixado apenas uma vez.  |
| RN048 | Uma ordem de produção deve possuir um dos seguintes status: "Aguardando material", "Aguardando produção", "Em produção", "Concluída" ou "Cancelada". |
| RN049 | Uma ordem de produção deve assumir o status "Aguardando material" quando houver déficit de um ou mais materiais necessários para sua produção. |
| RN050 | Uma ordem de produção poderá assumir o status "Aguardando produção" quando todos os materiais necessários estiverem disponíveis, mas sua produção ainda não tiver sido iniciada. |
| RN051 | Ao iniciar a produção, seu status deve ser alterado para "Em produção". |
| RN052 | Ao finalizar a produção, seu status deve ser alterado para "Concluída". |
| RN053 | Uma ordem de produção cancelada deve assumir o status "Cancelada" e liberar os materiais anteriormente comprometidos com ela. |
| RN054 | Cada ordem de produção deve possuir um prazo previsto para conclusão. |
| RN055 | Alterações na ficha técnica de um produto não devem modificar retroativamente os materiais e custos registrados em produções já concluídas. |
| RN110 | Cada ordem de produção deve registrar a configuração específica dos componentes personalizáveis da peça, incluindo os materiais, cores e acabamentos selecionados. |
| RN111 | Uma ordem de produção pode estar vinculada a um pedido ou ser registrada para produzir peças destinadas à pronta entrega. |
| RN112 | O cálculo da necessidade de materiais, do custo estimado e das quantidades comprometidas deve considerar a configuração definida para a ordem de produção. |
| RN113 | A configuração de uma produção concluída deve ser preservada historicamente, mesmo que a ficha técnica do produto seja alterada posteriormente. |
| RN114 | Peças concluídas e destinadas à pronta entrega devem permanecer identificáveis por produto e configuração, permitindo distinguir unidades disponíveis com diferentes cores e acabamentos. |

# 5. Clientes

| Código | Regra de Negócio |
|---|---|
| RN056 | Uma venda pode ser associada a um cliente cadastrado. |
| RN057 | Um cliente pode possuir várias vendas e pedidos associados ao seu histórico. |
| RN058 | Clientes que possuam vendas ou pedidos associados não devem ser excluídos permanentemente, podendo apenas ser desativados. |
| RN059 | A desativação de um cliente não deve alterar seu histórico de vendas e pedidos. |

# 6. Vendas e Pedidos

| Código | Regra de Negócio |
|---|---|
| RN060 | Toda venda ou pedido deve possuir pelo menos um item. |
| RN061 | Uma venda pode ser registrada com ou sem cliente identificado. |
| RN062 | Cada item de uma venda deve registrar o produto, a quantidade e o preço de venda praticado no momento da operação. |
| RN063 | O preço registrado em uma venda deve ser preservado historicamente, mesmo que o preço atual do produto seja alterado posteriormente. |
| RN064 | Uma venda pode conter produtos já cadastrados ou produtos cadastrados durante o próprio registro da venda. |
| RN065 | Um produto cadastrado durante uma venda pode ser salvo sem ficha técnica completa, devendo ser identificado como "Ficha Técnica Pendente". |
| RN066 | O cadastro de um novo produto durante uma venda não deve apagar os dados da venda que já tenham sido preenchidos. |
| RN067 | Produtos sob encomenda devem gerar uma necessidade de produção associada ao pedido. |
| RN068 | Produtos disponíveis para pronta entrega não devem gerar automaticamente uma nova ordem de produção. |
| RN069 | Uma mesma venda pode possuir mais de um produto e diferentes quantidades de cada produto. |
| RN070 | O valor total da venda deve considerar a soma dos itens, acrescida do frete cobrado do cliente e descontados eventuais descontos concedidos. |
| RN071 | Toda venda deve registrar o canal em que foi realizada, quando essa informação estiver disponível. |
| RN072 | O cancelamento de um pedido deve cancelar as produções vinculadas que ainda não tenham sido concluídas e liberar os materiais comprometidos com elas. |
| RN073 | Alterações posteriores no cadastro ou no custo de um produto não devem modificar os valores históricos registrados em vendas já realizadas. |

# 7. Financeiro

| Código | Regra de Negócio |
|---|---|
| RN074 | Uma venda pode ser paga integralmente no momento do pedido, parcialmente, posteriormente ou de forma parcelada. |
| RN075 | O status financeiro de uma venda deve ser controlado independentemente do status de produção ou entrega do pedido. |
| RN076 | Uma venda pode possuir os status financeiros "Pendente", "Parcialmente Pago", "Pago" ou "Cancelado". |
| RN077 | O valor recebido de uma venda deve corresponder à soma de todos os pagamentos registrados para ela. |
| RN078 | O saldo a receber de uma venda deve corresponder ao valor total da venda menos os pagamentos já recebidos. |
| RN079 | Uma venda deve ser considerada "Paga" somente quando o valor recebido for igual ou superior ao valor total devido. |
| RN080 | Quando houver pagamento parcial, o sistema deve manter registrado o saldo restante a receber. |
| RN081 | Vendas parceladas devem gerar parcelas individualizadas, contendo valor, vencimento e status de pagamento. |
| RN082 | Uma parcela deve possuir um dos status "Pendente", "Paga" ou "Vencida". |
| RN083 | O pagamento de uma parcela deve atualizar automaticamente o valor recebido e o saldo a receber da venda. |
| RN084 | Compras parceladas devem gerar contas a pagar independentes dos custos dos materiais adquiridos. |
| RN085 | O pagamento de uma parcela de compra não deve alterar o custo dos materiais, pois o custo da compra é reconhecido independentemente da forma de pagamento. |
| RN086 | O módulo financeiro deve distinguir receitas, despesas, contas a pagar e contas a receber. |
| RN087 | Receitas e despesas devem possuir data, valor e categoria. |
| RN088 | O fluxo de caixa deve considerar as movimentações financeiras efetivamente recebidas ou pagas no período. |
| RN089 | O custo estimado de mão de obra utilizado na ficha técnica não deve gerar automaticamente uma saída financeira no fluxo de caixa. |
| RN090 | O cancelamento de uma venda deve preservar o histórico financeiro já registrado e permitir identificar valores que precisem ser devolvidos ou ajustados. |

# 8. Indicadores e Dashboards

| Código | Regra de Negócio |
|---|---|
| RN091 | Os indicadores financeiros devem considerar o período selecionado pelo usuário. |
| RN092 | O faturamento deve corresponder ao valor das vendas realizadas no período, independentemente da data em que os respectivos pagamentos forem recebidos. |
| RN093 | O fluxo de caixa deve considerar somente os valores efetivamente recebidos ou pagos no período. |
| RN094 | Vendas canceladas não devem compor o faturamento, salvo quando necessário para análises históricas específicas. |
| RN095 | A quantidade vendida de um produto deve corresponder à soma das unidades registradas nas vendas válidas do período. |
| RN096 | A lucratividade estimada de um produto deve considerar o preço praticado na venda e o custo estimado correspondente ao produto. |
| RN097 | Os indicadores de estoque devem considerar separadamente a quantidade física, a quantidade comprometida e a quantidade disponível dos materiais. |
| RN098 | Materiais com quantidade disponível inferior ao estoque mínimo definido devem ser identificados nos indicadores de estoque. |
| RN099 | Os indicadores de produção devem considerar o status atual das ordens de produção. |
| RN100 | Alterações posteriores nos cadastros de produtos não devem modificar os valores históricos utilizados nos indicadores referentes a vendas já realizadas. |