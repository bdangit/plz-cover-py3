python_library(
  name = 'envutil',
  srcs = [
    "envutil/envutil/envutil.py",
  ],
  visibility = ["PUBLIC"],
)

python_test(
  name = 'tests',
  srcs = [
    "tests/test_env_to_str.py",
    # "tests/test_env_to_file.py",
    # "tests/test_str_to_file.py",
  ],
  deps = [
    ":envutil",
    # "//third_party/python:pyfakefs",
  ]
)
