# plz-cover-py3

test plz py3 coverage

```bash
✗ plz cover
Fail: //:tests   0 passed   0 skipped   0 failed   1 errored Took 450ms
Error: TestFailed in tests
Test failed
signal: segmentation fault
//:tests 1 test run in 450ms; 0 passed, 1 errored
1 test target and 1 test run; 0 passed, 1 errored.
Total time: 550ms real, 450ms compute.
Messages:
15:13:24.151   ERROR: //:tests failed: Test failed
Coverage results:
envutil/envutil:
  envutil.py 0/29 lines, 0.0%
Total coverage:  0/29 lines, 0.0%

✗ plz cover --shell
Temp directories prepared, total time 50ms:
  //:tests: /{redacted}/plz-cover-py3/plz-out/tmp/tests._test/run_1
    Command: $TEST

bash-5.1$ ls
tests           tests.pex
bash-5.1$ ./tests.pex
Segmentation fault: 11
bash-5.1$ exit
exit
Coverage results:
envutil/envutil:
  envutil.py 0/29 lines, 0.0%
Total coverage:  0/29 lines, 0.0%
```

```bash
✗ ./plz-out/bin/tests.pex
===================================================================== test session starts ======================================================================
platform darwin -- Python 3.9.2, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /{redacted}/plz-cover-py3
collected 2 items

tests/test_env_to_str.py ..                                                                                                                              [100%]

======================================================================= warnings summary =======================================================================
plz-out/bin/tests.pex/.bootstrap/_pytest/junitxml.py:436
  /{redacted}/plz-cover-py3/plz-out/bin/tests.pex/.bootstrap/_pytest/junitxml.py:436: PytestDeprecationWarning: The 'junit_family' default value will change to 'xunit2' in pytest 6.0.
  Add 'junit_family=xunit1' to your pytest.ini file to keep the current format in future versions of pytest and silence this warning.

-- Docs: https://docs.pytest.org/en/latest/warnings.html
---------------------------------------- generated xml file: /{redacted}/plz-cover-py3/test.results/results.xml ----------------------------------------
================================================================= 2 passed, 1 warning in 0.01s =================================================================
➜  plz-cover-py3 git:(main) ✗
```
