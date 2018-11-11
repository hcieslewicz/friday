# Friday
Task for Friday

## Getting Started

Get the copy of this example using git:
```
git clone https://github.com/hcieslewicz/friday.git
```

### Prerequisites

To have it running You need to have:
* Python 2.7 - python - https://www.python.org/
* Pytest - Python testing tool - pip install selenium pytest

## Running the tests

To run the test You have to just call pytest from the main directory. On Windows open command prompt and type:

```
pytest 
```

## Test examples
Test are checking if input string (combined street name and house number) is properly splitt into two separate filed in json format.
In this code example only two regular expressions were used, but in the same time this does not cover last test case ("Calle 39 No 1540"), which may be achived by split first regex into two separate.
To see this failing test, just go to test_address.py and uncomment line with the assertion.

## Authors

* **Hubert Cieslewicz** (https://github.com/hcieslewicz)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
