#TVGP Game Club

This repository stores the code and current suggestion, voted on, and picked lists for the TVGP Game Club. I've made this code open source mostly because I wanted to.

##Usage

This tool is used to automatically generate a new voting list, and automatically shuffle the existing or remaining game suggestions for TVGP Game Club.

To use:

* Make sure you have Python 2.7.x installed
* Open up cmd/PowerShell/Terminal
* Run the following command:
	* `python ListShuffler.py -s`

That's it! This will generate a new voting list (written to the `votinglists` directory), named with the date and time it was generated. It will also shuffle the GamesRemaining.txt list

###Options

* **`-i`** (*String*): Specify an input file path. Defaults to `GamesRemaining.txt`.
	* `python ListShuffler.py -i /path/to/MyListOfGames.txt`
* **`-c`** (*Integer*):  Specify the amount of games to add to the voting list. Cannot exceed the total number of games on the voting list. Defaults to `3`.
	* `python ListShuffler.py -c 5`

##Files

###GamesSuggested.txt
The master list of suggested games, taken from the [TVGP forums](http://tvgp.tv/forum).

###GamesRemaining.txt
The list of games that have not been put up for voting yet.

###GamesVoted.txt
The list of games that have been put up for voting.

###GamesPicked.txt
Games that won their vote. This will be manually updated each time a Game Club voting thread is closed.

###ListShuffler.py
The actual script that shuffles, creates, and updates everything.
