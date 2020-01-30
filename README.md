# What's new in Python (Jan 2020)

## Preqrequisites

Install pyenv and Python 3.8 on Mac:

```bash
brew upgrade pyenv
pyenv install --list
pyenv install 3.8.1
```

Install pipenv:

```bash
pip install pipenv
```

## Run Jupyter notebook

```bash
pipenv run jupyter notebook --notebook-dir=./examples
```

## Run examples

```bash
pipenv run python examples/10_debugging.py
pipenv run python examples/15_sharedmem_duplication.py
pipenv run python examples/15_sharedmem_shared.py
```
