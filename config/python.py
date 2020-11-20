import config.project

package_name = config.project.project_name

console_scripts = [
    'pypathutil=pypathutil.main:main',
]

setup_requires = [
]

run_requires = [
    'pylogconf',
    'pytconf',
]

test_requires = [
    'pytest',
    'pytest-cov',
    'pylint',
    'flake8',
    'pymakehelper',
]

dev_requires = [
    'pyclassifiers',
    'pypitools',
    'pydmt',
    'Sphinx',
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
}
test_os = "[ubuntu-16.04, ubuntu-18.04, ubuntu-20.04]"
test_python = "[3.6, 3.7, 3.8]"
test_container = "[ 'ubuntu:18.04', 'ubuntu:20.04' ]"
