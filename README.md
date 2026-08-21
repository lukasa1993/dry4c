# dry4c

Duplication analysis for **C** projects.

```bash
python -m pip install git+https://github.com/lukasa1993/dry4c.git
dry4c --min-tokens 30 --fail
```

The tool removes comments and literal contents, normalizes identifiers and numeric values, and reports repeated token windows.
