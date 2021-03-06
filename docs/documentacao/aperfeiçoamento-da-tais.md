---
layout: page
permalink: /documentacao/aperfeiçoamento-da-tais/
title: Aperfeiçoamento da Tais
---

# Processo de Aperfeiçoamento da Tais


## Como encontrar Bugs
Para perceber em quais pontos a Tais precisa melhorar, é necessário ter acesso às conversas dos usuários, pois só assim vamos entender onde a Tais está falhando com o nosso público alvo. Existe a possibilidade também de acessar os dashboards do Kibana, lá podemos ver as intents que estão com a confiança baixa e também a intents que estão caindo no default, ou seja, que a Tais não sabe responder. Mesmo tendo acesso aos dashboards é muito importante ler as conversas, pois lendo entendemos  o contexto e podemos ver a intenção real do usuário ao fazer a pergunta. 


## Como solucionar Bugs
Em cada conversa analisada é preciso anotar os bugs encontrados, quando a Tais possui o conteúdo perguntado mas não identificou a pergunta do usuário é um problema de atualização de intents, neste caso temos que procurar a intent existente e melhorá-la sem que isso afete a precisão das outras intents que existem.
Quando a Tais tem o conteúdo perguntado e também possui em sua intent o exemplo de pergunta que o usuário usou, neste caso provavelmente será um problema de contexto, ela não conseguiu entender a pergunta naquele momento, para solucionar este tipo de bug devemos fazer uma atualização de stories relacionadas ao contexto daquela pergunta, ou seja, devemos construir um caminho no fluxo que permita que ela entenda aquela pergunta naquele dado momento.
Alguns conteúdos que a Tais já possui podem ser otimizados, por exemplo se ela responde sobre determinado prazo, e temos uma pergunta se tal prazo pode ser prorrogado, podemos juntar os dois assuntos e fazer uma atualização de conteúdo. Neste caso, devemos melhorar tanto a utter quanto a intent relacionadas a este conteúdo.
Há também os novos assuntos que a Tais não sabe responder. Deste modo, temos também o procedimento de inserir conteúdo novo, nesta etapa temos que analisar quais conteúdos podem ser inseridos sem diminuir a eficiência da Tais, e quais ela ainda não tem maturidade para responder neste momento, o importante é sempre deixar anotado tudo isso para que um dia tal conteúdo possa fazer parte do seu repertório de informações.Quando um usuário pergunta, a Tais responde corretamente, mas mesmo assim ele não se sente contemplado com a resposta precisamos fazer uma melhoria de utter, temos que melhorar o texto da Utter para que ela fique mais clara e consiga sanar as dúvidas do usuário.
A Tais está constantemente aprendendo a se comunicar melhor, a ser mais gentil e mais polida, sendo assim temos a parte de melhoria de interação, nela criamos modos de fazer ela ser cada vez mais humana, como por exemplo responder a um obrigada, a um tudo bem, entre outras façanhas que fazem parte da nossa comunicação quotidiana. Estes são apenas algumas classes de bugs que foram encontradas, com toda certeza na medida em que a Tais for evoluindo vamos encontrar novas formas de atualizá-la e consequentemente surgirão novos problemas e novas classes de Bugs.


## Organização é Tudo
Mas e aí, como vamos conseguir organizar tudo isso de cada conversa lida? Primeiramente é necessário abrir issues relacionadas aos bugs encontrados, para a atualização de intents, pode-se fazer um compilado de intents que precisam ser atualizadas, mapeá-las, atualizá-las, testá-las uma por uma, deve-se fazer passar nos testes de stories e por fim averiguar se todas foram atualizadas com sucesso. Já para as outras situações é interessante abrir uma issue para cada bug encontrado.
Todos os dias os usuários entram em contato com o nosso chatbot, deste modo, deve-se ler as conversas diárias e anotar os bugs, separando-os na classificação de bugs propostas acima. Após, coletar material suficiente, abrimos as issues e começamos a trabalhar! Como já dito, aqueles bugs que a Tais ainda não tem maturidade para solucionar, ficam anotados esperando o dia em que ela possa aprender a lidar com aquele tipo de situação.


## Benefícios do Monitoramento
Quando criamos um(a) assistente virtual, colocamos as nossas melhores intents, sempre tentando pensar em como o usuário pode perguntar por esse conteúdo, além disso, tentamos criar os melhores fluxos e as melhores utters, para que ela responda de forma eficiente e sane as dúvidas dos usuários. Contudo, os nossos usuários são de fato imprevisíveis, quando lemos as conversas, passamos a ver tudo de um novo ângulo, aquele modo de perguntar pode ser feito de um zilhão de jeitos diferentes e muitas vezes também as mensagens que a nossa assistente virtual envia por mais que pareçam claras e coerentes podem despertar novas dúvidas em quem as recebe. A melhor forma de evoluir um chatbot é tendo o contato real de como ele está interagindo com as pessoas, lendo as conversas podemos enriquecer o nosso bot, tornando-o apto para lidar com as situações reais e não somente com as hipóteses que se passaram na nossa cabeça, tal processo garante que ele se torne cada dia mais eficiente. 
