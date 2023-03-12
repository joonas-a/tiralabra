# Testing Document

### Automatic tests

The automatic unittests test for successful maze generation, changing it's size, and that no cell has been left unvisited after running either of the algorithms.
The UI/mainloop/performance test module is not being tested.

#### Coverage report

![Picture of Coverage report](https://github.com/joonas-a/tiralabra/blob/main/docs/images/coverage.png)

### About the algorithms

Both the Kruskal's algorithm and the backtracker function by finding unvisited cells, and adding them to the main path if applicable.
This in itself guarantees every cell of the maze being reachable from every cell, assuming all cells have been visited, which is what is being tested.
Both algorithms also make sure there won't be any cycles within the maze, by refusing to connect two paths together should there already be a path between them.

### Performance testing

For testing purposes there is a separate CLI application for easily running performance tests without visualizing the mazes, for mazes of any size and any number of times.
Below are some test results that I've run for mazes sized 10x10, 100x100, 1000x1000 and 5000x5000.

![Performance test for a 10x10 maze](https://github.com/joonas-a/tiralabra/blob/main/docs/images/10_result.png)

![Performance test for a 100x100 maze](https://github.com/joonas-a/tiralabra/blob/main/docs/images/100_result.png)

Both algorithms only took a fraction of a second when the maze size was in the tens-hundreds, with the backtracker being about 40% faster than the Kruskal's algorithm.


![Performance test for a 1000x1000 maze](https://github.com/joonas-a/tiralabra/blob/main/docs/images/1000_result.png)

When maze size starts being in the thousands-range, the runtime started to drastically get slower, with the Kruskal's algorithm taking nearly 5 minutes with a maze sized 5000x5000. At that state the backtracker was nearly 2/3s faster.

![Performance test for a 5000x5000 maze](https://github.com/joonas-a/tiralabra/blob/main/docs/images/5000_result.png)

### To run the tests

Performance-testing CLI application can be run with

`poetry run invoke performance`

The application will ask for maze width/height + the amount of iterations, and will return the results as seen above.
*Noteworthy: the performance tester application has no input validation, running with large parameters will take a very long time.*

Automatic unittests can be run with

`poetry run invoke pytest`

Run automated tests & generate Coverage html report in the folder `htmlcov`

`poetry run invoke coverage`

