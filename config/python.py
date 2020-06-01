import config.project

package_name = config.project.project_name

console_scripts = [
    'pypathutil=pypathutil.endpoints.main:main',
]

setup_requires = [
]

run_requires = [
    'pylogconf',  # for nicer logging
    'pytconf',  # for nicer logging
]

test_requires = [
    'pytest',  # for testing
    'pytest-cov',  # for test coverage
    'pylint',  # to linting
    'pyflakes',  # for linting
    'flake8',  # for linting
]

dev_requires = [
    'pyclassifiers',  # for programmatic classifiers
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.4"
