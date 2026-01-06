import random
from typing import Dict, Any, List, Tuple
from src.data import PRESIDENTS

class GameLogic:
    def __init__(self) -> None:
        self.presidents = PRESIDENTS

    def generate_question(self) -> Dict[str, Any]:
        president = random.choice(self.presidents)
        question_type = random.choice(["number", "years", "legislation"])
        
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

        options = self._generate_options(question_type, correct_answer, president)
        
        return {
            "question": question_text,
            "options": options,
            "correct_answer": correct_answer,
            "president_name": president["name"]
        }

    def _generate_options(self, question_type: str, correct_answer: str, current_president: Dict[str, Any]) -> List[str]:
        options = {correct_answer}
        while len(options) < 4:
            other = random.choice(self.presidents)
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
