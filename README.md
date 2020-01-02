# mugbot
Source code of the mug discord bot

The code looks really bad and a lot of things can be improved, so feel free to brach it.

It uses pickle to save scores. To save the score type "s" in any chat. This is not the best solution, but it is better than to save scores on each 'mug' message.

To clear edited messages type "c" in the chat. It uses regex to check last 100 messages and delete anything that matches it. (the exact regex I am using is not included).

Modules required:
```
pip install discord.py
pip install python-dotenv
```
