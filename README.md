# 📊 WhatsApp Chat Analyzer

Video demo: https://youtu.be/pkIC6Y225EI

Final project for **CS50's Introduction to Programming with Python**.  
This program analyzes a `.txt` file exported from a WhatsApp chat and provides insightful statistics about the conversation.

## 💡 Features

The program offers the following analysis options:

1. **Count messages per user**  
2. **Count messages in a specific date range**  
3. **Most frequent words in a specific date range**  
4. **Most used emojis in a specific date range**  
5. **Summary report with graphs**:
   - Daily messages per user
   - Total messages per user within a selected date range

## 🗂️ Expected Input

A `.txt` file exported from WhatsApp using the default format (date - user: message).  
Example of a valid line:
```
07/12/2023 14:23 - John: Hey, how are you?
```

## ▶️ How to Use

```bash
python project.py "path/to/chat_file.txt"
```

After loading the file, a menu will appear with options to choose from for analysis.

## 🧰 Requirements

- Python 3.x  
- Libraries:
  - `emoji`
  - `matplotlib`

Install the required dependencies with:

```bash
pip install emoji matplotlib
```

## 📈 Example Output

The program generates:
- Line charts of daily messages per user
- Bar charts showing total messages per user during a selected date range

## 🧑‍💻 Author

Developed by **Lucas Reis** as the final project for [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/).