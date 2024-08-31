# Send Email using Gmail with Python 🐍📨

How to send emails from your gmail account using Python. This is a simple and easy to use package that allows you to send emails from your gmail account using Python. 

This package is built on top of the `smtplib` library and is designed to be easy to use and have common defaults for using smtp with Gmail so you don't have to think about it. This package also supports emojis in text by default.

## Table of Contents

## Features

- Easy API
- Common defaults for using smtp with Gmail so you don't have to think about it.
- Supports emojis in text by default

## Requirements

- Must have a Gmail account
- Must have 2 factor authentication setup on your gmail account
- Must create an app password for your gmail account
- Python 3.10 or higher
- Pip 24.2 or higher
- Pip packages:
        - annotated-types==0.7.0
        - pydantic==2.8.2
        - pydantic_core==2.20.1
        - python-dotenv==1.0.1
        - typing_extensions==4.12.2

## Quick-Start

Create your instance and send an email:

```py
>>> from gmail import Client
>>> client = Client(
    email='sender@gmail.com', 
    app_password='a1aa bb2b dddd cc3c'
)
>>> client.send_email(
    to='reciver@gmail.com', 
    subject='Hello! 👋', 
    body='How are you today? 🤔'
)
```

or send to multiple emails separately:

```py
>>> client.send_email(
    to=[
        'first.email@ptyhon.org', 
        'second.email@python.org'
        ], 
    subject='Hello! 👋', 
    body='How are you today? 🤔')
```

That's it!

## Basic Usage

### Creating an Instance

You can create a gmail instance from just your gmail account email and your gmail account app password

```py
>>> from gmail import Client
>>> client = Client(
    email='your.gmail@gmail.com', 
    app_password='a1aa bb2b dddd cc3c'
)
```

>This will create a client instance that you can use to send emails. This is not the most secure way to create a client instance, but it is the easiest way to do so.

If you wish to create a client instance more securely, you can create a client instance from environment variables.

---

### Creating an Instance from environment variables

If you wish to create instantiate a client **more securely**, you can create your instance from environment variables using the `GMAIL_EMAIL` and `GMAIL_APP_PASSWORD` environment variable names.

1. Create a `.env` file in your directory and add the following:

```.env
GMAIL_EMAIL=example@gmail.com
GMAIL_APP_PASSWORD=aaaa aaaa aaaa aaaa
```

2. Create your instance:

```python
>>> client = Client.from_env()
```

### Sending Emails

You can send an email by writing the following:

```python
>>> client.send_email(
...     to='other@gmail.com',
...     subject='Hello! 👋',
...     body='How are you doing? 🤔'
... )
```

This will send an email with a subject and body.

>**Important Note:** Where usually you would see the name of your gmail account, you will only see your email **unless** you specify a name in the `from_` field, like this:

```python
>>> client.send_email(
...     from_=f'Example Email <{client.email}>', 
...     to='my.neighbor@email.org',
...     subject='Yahoooo! 🤠',
...     body='Good morning neighbor! ☀️🏠🥓'
... )
```

For convenience, you can also create this at the instantiation and not have to think about it later:

```python
>>> # Name will be Donald <example@gmail.com>
>>> client = Client(
    email='akiro.trump@matsabushi.com', 
    name='Akiro Trump', 
    app_password=************
)
>>> # or from env vars
>>> client = gmail.from_env(name='AKIRO')  # OR set GMAIL_NAME as an environment variable
```

Then you can send an email without the `from_` argument and it will have your name in it.

---
