'''
Given a sorted dictionary of an alien language, find order of characters
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.


The idea is to create a graph of characters and then find topological sorting of the created graph. Following are the
detailed steps.

1) Create a graph g with number of vertices equal to the size of alphabet in the given alien language. For example,
if the alphabet size is 5, then there can be 5 characters in words. Initially there are no edges in graph.

2) Do following for every pair of adjacent words in given sorted array.
…..a) Let the current pair of words be word1 and word2. One by one compare characters of both words and find the first
mismatching characters.
…..b) Create an edge in g from mismatching character of word1 to that of word2.

3) Print topological sorting of the above created graph.

Following is the implementation of the above algorithm.
'''

import CdataS.Graph.graphclass as graph

##     // This function fidns and prints order of characer from a sorted
# // array of words. n is size of words[].  alpha is set of possible
# // alphabets.
# // For simplicity, this function is written in a way that only
# // first 'alpha' characters can be there in words array.  For
# // example if alpha is 7, then words[] should have only 'a', 'b',
# // 'c' 'd', 'e', 'f', 'g'
def printOrder(words):
    #// Create a graph with 'aplha' edges
    g = graph.Graph()
    n = len(words)
    #// Process all adjacent pairs of words and create a graph
    for i in range(n-1):

        # // Take the current two words and find the first mismatching
        # // character
        word1 = words[i]
        word2 = words[i+1]
        for j in range(0, min(len(word1), len(word2))):

            # // If we find a mismatching character, then add an edge
            # // from character of word1 to that of word2
            if word1[j] != word2[j]:
                g.add_edge(word1[j], word2[j])
                break


    #// Print topological sort of the above created graph
    g.topologicalSort()

#// Driver program to test above functions
#words = ["caa", "aaa", "aab"]
words = ["baa", "abcd", "abca", "cab", "cad"]
printOrder(words)
