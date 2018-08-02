from rasa_core.actions.action import Action

class ActionWhatIs(Action):
    def name(self):
        return 'action_what_is'

    def run(self, dispatcher, tracker, domain):
        word_template_map = {
            'proponente': 'Um proponente é bla bla bla bla bla',
            'banana': 'Banana é uma fruta amarela =)',
        }

        user_message = tracker.latest_message.text

        for word in word_template_map:
            if word in user_message:
                dispatcher.utter_message(word_template_map[word])
                return []
        dispatcher.utter_message('Desculpe, não sei conceituar isso ainda =/')
        return []

class ActionMultiline(Action):
    messages = ['']

    def name(self):
        return self.__class__.__name__

    def run(self, dispatcher, tracker, domain):
        for message in self.messages:
            dispatcher.utter_message(message)
        return []

class ActionCumprimentar(ActionMultiline):
    messages = [
        'Oi eu sou a Rouana, assistente virtual do minc, e posso te ajudar a '
        'esclarecer dúvidas sobre a Lei Rouanet',

        'e também solucionar problemas de proposta e projeto'
    ]

class ActionDefinirPerfil(ActionMultiline):
    messages = [
        'Você quer conversar sobre criação e andamento de projetos? '
        'Ou, podemos falar mais sobre a Lei Rouanet'
    ]

class ActionNovaProposta(ActionMultiline):
    messages = [
        'Esta trabalhando em uma nova proposta?'
    ]

class ActionDuvidaExecucao(ActionMultiline):
    messages = [
        'Sua dúvida está relacionada com captação de verba e execução do '
        'projeto?'
    ]

class ActionConheceProcesso(ActionMultiline):
    messages = [
        'Você sabe como funciona todo o andamento de um projeto de incentivo a'
        ' cultura?'
    ]

class ActionEspecificarProcesso(ActionMultiline):
    messages = [
        'Então, eu não consigo responder esta parte agora :confused:'
    ]

class ActionCadastroSalic(ActionMultiline):
    messages = [
        'Tem cadastro no SALIC?'
    ]

class ActionDespedir(ActionMultiline):
    messages = [
        'Tchau, até a próxima =)'
    ]

class ActionSubmissaoDeProjetos(ActionMultiline):
    messages = [
        'Tudo bem. Aqui vai um resumo do processo:',
        'A pessoa responsável, chamada de proponente, insere uma proposta cultural no Sistema de Apoio às Leis de Incentivo à Cultura (Salic), de forma eletrônica.',
        'Essa proposta é analisada pelo MinC. Se for aprovada, autoriza o proponente a captar recursos.',
        'Assim que o valor mínimo for captado, o proponente pode começar a executar o projeto.',
        'Durante a execução o proponente deve prestar contas de acordo com os prazos definidos na Lei Rouanet.',
        'A prestação de contas é analisada pelos técnicos do Ministério e se aprovada, permite que o proponente crie um novo projeto.',
    ]

class ActionDefinirContexto(ActionMultiline):
    messages = [
        'Entendi.',
        'Então, onde sua pergunta se encaixa melhor:',
        '1. Processo e estado do projeto',
        '2. Preenchimento do Salic',
        '3. Datas e Prazos',
        '4. Erros do SALIC',
        '5. Não sei bem onde se encaixa',
    ]

class ActionAviso(ActionMultiline):
    messages = [
        'Para eu ser mais eficiente na solução da sua dúvida vou fazer algumas perguntas.',
        'Você já preencheu uma proposta?',
    ]

class ActionIntroduzirExecucao(ActionMultiline):
    messages = [
        ':disappointed_relieved:',

        'Eu ainda não aprendi a falar sobre um projeto que está em Execução ou'
        ' em Prestação de Contas. Porém eu ainda estou aprendendo, em um futuro'
        ' próximo eu saberei responder sua dúvida :wink:',

        'Por agora eu recomendo entrar em contato com as equipes da SEFIC',

        'Execução: acompanhamento.incentivo@cultura.gov.br',

        'Prestação de Contas: prestacaodecontas.incentivo@cultura.gov.br',
    ]
