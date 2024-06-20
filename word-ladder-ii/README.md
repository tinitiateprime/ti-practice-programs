# Word Ladder II
* Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequences from beginWord to endWord, such that:
    * Only one letter can be changed at a time.
    * Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

# Word Ladder II
This project implements the Word Ladder II problem, which finds all the shortest transformation sequences from a `beginWord` to an `endWord`, given a dictionary of words. The transformation sequence must follow the rules where only one letter can be changed at a time, and each transformed word must exist in the word list.

## Files

- `word_ladder.py`: Contains the main code for solving the Word Ladder II problem.

## Functions
### `find_ladders(beginWord, endWord, wordList)`
Finds all shortest transformation sequences from `beginWord` to `endWord`.

#### Arguments

- `beginWord` (str): The starting word.
- `endWord` (str): The ending word.
- `wordList` (list): A list of words.

#### Returns

- `list`: A list of all shortest transformation sequences from `beginWord` to `endWord`.

#### Description

- Converts the word list to a set for faster membership checks.
- Checks if `endWord` is in the word list; returns an empty list if it is not.
- Uses breadth-first search (BFS) to explore all possible transformations level by level.
- Generates all possible one-letter transformations of each word.
- Builds new layers of transformations until the `endWord` is reached.
- Returns all transformation sequences that end with `endWord`.

## Usage

- Import the `find_ladders` function from the `word_ladder.py` file.
- Call the function with the `beginWord`, `endWord`, and `wordList`.