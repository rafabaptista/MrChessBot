**Version 2.5.1**
---
* \[New\] PR Template.
* \[Edit\] Update Readme file.

**Version 2.5.0**
---
* \[New\] English translation for daily tournaments message to all.

**Version 2.4.1**
---
* \[Fix\] Fix Arena tournament creation due to Lichess Api POST changes
* \[Fix\] Fix Message to All from Teams due to Lichess Api POST changes

**Version 2.4.0**
---
* \[New\] Support Team Name and Team ID by config vars
* \[Fix\] Fix tournament creation in the last days of the month
* \[Remove\] Remove WhatsApp send message support (cost matters)
* \[Remove\] Remove unnesed code and classes

**Version 2.3.1**
---
* \[Fix\] Fix tournament creation for the last day of the year
* \[Remove\] Remove WhatsApp send message support (cost matters)

**Version 2.3.0**
---
* \[New\] Challenge MrChessTheBot Lichess BOT -> .bot

**Version 2.2.0**
---
* \[New\] Send message to WhatsApp group
* \[New\] Send message to Tournament Discord Channel

**Version 2.1.3**
---
* \[Update\] Allow comma(,) in extra messages for tournament list creation

**Version 2.1.2**
---
* \[Update\] Change message for failure tournament creation
* \[Fix\] Remove special characters that doesn`t work in Lichess Messages

**Version 2.1.1**
---
* \[Fix\] Trick for midnight hours

**Version 2.1.0**
---
* \[New\] Support MongoDB
* \[New\] New way to create tournaments integrated with DB
* \[New\] CRUD for tournaments

**Version 2.0.3**
---
* \[New\] Add New tournament list -> .torneio-p5
* \[Update\] Decrease sleep between tournament list creation to 1 second
* \[Fix\] Fix for .torneio-p1

**Version 2.0.2**
---
* \[Fix\] Specify Intents all() to start Discord Client for bot events


**Version 2.0.1**
---
* \[Fix\] Specify Intents to start Discord Client

**Version 2.0.0**
---
* \[New\] New Main, based on Discord.py Commands
* \[New\] Using Discord embed messages to be more pretty

**Version 1.3.2**
---
* \[New\] Tournament Creation Support -> .swiss / .arena
* `.swiss <title>, <description (can be a .jpg image url)>, <clock(in minutes)>, <increment(in seconds)>, <rounds>, <interval(in seconds)>, <hour(default 0-23 hours)>, <minutes(default 0-60 minutes)>` → create Swiss tournament based
* `.arena <title>, <description(can be a .jpg image url)>, <clock(in minutes)>, <increment(in seconds)>, <duration (in minutes)>, <hour(default 0-23 hours)>, <minutes(default 0-60 minutes)>` → create Swiss tournament