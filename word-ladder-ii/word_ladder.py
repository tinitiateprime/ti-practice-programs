from collections import defaultdict, deque

def find_ladders(beginWord, endWord, wordList):
    """
    Given a beginWord, endWord, and a dictionary's word list, 
    return all shortest transformation sequences from beginWord to endWord.

    Args:
        beginWord (str): The starting word.
        endWord (str): The ending word.
        wordList (list): A list of words.

    Returns:
        list: A list of all shortest transformation sequences from beginWord to endWord.
    """

    # Convert wordList to a set for faster membership checks
    word_set = set(wordList)

    # If endWord is not in the word list, return an empty list
    if endWord not in word_set:
        return []

    # Initialize the layer with the beginWord
    layer = defaultdict(list)
    layer[beginWord] = [[beginWord]]

    while layer:
        new_layer = defaultdict(list)  # Create a new layer for the next level of words

        # Iterate over each word in the current layer
        for word in layer:

            # If the word is the endWord, return all paths
            if word == endWord:
                return layer[word]

            # Generate all possible transformations of the word
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]

                    # If the new word is in the word list, add it to the new layer
                    if new_word in word_set:
                        new_layer[new_word] += [j + [new_word] for j in layer[word]]

        # Remove words that have been visited from the word list
        word_set -= set(new_layer.keys())

        # Update the current layer with the new layer
        layer = new_layer

    return []

# Example usage:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(find_ladders(beginWord, endWord, wordList))  # Print all shortest transformation sequences
