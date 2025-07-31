from project import count_user_messages
from project import count_day_messages
from project import count_frequent_words
from project import count_frequent_emojis
import time
from collections import Counter

test_messages = [
    "01/01/2025 10:00 - test1: testest",
    "01/01/2025 10:00 - test2: testest2 😂😂",
    "01/01/2025 10:00 - test1: testest",
    "01/01/2025 10:00 - test1: testest 😊",
    "01/01/2025 10:00 - test2: testest2",
    "01/01/2025 10:00 - test1: testest",
    "01/01/2025 10:00 - test2: testest2",
]

def test_count_user_messages():
    assert count_user_messages({"test1": 0, "test2": 0}, test_messages) == {"test1": 4, "test2":3}

def test_count_day_messages():
    assert count_day_messages(test_messages, time.strptime("2025 01 01", "%Y %m %d")) == 7

def test_count_frequent_words():
    assert count_frequent_words(test_messages, time.strptime("2025 01 01", "%Y %m %d")) == [{"word": 'testest', "times": 4},{"word": 'testest2', "times": 3}]

def test_count_frequent_emojis():
    assert count_frequent_emojis(test_messages, time.strptime("2025 01 01", "%Y %m %d")) == Counter({"😂": 2, "😊": 1})



