Create python venv
  - python -m venv name
  - virtualenv name
  - pipenv install (requirements.txt)

Build package
  - pip install (with setup.py)
  - python -m build
  - python setup.py sdist bdist_wheel
  

View contents of python package:
tar tf dist/*.tar.gz 
unzip -l dist/*.whl


```pip install -e . (after sourcing .venv)
python -m <package name> (runs stuff in __init__.py)```

pyspark
`docker run -it --rm -p 8888:8888 -v /Users/user/Documents/AWS_Glue_Jobs:/home/jovyan/work jupyter/pyspark-notebook`
