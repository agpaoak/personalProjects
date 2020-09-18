import sys
import os

from task import Task
from random import randint
from collections import OrderedDict
from datetime import datetime, time

from peewee import * 

db = SqliteDatabase('habits.db')

class Habit(Model):
    task = TextField()
    duration = TextField() # X reps / time
    # Need to add random time of day to do it
    # Need to add time created

    class Meta:
        database = db

# Clears console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Shows menu
def menu_loop():
    """Show menu"""
    choice = None

    while choice != 'q':
        print('Welcome! This will create a randomized time to do a task.')
        print('The aim of this is build habits slowly.')
        print('Instead of tracking habits, we will build them.')
        print('So this is a habit building app.')
        print ('Please enter a task to do for a certain duration')
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

def view_entries():
    """View entries"""
    # View entries one by one
    # Break out if I don't want to see this anymore
    for habit in Habit.select():
        print(f'At do {habit.task} for {habit.duration}')
        temp = input('Would you like to see next [Yn]? ')
        clear()

        if temp == 'n':
            break

def add_entry():
    """Add an entry"""
    print('Adding Entry')
    action = input('Enter an action: ').lower().strip()
    duration = input('Enter a duration: ').lower().strip()

    habit = Task(action, duration)


    print(f'At {habit.time} do {habit.task} for {habit.duration}')

    h = Habit.create( task = habit.task,
                    duration = habit.duration) # Need time of creation

    print("Habit saved")
    h.save


db.connect()
db.create_tables([Habit])

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries)
])

menu_loop()