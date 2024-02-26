# Introduction

## The Premise

This project came to me as an idea some time ago while I was shopping and contemplated my concerningly large collection of Tesco receipts and how quickly the ink on them rubbed off, making it impossible to look back on my purchases and money sinks. It came to me to make a more time-durable form of storage for those receipts. This is what I aim to achieve with this application. A snap-and-go approach to receipts where a user can just scan their receipts with a smartphone and use an application not too dissimilar from banking applications, but keeping track of the individual products and prices instead of just the total price charged at the end.

## Alternatives

Unsurprisingly, other developers have also had the same idea and created such applications, but in my experience those applications are paid or riddled with ads and micro-transactions when free. Regardless, it makes for a great exercise of my software development skills.

## The Pitch

*What will this application be?*

- I plan on making the application cross-platform, with the backend of the application made in python, and a frontend made in either MAUI or Avalonia using .NET. The mobile app will be the main focus, with the ability to scan receipts from photos and possibly tailored to account for human error when taking them, like incorrect rotation. Those receipts will be stored in a database and viewable in-app with the ability to export to other formats (txt and csv or xlsx for use in excel, most likely csv). If I have time, I will also make a desktop app, more geared towards printer-scanned receipts (using a webcam to scan 50 receipts sounds like a nightmare).

### The Language Issue

*Why use a different language for the UI when everything else will use python?*

- I have personally never been fond of making UI in python, be it Tkinter or mobile-wise. Instead, I have a preference for C# when it comes to making UI. I also have more experience in it, so I would spare myself the time of learning another UI framework and reinventing the proverbial wheel.

*Then why not just use C# for the whole project?*

- Simply put, python is just easier and quicker to develop with. This project is under a time constraint, so reaching funcitonality as quickly as possible is crucial so I can add as many additional features (such as reading receipts from other sellers, statistics and price tracking) as possible. When working with C#, code tends to feel more verbose and stringlently written with type checking and other caveats. Meanwhile python is as plug-and-play as it gets, which makes reaching a full-feature state more realistic given my lack of experience with OCR and finishing projects of this scale.

## The Libraries

TODO: Write this

### MAUI

### Avalonia

### Tesseract

### OpenCV

### PIL

### MySQL

### SQLite
