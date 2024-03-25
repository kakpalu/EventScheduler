import datetime
from dataclasses import dataclass


@dataclass
class Event:
    def __init__(self, title, date, description=""):
        self.title = title
        self.date = date
        self.description = description

    def __repr__(self):
        return f"Title: {self.title}, Date: ({self.date}),  Description: {self.description}"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Title cannot be empty.")
        self._title = title

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, datetime.date):
            try:
                date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                self._date = date
            except ValueError:
                raise ValueError("Date must be a valid date object.")
        self._date = date

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
        }
