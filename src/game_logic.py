import random
from typing import Dict, Any, List, Tuple
from src.data import get_all_presidents

class GameLogic:
    def __init__(self) -> None:
        pass

    def _get_presidents(self) -> List[Dict[str, Any]]:
        return get_all_presidents()

    def generate_question(self) -> Dict[str, Any]:
        presidents = self._get_presidents()
        president = random.choice(presidents)
        
        # Filter question types based on available data
        available_types = ["number", "years"]
        if president["legislation"]:
            available_types.append("legislation")
            
        question_type = random.choice(available_types)
        
        question_text = ""
        correct_answer = ""
        
        if question_type == "number":
            question_text = f"What number president was {president['name']}?"
            correct_answer = str(president["number"])
        elif question_type == "years":
            question_text = f"What years was {president['name']} president?"
            correct_answer = president["years"]
        elif question_type == "legislation":
            legislation = random.choice(president["legislation"])
            question_text = f"Which president oversaw the {legislation}?"
            correct_answer = president["name"]

        options = self._generate_options(question_type, correct_answer, president, presidents)
        
        return {
            "question": question_text,
            "options": options,
            "correct_answer": correct_answer,
            "president_name": president["name"]
        }

    def _generate_options(self, question_type: str, correct_answer: str, current_president: Dict[str, Any], all_presidents: List[Dict[str, Any]]) -> List[str]:
        options = {correct_answer}
        while len(options) < 4:
            other = random.choice(all_presidents)
            if other["name"] == current_president["name"]:
                continue
                
            if question_type == "number":
                options.add(str(other["number"]))
            elif question_type == "years":
                options.add(other["years"])
            elif question_type == "legislation":
                options.add(other["name"])
        
        options_list = list(options)
        random.shuffle(options_list)
        return options_list
