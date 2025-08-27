# Personal Website

A personal website built with **Django**, combining static templates with other stuff like a chatbot.

---

##  Overview

This repository contains a Django-based personal website featuring:

- App folders (e.g., blog, chatbot).
- A simple AI or conversational **chatbot** module. (an external module in python)
  An untrained Chatterbot works by saving your input text in its library. Every time you give chat with the chatterbot, it increases the accuracy of the response of the chatbot. Basically the program selects the closest matching response by searching for the closest matching known statement that matches the input, it then chooses a response from the selection of known responses to that statement.
  But in this project I have already trained the chatbot before hand using the the chatterbot module's inbuilt corpus data.
  This chatbot was primarily made to answer the queries of my viewers regarding my yt channel (discontinued).
```python
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")
```

- `codewithshakyo` is the django project with apps like `blog`, `chatbot` in it.

---

##  Components and 

| Component               | Lang used and Description|
|------------------------|--------------------------|
| Web Framework          | Python Django            |
| Templates               | HTML, Django templating |
| Styling & Interactivity | CSS, Materialize,JavaScript|
| Chatbot                 | `chatterbot` database`database-chatterbot.sqlite3`|
| Deployment Config      | `Procfile (for heroku)`, `vercel.json`, `domain.pythonanywhere.com`|
| Dependencies           | Listed in `requirements.txt` |
| Runtime                | Python version specified in `runtime.txt` |

---

##  Project Initialization

### Clone & Setup

```bash
git clone https://github.com/sudo-shakyo/personal-website.git
cd personal-website
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Locally
To run this website locally you just need to run the follwing commands in your terminal:
```bash
python manage.py makemigrations #
python manage.py migrate     # Set up the database
python manage.py runserver   # Visit http://127.0.0.1:8000
```
### Python manage.py makemigrations
-this command is used to generate new migrations files based on the changes that you have made in your models.py file (models.py file contains those classes that defines your database schema).
-this command detects changes in your models then this command prepares migration files which store the changes of the database schema. 
 but this command doesn't apply the changes in your database, it just stores the changes (think of it like writing down the plan).

### Python manage.py migrate
-this command basically applies those changes into the database.
-think of it like executing the gameplan.

### Python manage.py runserver
-this command just runs a locally hosted server in your machine (usually 127.0.0.1:8000).
-you can change the port or run it on your ip address or anything depending on your need by applying the needed changes in the `settings.py` file in `codewithshakyo` folder.




### Project Structure
```
/
├── blog/                     # Blog (contains functionalities and logic behind stuff like the contact form, announcements page, user auth, etc.
├── chatbot/                  # Chatbot made using the chatterbot module
├── codewithshakyo/           # Main App
├── static/                   # Static files (CSS, JS)
│   └── styles/                  CSS files
├── templates/                # Django templates
├── app.py                    # A demo usage of the chatbot using Flask (file is commented out so its basically useless)
├── manage.py                 # Django management script (basically used to run commands like migrate, makemigrations, and running the server or creating superuser)
├── requirements.txt          # Python dependencies or modules that are used in this project
├── runtime.txt               # Python runtime version
├── Procfile                  # Deployment config for Heroku *didn't deploy it yet
├── vercel.json               # Deployment config for Vercel *didn't deply it yet
├── database*.sqlite3         # SQLite DB files (chatbot & contact page, user auth etc etc.)
└── sentence_tokenizer.pickle # Tokenizer model for chatbot
```
### Contributing to the project
Any sort of contributions are welcome!


### Auhor
Shakyo Deb Choudhury `sudo-shakyo`
