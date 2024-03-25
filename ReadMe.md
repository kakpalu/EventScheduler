## Event Scheduler
The Event Scheduler is a Python script designed to manage events, allowing users to add, remove, and list events through a command-line interface. The script uses object-oriented programming principles, handles errors gracefully, and includes data persistence by saving events to and loading events from a JSON file.

## Features
Add Event: Users can add events with a title, date (in YYYY-MM-DD format), and an optional description.  
Remove Event: Events can be removed by specifying their title.  
List Events: All events are listed sorted by their dates in ascending order.

## Requirements
Python 3.x  
JSON module (built-in)  
Command-line interface (CLI) or script execution environment

## Usage
Run the Script: Execute the script using Python:
```bash
python entry.py
```

Choose Options: Follow the prompts to add, remove, or list events.  
Quit: Choose the option to quit to save events and exit the application.

## Example
```
Options:
1. Add Event
2. Remove Event
3. List Events
4. Quit
Enter your choice: 1
Enter event title: Meeting
Enter the date (YYYY-MM-DD): 2024-03-30
Enter event description (optional): Team meeting
Event added successfully.

Options:
1. Add Event
2. Remove Event
3. List Events
4. Quit
Enter your choice: 3
Title: Meeting, Date: (2024-03-30),  Description: Team meeting

Options:
1. Add Event
2. Remove Event
3. List Events
4. Quit
Enter your choice: 4
Events saved successfully. Exiting ...
```

## Data Persistence
The script uses a JSON file named events.json to persist events. Events are saved to this file when the user quits the application, and they are loaded from the same file when the application starts.
Also for any write operation the script saves the events to the file.


## Author
Kafui Akpalu