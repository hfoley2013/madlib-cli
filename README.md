# LAB - Class 3

## Project: MadLibs

## Author: Harper Foley

## Links and Resources

* [GitHub Repo](https://github.com/hfoley2013/madlib-cli)

### Setup

* To set up this repo create a local repository on your machine
* Create a virtual environment for Python
  * `python3.11 -m venv .venv`
* Activate the venv file
  * `source .venv/bin/activate`
* Install `pytest` and `pytest-watch`
  * `pip install pytest pytest-watch`
* Use `git clone` to clone the repo to your local machine
  * `git clone https://github.com/hfoley2013/madlib-cli.git`
* Your repo is now ready to run the Madlibs program

### How to initialize/run

* To run the test scripts:
  * Run `pytest` in the CLI
* To run the program:
  * Run `python3.11 ./modules/madlib.py`
  * Answer the prompts in order to see a print out of a videogame script using your inputs

### Tests

* How do you run tests?
  * Tests are conducted via `pytest`
  * There are four tests total that verify that each of the three main function operate correctly
    * `test_read_template_returns_stripped_string` tests that `read_template` grabs the correct file based on file path.
    * `test_parse_template` tests that `parse_template` correctly separates content contained within `{ }` out of the template and stores them as a separate tuple.
    * `test_merge` tests that `merge` correctly stitches together the users inputs into the parsed template.
    * `test_read_template_raises_exception_with_bad_path` tests that `read_template` raises an exemption whenever an invalid file path is entered.