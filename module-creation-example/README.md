# example package

```bash
python3 -m build
pip install -e .
```

## for uploading to pypi artifactory
```bash
python setup.py sdist or python setup.py bdist_wheel or poetry build
twine upload dist/*
```