#TVGP Game Club

This repository stores the code and current suggestion, voted on, and picked lists for the TVGP Game Club. I've made this code open source mostly because I wanted to.

##Usage

This tool is used to automatically generate a new voting list, and automatically shuffle the existing or remaining game suggestions for TVGP Game Club.

To use:

* Make sure you have Python 2.7.x installed
* Open up cmd/PowerShell/Terminal
* Run the following command:
	* `python ListShuffler.py`

That's it! This will generatea new voting list (written to the `votinglists` directory), named with the date and time it was generated.

###Options

* **`-i`** (*String*): Specify an input file path. Defaults to `GamesRemaining.txt`.
	* `python ListShuffler.py -i /path/to/MyListOfGames.txt`
* **`-s`** (*Boolean*): If provided, will shuffle the parameters of the suggestions. Defaults to `False`.
	* `python ListShuffler.py -d`
* **`-c`** (*Integer*):  Specify the amount of games to add to the voting list. Cannot exceed the total number of games on the voting list. Defaults to `3`.
	* `python ListShuffler.py -c 5`

##Files

###GamesSuggested.txt
The master list of suggested games, taken from [this thread](http://tvgp.tv/forum/index.php?topic=5176.) on the TVGP forums.

###GamesRemaining.txt
The list of games that have not been put up for voting yet. Currently an exact copy of `GamesSuggested.txt`.

###GamesVoted.txt
The list of games that have been put up for voting already.

###GamesPicked.txt
Games that won their vote. This will be manually updated each time a Game Club voting thread is closed.

###ListShuffler.py
The actual script that shuffles, creates, and updates everything.
