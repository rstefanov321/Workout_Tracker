# Workout_Tracker
An application, which uses a Natural Language Processing API (https://developer.nutritionix.com/login) to distinguish the types of sports you have done over the day. Initially, you are supposed to input your physical data like gender, weight in kg, height in cm and age. 

The program also fetches the data and records it into a Google Spreadsheet with time and date. Multiple types of data can be extracted from the Nutritionix API, so this is only a demo. 

The authorization variables are turned into environment variables, so the "os" module is used to fetch them. 
