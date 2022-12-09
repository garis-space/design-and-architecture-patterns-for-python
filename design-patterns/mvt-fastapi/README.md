# Run example and get user data

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run example
```bash
uvicorn main:app --reload
```

### Get user data
```bash
curl http://localhost:8000/user?username=foo
```

### Run tests
```bash
pytest tests.py
```
