# example package

```bash
python3 -m build
pip install -e .
```

## for uploading to pypi artifactory
```bash
python setup.py sdist
twine upload dist/*
```