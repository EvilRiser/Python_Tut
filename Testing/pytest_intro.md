# Pytest

```
pip install -U pytest
```

Every pytest file and function should start with "test"  
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories
To run all the pytest files:
```
$ pytest
```
This will run all the files starting with test

if test passes then one "."(dot) will appear otheerwise F will appear for fail cases

Example of Pass cases
```
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.7.9, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: E:\Hustling\Python_Tut\Testing
collected 1 item

test_part1.py .                                                                                                                                                  [100%]

========================================================================== 1 passed in 0.08s ==========================================================================
```

Example of Fail cases
```
================================================= test session starts =================================================
platform win32 -- Python 3.7.9, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: E:\Hustling\Python_Tut\Testing
collected 1 item

test_part1.py F                                                                                                  [100%]

====================================================== FAILURES =======================================================
_____________________________________________________ test_answer _____________________________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_part1.py:7: AssertionError
=============================================== short test summary info ===============================================
FAILED test_part1.py::test_answer - assert 4 == 5
================================================== 1 failed in 0.31s ==================================================
```
Refer part1 for code


Here when the test case fail then fail report summary is also generated
----
Part 2

Use the raises helper to assert that some code raises an exception(refer part2)  

Execute the test function with “quiet” reporting (-q) mode:
```
pytest -q test_part2.py
```

