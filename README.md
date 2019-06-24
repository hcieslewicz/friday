# Friday
Example of using pytest for testing split street name and_number

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
In this code example three regular expressions were used. There is also solution using 2 expression, but it's commented in regression list place, casue of usual rule: simpler is better.


## Authors

* **Hubert Cieslewicz** (https://github.com/hcieslewicz)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
