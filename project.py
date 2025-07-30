import re
import sys
import time
from emoji import UNICODE_EMOJI
from collections import Counter
import matplotlib.pyplot as plt




def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py 'file path'.txt")
    
    lines = load_file(sys.argv[1])
    messages = extract_messages(lines)
    users = extract_users(messages)
    message_per_user = count_user_messages({user: 0 for user in users}, messages)
    messages_in_day = count_day_messages(messages, "19/11/2024", "22/11/2024")
    frequent_words = count_frequent_words(messages, "01/01/2024", "31/12/2024")
    #index = 0
    # for word in sorted(frequent_words, reverse=True, key=lambda s: s["times"]):
    #     print(f"Word: {word["word"]}, apeared {word["times"]} times")
    #     index += 1
    #     if index > 10:
    #         break
    # frequent_emojis = count_frequent_emojis(messages, "01/01/2024", "31/12/2024")
    # print(frequent_emojis)
    # for emoji in sorted(frequent_emojis.items(), reverse=True, key=lambda kv: (kv[1], kv[0])):
    #     print(f"{emoji[0]} appeared {emoji[1]} times")
    #     index += 1
    #     if index > 10:
    #         break
    report(messages, users, "01/01/2023", "31/12/2025")
        
def load_file(path):
    """ Load the .txt file extracted from WhatsApp """

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        sys.exit(".txt file not found")
    except:
        sys.exit("Error in opening the file")


def extract_messages(lines):
    """ Filter only the messages sent and received in the chat, removing WhatsApp messages like end to end criptografy if necessary """

    messages = []
    for line in lines:
        if _ := re.search(r"^\d\d/\d\d/\d\d\d\d \d\d:\d\d - .*: ", line):
            messages.append(line)
        elif _ :=re.search(r"^[^\d\d/\d\d/\d\d\d\d \d\d:\d\d]", line):
            messages.append(line)
        
    return messages

def extract_users(messages):
    """ Exctrat the users of the chat """

    users = []
    for message in messages:
        if match := re.search(r"^\d\d/\d\d/\d\d\d\d \d\d:\d\d - (.[^:]*): ", message):
            if match.group(1) not in users:
                users.append(match.group(1))
    
    return users

def count_user_messages(users, messages):
    """ Count messages per user and returns a dictionary """

    for message in messages:
        if message := re.search(r"^\d\d/\d\d/\d\d\d\d \d\d:\d\d - (.[^:]*): ", message):
            users[message.group(1)] += 1

    return users
            

def count_day_messages(messages, first_day, last_day = 0):
    """ Returns all the messages sent and received between the given dates """

    number_of_messages = 0
    first_day=time.strptime(str(first_day).replace("/", " "), "%d %m %Y")

    if last_day == 0:
        last_day = first_day
    else:
        last_day = time.strptime(str(last_day).replace("/", " "), "%d %m %Y")

    for message in messages:
        if match := re.search(r"^(\d\d)/(\d\d)/(\d\d\d\d)", message):
            message_date = time.strptime(f"{match.group(1)} {match.group(2)} {match.group(3)}", "%d %m %Y")
            if first_day <= message_date <= last_day:
                number_of_messages += 1

    return number_of_messages
        

def count_frequent_words(messages, first_day, last_day = 0):
    """ Count the ocurrencys of every word between given dates """

    words = []

    first_day=time.strptime(str(first_day).replace("/", " "), "%d %m %Y")

    if last_day == 0:
        last_day = first_day
    else:
        last_day = time.strptime(str(last_day).replace("/", " "), "%d %m %Y")

    for message in messages:
        if match := re.search(r"^(\d\d)/(\d\d)/(\d\d\d\d) \d\d:\d\d - (?:.[^:]*): (.*)", message):
            message_date = time.strptime(f"{match.group(1)} {match.group(2)} {match.group(3)}", "%d %m %Y")
            if first_day <= message_date <= last_day:
                for word in match.group(4).split():
                    if word.lower() in ["<mídia", "oculta>", "e", "a", "de", "da", "do", "se", "que", "o", "pra", "para", "te", "é", "um", "ta", "na", "no", "as", "mas", "os", "com", "aí", "(arquivo", "anexado)", "ou"]:
                        break
                    index = find_word(words, "word", word)
                    if index == -1:
                        words.append({"word": word, "times": 1})
                    else:
                        words[index]["times"] += 1
        else:
            if first_day <= message_date <= last_day:
                for word in message.split():
                    if word.lower() in ["<mídia", "oculta>", "e", "a", "de", "da", "do", "se", "que", "o", "pra", "para", "te", "é", "um", "ta", "na", "no", "as", "mas", "os", "com", "aí", "(arquivo", "anexado)", "ou"]:
                        break
                    index = find_word(words, "word", word)
                    if index == -1:
                        words.append({"word": word, "times": 1})
                    else:
                        words[index]["times"] += 1
    return words

def find_word(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


def count_frequent_emojis(messages, first_day, last_day = 0):
    emoji = []

    first_day=time.strptime(str(first_day).replace("/", " "), "%d %m %Y")

    if last_day == 0:
        last_day = first_day
    else:
        last_day = time.strptime(str(last_day).replace("/", " "), "%d %m %Y")

    for message in messages:
        if match := re.search(r"^(\d\d)/(\d\d)/(\d\d\d\d) \d\d:\d\d - (?:.[^:]*): (.*)", message):
            message_date = time.strptime(f"{match.group(1)} {match.group(2)} {match.group(3)}", "%d %m %Y")
            if first_day <= message_date <= last_day:
                for word in match.group(4).split():
                    for character in word:
                        if character in UNICODE_EMOJI["en"]:
                            emoji.append(character)
        else:
            if first_day <= message_date <= last_day:
                for word in message:
                    for character in word:
                        if character in UNICODE_EMOJI["en"]:
                            emoji.append(character)

    return Counter(emoji)

def report(messages, users, first_day, last_day = 0):
    tp_all_time_user_messages = {name: 0 for name in users}
    day_users_messages = {name: 0 for name in users}
    chat_days=[]
    message_per_user = []
    all_time_message_per_user = []
    first_day=time.strptime(str(first_day).replace("/", " "), "%d %m %Y")

    if last_day == 0:
        last_day = first_day
    else:
        last_day = time.strptime(str(last_day).replace("/", " "), "%d %m %Y")

    for message in messages:
        if match := re.search(r"^(\d\d)/(\d\d)/(\d\d\d\d) \d\d:\d\d - (.[^:]*):", message):
            message_date = time.strptime(f"{match.group(1)} {match.group(2)} {match.group(3)}", "%d %m %Y")
            if first_day <= message_date <= last_day:
                if f"{match.group(1)}/{match.group(2)}/{match.group(3)}" in chat_days:
                    day_users_messages[match.group(4)] += 1
                    tp_all_time_user_messages[match.group(4)] += 1
                else:
                    chat_days.append(f"{match.group(1)}/{match.group(2)}/{match.group(3)}")
                    if len(chat_days) == 1:
                        day_users_messages[match.group(4)] += 1
                        tp_all_time_user_messages[match.group(4)] += 1
                        continue
                    temp_message = []
                    for value in day_users_messages:
                        temp_message.append(day_users_messages[value])
                    message_per_user.append(temp_message)
                    for value in day_users_messages:
                        day_users_messages[value] = 0

                    day_users_messages[match.group(4)] += 1
                    tp_all_time_user_messages[match.group(4)] += 1

    temp_message = []
    for value in day_users_messages:
        temp_message.append(day_users_messages[value])
    message_per_user.append(temp_message)

    for value in tp_all_time_user_messages:
        all_time_message_per_user.append(tp_all_time_user_messages[value])

    plt.plot(chat_days, message_per_user, label=users)
    plt.xlabel('Day')
    plt.ylabel('Number of messages')
    plt.xticks(rotation=45)
    plt.title('Messages per day per user')
    plt.legend()
    plt.show()

    fig, ax = plt.subplots()
    hbars = ax.barh(users, all_time_message_per_user, align='center')
    ax.bar_label(hbars)
    ax.set_xlabel('Messages per user')
    plt.title('Messages per user')
    plt.show()


if __name__ == "__main__":
    main()

