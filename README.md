# sgcharts-stringx

Utility functions for strings

## Usage 

Add this library as a dependency in `setuptools`.

Example `setup.py`

```python
install_requires=[
    'sgcharts-stringx',
    ...
],
dependency_links=[
    'git+https://github.com/seahrh/sgcharts-stringx.git@master#egg=sgcharts-stringx-1.0.0'
]
```

You must specify the version at the *end* of the string in `dependency-links`.

Then run `pip install` in your project's virtual environment.

```
pip install --process-dependency-l
inks git+https://github.com/seahrh/sgcharts-stringx.git
```
