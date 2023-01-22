# Project specification (määrittelydokumentti)

**Study programme: tietojenkäsittelytieteen kandidaatti (TKT)**

This project will be written in **English** using the programming language **Python**

I can do code reviews in both **Finnish** or **English**

## Maze generator

Aim of this project is to create an application capable of generating and displaying (both while generating and while finished) a maze using at least two different maze generating algorithms, possibly to compare the overall effectiveness of said algorithms.

### Algorithms I will be using

Randomized Kruskal's algorithm *O(E log E)*

Recursive backtracker (iterative DFS) algorithm *O(|C|+|E|)*

*where E are the edges and C the cells (10x10 maze would result in 100 cells)*

Both of these were often brought up when researching about maze generation. The way they also generate mazes differ a lot from each other, so I feel they're a fair pair for comparison.

Other algorithms which (one or both) could potentially be implemented are the Hunt-and-Kill algorithm and/or the Wilson's algorithm.

### The application

User can alter the size of the maze, start/finish nodes, and select the wanted algorithm. Possibly also slow down the algorithm to better visualize what it's doing.

App will generate/display the maze and possibly some other relevant data (at least runtime of the algorithm)

### Resources

[Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

[Kruska's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

[Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)

[StackOverflow](https://stackoverflow.com/questions/38502/whats-a-good-algorithm-to-generate-a-maze)
