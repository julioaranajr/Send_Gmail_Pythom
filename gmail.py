"""
Description:
A simple Gmail client that sends emails using the Gmail API.
The code is a simple Python class that uses the Gmail API to send emails.

The Client class is a dataclass that represents a Gmail client. 
It has three fields: email, app_password, and name. 
The email field is the Gmail address of the client, 
the app_password field is the app password of the client, and 
the name field is the name of the client.

The Email class is a dataclass that represents an email.
It has four fields: from_, to, subject, and body.
The from_ field is the email address of the sender,
the to field is the email address of the recipient,
the subject field is the subject of the email, and
the body field is the body of the email.

Attributes:
    email (str): The Gmail address of the client.
    app_password (str): The app password of the client.
    name (str): The name of the client.
    from_ (str): The email address of the sender.
    to (str): The email address of the recipient.
    subject (str): The subject of the email.
    
Methods:
    __str__(): Returns the email address of the client.
    __repr__(): Returns the string representation of the GmailClient object.
    validate_email_is_gmail(cls, email: str): Validates the email address of the client.
    validate_app_password(cls, app_password: str): Validates the app password of the client.
    from_env(cls): Creates a GmailClient object from the environment variables.
    from_(self): Returns the email address of the sender.
    send_email(self, to: str | list[str], subject: str, body: str, from_: str | None = None): Sends an email.
    __str__(self): Returns the string representation of the Email object.
"""
from __future__ import annotations

import os
import smtplib
from dataclasses import dataclass

from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator


class Client(BaseModel):
    email: str
    app_password: str = Field(..., repr=False)
    name: str | None = Field(default=None, description=None)

    def __str__(self):
        return self.from_

    def __repr__(self):
        return f'<GmailClient {self.from_}>'

    @classmethod
    @field_validator('gmail')
    def validate_email_is_gmail(cls, email: str):
        if not email.endswith('@gmail.com'):
            raise ValueError('Email must be a Gmail address')
        return email

    @classmethod
    @field_validator('app_password')
    def validate_app_password(cls, app_password: str):
        if not len(app_password) in (16, 19):
            feedback = 'App password must be 16 or 19 characters long'
            help_link = 'https://support.google.com/accounts/answer/185833?hl=en'
            raise ValueError(f'{feedback}. For more information, visit {help_link}')
        return app_password

    @classmethod
    def from_env(cls):
        load_dotenv(override=True)
        return cls(
            email=os.getenv('GMAIL_EMAIL'),
            app_password=os.getenv('GMAIL_APP_PASSWORD'),
            name=os.getenv('GMAIL_NAME'),
        )

    @property
    def from_(self) -> str:
        return f'{self.name} <{self.email}>' if self.name else self.email

    def send_email(self,  to: str | list[str], subject: str, body: str, from_: str | None = None):
        from_ = from_ or self.from_
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(
                user=self.email,
                password=self.app_password,
            )
            for email_address in to if isinstance(to, list) else [to]:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email_address,
                    msg=str(Email(from_=from_, to=email_address, subject=subject, body=body)).encode('utf-8'),
                )


@dataclass
class Email:
    from_: str
    to: str
    subject: str
    body: str

    def __str__(self):
        return f'From: {self.from_}\nTo: {self.to}\nSubject: {self.subject}\n\n{self.body}'
    