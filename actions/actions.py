from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction

# Ação para colocar o usuário na fila prioritária
class ActionColocarNaFilaPrioritaria(Action):
    def name(self) -> str:
        return "action_colocar_na_fila_prioritaria"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Simulando a adição do usuário à fila de urgência
        # Aqui, podemos melhorar a lógica para calcular dinamicamente o número da fila
        # Vamos usar uma variável ou banco de dados para gerenciar isso em um cenário real
        line_number = 1  # Exemplo estático para o número da fila

        dispatcher.utter_message(text=f"Sua chamada foi registrada como urgente e você é {line_number} da fila prioritária.")

        # Atualizando o slot 'urgencia' para True, indicando que o usuário foi colocado na fila de urgência
        return [SlotSet("urgencia", True)]

# Ação para salvar os detalhes do problema
class ActionSaveProblemDetails(Action):
    def name(self) -> Text:
        return "action_save_problem_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Coletando a descrição do problema a partir da última mensagem do usuário
        descricao = tracker.latest_message.get('text')
        if descricao:
            dispatcher.utter_message(text=f"Entendido, você mencionou: {descricao}.")
        else:
            dispatcher.utter_message(text=f"Eu não entedi seu problema")
        # Salvando a descrição no slot 'descricao_problema'
        return [SlotSet("descricao_problema", descricao), FollowupAction('utter_acknowledge')]



class ActionSaveFeedBack(Action):
    def name(self):
        return "action_save_feedback"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        feedback = tracker.latest_message.get('text')
        dispatcher.utter_message(text="Obrigado pelo feedback! Com isso você nos ajuda amelhor o seu atendimento :)")

        return [SlotSet("feedback", feedback), FollowupAction('utter_despedida')]
    
class ActionCarreira(Action):
    def name(self):
        return "action_carreira"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Entendido, você quer falar sobre Carreira")

class ActionCultura(Action):
    def name(self):
        return "action_cultura"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Entendido, você quer falar sobre Cultura")

class ActionComite(Action):
    def name(self):
        return "action_comite"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Entendido, você quer falar sobre Comitê")

class ActionDesligamento(Action):
    def name(self):
        return "action_desligamento"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Entendido, você quer falar sobre Desligamento")

class ActionDesenvolvimento(Action):
    def name(self):
        return "action_desenvolvimento"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Entendido, você quer falar sobre Desenvolvimento")

class ActionGreetUser(Action):
    def name(self):
        return "action_greet_user"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name = tracker.latest_message.get("metadata", {}).get("user_name")

        if user_name:
            message = f"Olá gestor {user_name}! Como posso te ajudar?"
        else:
            message = "Olá Usuário! Como posso te ajudar?"
        
        dispatcher.utter_message(text=message)






