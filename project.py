import re
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py 'file path'.txt")
    
    lines = load_file(sys.argv[1])
    messages = extract_messages(lines)
    users = extract_users(messages)
    message_per_user = count_user_messages({user: 0 for user in users}, messages)
    print(message_per_user)



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
            

def count_day_messages(day):
    ...

def frequent_words(first_day, last_day):
    ...

def frequent_emojis(first_day, last_day):
    ...

def report():
    ...

if __name__ == "__main__":
    main()

