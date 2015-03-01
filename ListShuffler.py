import argparse
import os
import random
import time

# Set up the parser for the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '-i',
    '--sug_list',
    type=str,
    default=os.path.dirname(__file__) + 'GamesRemaining.txt',
    help='Path to list of user-suggested games to shuffle.'
)
parser.add_argument(
    '-s',
    '--do_shuffle',
    action='store_true',
    help='Boolean flag--if true, shuffle suggestions before generating new '
         'vote list. If false, skip shuffling and just generate vote list.'
)
parser.add_argument(
    '-c',
    '--count',
    type=int,
    default=3,
    help='Number of items to put on the vote list'
)

args = parser.parse_args()  # Store the command line arguments
creation_time = time.strftime('%Y%m%d%H%M%S')  # Get current time


def getSuggestions(path):
    sug_list_file = open(path, 'r')  # Open suggestion list file
    sug_list = [  # Store all lines in the suggestion list
        line.rstrip('\n') for line in sug_list_file.readlines()
    ]
    sug_list_file.close()  # Close suggestion list file
    if args.do_shuffle is True:
        random.shuffle(sug_list)
    return sug_list


def writeNewSuggestionsFile(sug_list, voted_list):
    new_sug_list_path = os.path.join(  # Define new suggestion list path
        os.path.dirname(__file__) + 'suggestionlists',
        'GamesSuggestedShuffled-' + creation_time + '.txt'
    )

    # Open new suggestion file
    new_sug_list_file = open(new_sug_list_path, 'w')
    for sug in sug_list:  # Write new suggestion list
        if sug not in voted_list:
            new_sug_list_file.write(sug+'\n')
    new_sug_list_file.close()  # Close new suggestion list
    return new_sug_list_path


def getNewVoteData(sug_list, count):
    if count > len(sug_list):
        count = len(sug_list)

    vote_list = []  # Create empty vote list

    for sug in sug_list[:args.count]:  # Add items to vote list based on count
        vote_list.append(sug)
    return vote_list


def writeNewVoteListFile(vote_list):
    vote_list_path = os.path.join(  # Define vote list path
        os.path.dirname(__file__) + 'votelists',
        'VoteList-' + creation_time + '.txt'
    )

    vote_list_file = open(vote_list_path, 'w')  # Open new suggestion file
    for vote in vote_list:  # Write new suggestion list
        vote_list_file.write(vote+'\n')
    vote_list_file.close()  # Close suggestion list
    return vote_list_path


def updateVoted(vote_list):
    voted_path = os.path.join(  # Define voted_file path
        os.path.dirname(__file__),
        'GamesVoted.txt'
    )
    voted_file = open(voted_path, 'a')  # Open voted_file
    for vote in vote_list:  # Write votes to file
        voted_file.write(vote+'\n')
    voted_file.close()  # Close voted_file
    return voted_path


def getVoted():
    voted_path = os.path.join(  # Define voted_file path
        os.path.dirname(__file__),
        'GamesVoted.txt'
    )
    voted_file = open(voted_path, 'r')  # Open voted_file
    voted_list = [line.rstrip('\n') for line in voted_file.readlines()]
    voted_file.close()  # Close voted_file
    return voted_list


def updateRemaining(sug_list, vote_list):
    rem_path = os.path.join(
        os.path.dirname(__file__),
        'GamesRemaining.txt'
    )
    # Build new remaining list
    rem_list = [item for item in sug_list if item not in vote_list]
    rem_file = open(rem_path, 'w')  # Open rem_file
    for rem in rem_list:  # Write remaining suggestions to file
        rem_file.write(rem+'\n')
    rem_file.close()

# Start program
sug_list = getSuggestions(args.sug_list)  # Initialize suggestion list
vote_list = getNewVoteData(sug_list, args.count)  # Initialize vote list
new_vote_list_path = writeNewVoteListFile(vote_list)  # Write vote list file
updateVoted(vote_list)  # Update GamesVoted.txt
updateRemaining(sug_list, vote_list)  # Update GamesRemaining.txt

if args.do_shuffle:
    print '\n' + args.sug_list + ' shuffled!\n'  # Notify remaining shuffled
    print args.sug_list + ' updated!\n'  # Notify remaining updated
print new_vote_list_path + ' created!\n\n'  # Notify new vote list created
# Notify of vote list contents and their addition/removal from cretain files
print 'The following games were added to GamesVoted.txt and removed from '\
      'GamesRemaining.txt:\n\n'\
      + '\n'.join(vote_list) + '\n'
# Notify of script run completion
print 'Finished!'  # Print that the script has finished running
