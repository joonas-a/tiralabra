# Testing Document

### Unittesting

Currently the automatic tests test for successfull generation of the maze, and changing of it's properties.
Tests for finding if there are cycles within the maze are still work in progress. The UI is not being tested by unittests.

### Running the tests

Tests can be run by running

`poetry run invoke pytest`

Run tests & generate Coverage html report in the folder `htmlcov`

`poetry run invoke coverage`

### Coverage report

![Picture of Coverage report](https://github.com/joonas-a/tiralabra/blob/main/docs/coverage.png)
