from typing import List


console_scripts: List[str] = [
    "pypathutil=pypathutil.main:main",
]
dev_requires: List[str] = [
    "pypitools",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pylogconf",
    "pytconf",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
