from src.game_logic import GameLogic

def test_generate_question():
    game = GameLogic()
    question = game.generate_question()
    
    assert "question" in question
    assert "options" in question
    assert "correct_answer" in question
    assert len(question["options"]) == 4
    assert question["correct_answer"] in question["options"]

def test_options_unique():
    game = GameLogic()
    question = game.generate_question()
    options = question["options"]
    assert len(set(options)) == 4
