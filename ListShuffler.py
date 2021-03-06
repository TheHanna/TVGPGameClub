import argparse
import os
import random
import time
import msvcrt

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
    random.shuffle(sug_list)
    print '\n' + args.sug_list + ' shuffled!\n'  # Notify list shuffled
    return sug_list


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


def confirmVoteList(sug_list, vote_list):
    print '\n'.join(vote_list) + '\n'
    print 'Are these the suggestions you want to use (y or n)?\n'
    choice = msvcrt.getch().lower()
    print choice + '\n'
    if choice == 'y':
        # Write vote list file
        new_vote_list_path = writeNewVoteListFile(vote_list)
        # Notify new vote list created
        print new_vote_list_path + ' created!\n\n'
        updateVoted(vote_list)  # Update GamesVoted.txt
        updateRemaining(sug_list, vote_list)  # Update GamesRemaining.txt
        # Notify of vote list contents and their addition/removal from
        # certain files
        print 'The following games were added to GamesVoted.txt and removed f'\
            'rom GamesRemaining.txt:\n\n'\
            + '\n'.join(vote_list) + '\n'
        print 'Finished!'  # Print that the script has finished running
        return True
    if choice == 'n':
        confirmExit()
        return True
    else:
        print '\nPlease respond with y or n\n'
        confirmVoteList(sug_list, vote_list)


def confirmExit():
    print 'Would you like to see a new list of games?\n'
    choice = msvcrt.getch().lower()
    print choice
    if choice == 'y':
        sug_list = getSuggestions(args.sug_list)
        vote_list = getNewVoteData(sug_list, args.count)
        confirmVoteList(sug_list, vote_list)
        return True
    if choice == 'n':
        print '\nFinished, but no changes were made!'
        return True
    else:
        print '\nPlease respond with y or n\n'
        confirmExit()

# Start program
sug_list = getSuggestions(args.sug_list)  # Initialize suggestion list
vote_list = getNewVoteData(sug_list, args.count)  # Initialize vote list
confirmVoteList(sug_list, vote_list)
