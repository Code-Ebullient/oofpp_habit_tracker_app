# Habit Tracker App

## Table of Contents
1. [Introduction](#Introduction)
2. [Motivation](#Motivation)
3. [Goals](#Goals)
4. [Installation](#Installation)
5. [Flowchart](#Flowchart)
6. [Usage](#Usage)
7. [Features](#Features)
8. [Sample Habits](#Sample)
8. [Contributing](#Contributing)

## Introduction

The Habit Tracker App is a streamlined, user-centric application designed to help individuals build, manage, and maintain positive habits in their daily, weekly, and monthly routines. It provides a personalized interface for users to record, track, and complete habits while visualizing their progress and maintaining consistency through streak tracking. 


## Motivation
The project was inspired by the idea that habits are the foundation of personal growth, but most users struggle to stay consistent. By creating a tool that is both personalized and visually appealing, the app helps users stay on track with their goals. It was created for the *Object-Oriented and Functional Programming with Python*  Portfolio Course at the IU International University of Applied Sciences.


## Goals

1. Empower users to build healthy habits with personalized tracking.

2. Provide an intuitive, minimalist interface that simplifies habit management.

3. Encourage consistency through streak tracking and visual progress.

4. Ensure user data privacy with user-specific habit views.


## Installation

**Requirements:** 
Make sure you have Python 3.11+ installed on your computer. You can download the latest version of Python [here](https://www.python.org/downloads/). 

**Req. Package:**
* [streamlit](https://streamlit.io/#install) (Streamlit (Frontend GUI))
* SQLite (Database)


1. Clone or Download the repository from GitHub: https://github.com/Code-Ebullient/oofpp_habit_tracker_app
2. Install dependencies: 

```shell
pip install -r requirements.txt
```

3. Run the app:

```shell
streamlit run main.py
```


## Flowchart

[Visit App]
   ↓
[Enter Name] —→ (Already registered?) → [Dashboard]
   ↓                        ↓
[Register New User]        [Login]
   ↓                        ↓
[Dashboard: View/Add/Complete/Delete Habits]
   ↓
[Check progress → Analytics → Streaks/History]
   ↓
[Exit or Come Back Anytime]




## Usage:

1. Run `streamlit run main.py` to start the App. 

2. It loads to Streamlit Frontend GUI
      
   * Enter your name to begin.

   * Add habits using the input form.

   * Mark habits as completed using the "✅ Done" button.

   * Delete habits with the "❌" button.

   * Track your streaks for each habit.

   * Logout using the "🚪 Exit App" button. 



## Features

1. User-specific habit tracking: Each user can create and manage their own list of habits.

2. Habit categories: Daily, weekly, and monthly habits are supported.

3. Completion history: Track when each habit is completed.

4. Streak tracking: Automatically calculate and display the longest streak.

5. Interactive UI with Streamlit: Simple and intuitive interface.

6. SQLite Database: Secure, persistent storage for all user data.

7. User authentication (name entry): Personalized user experience.


## Sample Habits

The application comes with the following predefined habits for testing purpose:

* study (Daily)
* exercise (Daily)
* devotion (Daily)
* sport (Daily)
* grocery (Weekly)
* deep-cleaning (monthly)


## Contribution:

Feel free to fork this project and make improvements. Pull requests are welcome!
