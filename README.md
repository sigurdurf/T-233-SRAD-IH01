# FizzBuzz TDD - IH01
This FizzBuzz program is available through the file sample.py.  

## Getting started
### Running the program
The FizzBuzz program itself has no requirements outside of the standard library. I assume you have python 3.6+ installed on your system.  
I advice you to create a virtual environment to simplify and isolate any issues that might occur.

```bash
$ python3 -m venv env && source env/bin/activate
```

### Testing
Running the tests requires the pytest module.  
If you skipped installing a virtual environment I advice you to do that now.
```bash
$ python3 -m venv env && source env/bin/activate
```
**This assumes you are running commands through bash. Windows activation script ends in .bat**

To add the pytest module to your system, install the requirements
```bash
$ pip install -r requirements.txt
```

To run the tests, simply run the following command
```bash
$ pytest
```

