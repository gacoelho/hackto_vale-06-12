from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionColocarNaFilaPrioritaria(Action):
    def name(self) -> str:
        return "action_colocar_na_fila_prioritaria"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Aqui você pode adicionar lógica para colocar o usuário em uma fila de urgência
        # Isso pode ser feito armazenando informações no banco de dados ou usando slots.
        
        # Simulando a adição do usuário à fila de urgência
        line_numeber =+ 1
        dispatcher.utter_message(text=f"Sua chamada foi registrada como urgente e voce é {line_numeber} da fila prioritária.")

        # Se você tiver algum slot para gerenciar a urgência, pode configurá-los aqui
        return [SlotSet("urgencia", True)]