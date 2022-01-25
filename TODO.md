# Cookbook-App

This repository stores and versions my work formatting recipes in mom's CookBook App.

## Need to Start

## In Progress

## Completed

- [X] `RecipeNoteScraper`
    - [X] Grab title of recipe
    - [X] Write text file
        - [X] Title the file into a file-safe format
        - [X] Save file to a specific directory
    - [X] Create file path list for all HTML files.

- [X] `RecipeScraper`
    - [X] Grab title
    - [X] Get the notes as a `ResultSet`
    - [X] Load a text root directory as an argument
    - [X] Process the `ResultSet` note object into a `str`
        - [X] Replace the `<br>` tags with newlines (`\n`).
    - [X] Save the note `str` as a text file.
        - [X] Make a file name safe `str` to name the text file.
        - [X] Create an absolute file path to save the text file to the text directory.
