import pytest
from unittest.mock import patch, MagicMock
from src.game_logic import GameLogic

# Mock data to avoid database dependency in tests
MOCK_PRESIDENTS = [
    {
        "id": 1,
        "number": 1,
        "name": "George Washington",
        "years": "1789-1797",
        "legislation": ["Judiciary Act"]
    },
    {
        "id": 2,
        "number": 2,
        "name": "John Adams",
        "years": "1797-1801",
        "legislation": ["Alien and Sedition Acts"]
    },
    {
        "id": 3,
        "number": 3,
        "name": "Thomas Jefferson",
        "years": "1801-1809",
        "legislation": ["Embargo Act"]
    },
    {
        "id": 4,
        "number": 4,
        "name": "James Madison",
        "years": "1809-1817",
        "legislation": []
    }
]

@patch('src.game_logic.get_all_presidents')
def test_generate_question(mock_get_presidents):
    mock_get_presidents.return_value = MOCK_PRESIDENTS
    game = GameLogic()
    question = game.generate_question()
    
    assert "question" in question
    assert "options" in question
    assert "correct_answer" in question
    assert len(question["options"]) == 4
    assert question["correct_answer"] in question["options"]

@patch('src.game_logic.get_all_presidents')
def test_options_unique(mock_get_presidents):
    mock_get_presidents.return_value = MOCK_PRESIDENTS
    game = GameLogic()
    question = game.generate_question()
    options = question["options"]
    assert len(set(options)) == 4
