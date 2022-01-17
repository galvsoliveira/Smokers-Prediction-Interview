# SmokersPredictionInterview

## 1. Contextualização
Este projeto é parte da segunda fase de um processo seletivo da empresa X. Recebemos o conjunto de dados e somente as seguintes informações:

"-- 2ª Etapa de entrevista para vaga - Cientista de dados Jr.

Olá! Se você está lendo esta mensagem é porque te escolhemos para avançar em nosso processo seletivo! Parabéns =D
O intuito agora é verificar se você possuí a capacidade de execução, e para isso temos uma lista de desafios que deve ser entregue em Python.
Lembrando, você fará a apresentação do seu projeto em nossa próxima conversa, estamos ansiosos por isso. Rs
Utilize o arquivo "DF Cientista de dados Jr" como base de dados para seu projeto.
Confira os desafios logo a baixo, boa sorte!😉

-- Desafios
- ETL
- Engenharia de variávies
- Gráficos / Visualização
- Correlações
- Modelo para Classidicação - Variável target: Fumante
- Tunagem de modelo

**Caso queira fazer um webapp fique à vontade."


## 2. Sobre os dados, temos as seguintes informações:

 - Sexo: masculino ou feminino.
 - Região: sudoeste, sudeste, nordeste, noroeste.
 - IMC: de 15.96 à 53.13.
 - Número de filhos: de 0 à 5.
 - Idade: de 18 à 64.
 - Renda em 2021: 1121.87 à 63770.43.
 - Fumante: sim ou não.

Por simplicidade, vamos considerar que os fumantes são exclusivamente fumantes de cigarro tradicional. O valor hoje de um maço de cigarro é em média 7.00 reais. Além disso, um estudo de 2013 revela que o brasileiro consome em média 17 cigarros por dia, e como em cada maço contém 20 cigarros, o gasto mensal fica em torno de 178.50 reais, 16.22% do salário mínimo de 2021 (Fonte: [http://g1.globo.com/pr/norte-noroeste/noticia/2015/07/pesquisa-mostra-que-fumante-gasta-r-10-mil-por-mes-com-cigarros.html](http://g1.globo.com/pr/norte-noroeste/noticia/2015/07/pesquisa-mostra-que-fumante-gasta-r-10-mil-por-mes-com-cigarros.html)).

Com isso, podemos formalizar algumas hipóteses:

- Pessoas que ganham mais dinheiro, tem mais chances de serem fumantes.
- Pessoas que moram em regiões mais caras têm maior probabilidade de serem fumantes.
- Pessoas fumantes tendem a ter um IMC maior.
- Fumantes independem do sexo ou da idade.
- Fumantes vivem menos.


## 3. Sobre as hipóteses:

- Pessoas que ganham mais dinheiro, tem mais chances de serem fumantes?
    Confirmado, as pessoas com uma renda maior tem mais chances de manter o vício do tabajismo, possivelmente pelo alto preço do maço de cigarro hoje em dia. Isso reforça que as políticas de aumento do preço do cigarro causaram o decaimento de fumantes (Fonte: http://direito.folha.uol.com.br/blog/tabagismo-o-consumo-caiu-por-causa-do-preo-maior-ou-junto-com-o-aumento-do-preo)
- Pessoas que moram em regiões mais caras têm maior probabilidade de serem fumantes.
    Confirmado, mas seria interessante obter dados de regiões mais desiguais para comparar melhor.
- Pessoas fumantes tendem a ter um IMC maior.
    Refutado, pelos dados, não podemos relacionar IMC com tabajismo.
- Fumantes independem do sexo.
    Confirmado, o sexo da pessoa não é relevante na determinação do vício, porém, devido a homens terem uma renda maior que mulheres, há mais homens fumantes que mulheres.
- Fumantes vivem menos.
    Confirmado!! Pessoas viciadas em cigarro tendem a viver cerca de 2 anos menos, em média.

## 4. Questões que devem ser levadas ao time para uma análise mais aprofundada:

- Por que mulheres que não fumam ganham mais que os homens? Ou está dentro do erro esperado?
- Por que temos mais fumantes no sudeste? Região mais fria? Região onde tem mais renda tem mais pessoas estressadas devido ao trabalho (overwork) e levando a mais pessoas fumantes?
- O que leva jovens a fumarem mais?
- O que causa pessoas com 1 a 2 filhos terem maiores chances de serem fumantes?

## 5. Modelo:
 - O melhor modelo é o de Regressão Logística, com acurácia de 96.41%, mas com a maior precisão 85.18%. (Antes de remover Sexo, Região e Filhos).
 - Depois da remoção o melhor é o KNN, com 96.11% de acurácia e 85% de precisão.

## 5.1 Conclusão sobre o modelo:
- A filtragem de variáveis melhorou o desempenho do modelo KNN de 95% de acurácia para 96% e a precisão de 81% para 85%. Portanto, a remoção de parâmetros não importante melhorou consideravelmente o desempenho do KNN (o que faz sentido com a teoria do KNN), facilitando o treinamento e como consequência o fitting.

## 6. WebApp
 O webapp está disponível no arquivo app.py. Ele foi desenvolvido no streamlit e nele é possível que o usuário insira valores de parâmetros de indivíduos a serem analisados pelo modelo. Ao pressionar um botão no aplicativo, é retornado se o indivíduo é ou não fumante e qual a probabilidade daquele valor ser real. Com base nos dados inseridos e resultantes do modelo, é formado uma tabela que pode ser baixada pelo usuário através de um botão de download no formato CSV.
