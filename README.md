A showcase of using taretto framework.

These tests written for the sample microblog application https://github.com/quarckster/microblog.
There are two file with tests: [tests_basic.py](https://github.com/quarckster/microblog_tests/blob/master/mt/tests/tests_basic.py) and [tests_basic_old.py](https://github.com/quarckster/microblog_tests/blob/master/mt/tests/tests_basic_old.py). The first one shows taretto based tests and the second one implements
the same tests in raw selenium calls.

Prerequisites
=============

Install and [run](https://github.com/quarckster/microblog#run) the application before running the tests.


Install
=======

`python setup.py install`


Run
===

`pytest -v mt/tests`