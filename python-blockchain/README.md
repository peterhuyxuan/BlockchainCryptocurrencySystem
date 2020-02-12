**Change into the 'python-blockchain' directory first**

```
cd python-blockchain
```

**Activate the virtual environment**

```
blockchain-env/Scripts/activate
```

Using activating virtual environment using Git Bash

```
. blockchain-env/Scripts/activate
```

**Install all packages**

```
pip install -r requirements.txt
```

**Run the tests**
Make sure to activate virtual environment.

```
python -m pytest backend/tests
```

**Run the application and API**
Make sure to activate the virtual environment.

```
python -m backend.app
```

**Test pub/sub**

```
python -m backend.pubsub
```

**Run a peer instance**

```
export PEER=True && python -m backend.app
```

Use 'set' instead of 'export' when using Windows "cmd.exe" Command Prompt

**Test application script**

```
python -m backend.scripts.test_app
```
