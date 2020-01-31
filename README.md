# PUG: Recent and interesting features of Python (Jan 2020)

Talk at Python User Group on 30 Jan 2020.

Slides available on [Google Drive](https://docs.google.com/presentation/d/13O3DJCPsaf8xEANKX3t7Jn39OJPpit4V5OF-U2CPh_4/edit?usp=sharing)

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

Pull dependencies:

```bash
pipenv sync
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
