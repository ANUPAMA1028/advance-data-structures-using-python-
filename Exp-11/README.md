Experiment11: Brute Force Pattern Matching

Aim of the experiment - Write a program for implementing Brute Force pattern matching algorithm

procedure for the experiment:

The naive method is simply a brute force method of searching for the given substring in the main string. The method is to start looking for each letter in the main string. If the first letter of the supplied substring matches, we start an inner loop to check if all elements from substring match with the consecutive elements in the main string. That is, we simply see if the entire substring is present or not. If it is present, we return the starting index in the main string. The algorithm does well for small strings but consumes too much time for longer ones. Nevertheless, it helps us understand the basic idea of pattern search and is a good place to start. The time complexity of Naive Pattern Search method is O(m*n). The m is the size of pattern and n is the size of the main string.
