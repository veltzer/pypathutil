import config.project

package_name = config.project.project_name

console_scripts = [
    "pypathutil=pypathutil.main:main",
]

run_requires = [
    "pylogconf",
    "pytconf",
]

test_requires = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "pymakehelper",
]

dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
