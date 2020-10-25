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
Make sure to activate the virtual environment.

```
python -m backend.pubsub
```

**Run a peer instance**
Make sure to activate the virtual environment.

```
export PEER=True && python -m backend.app
```

Use 'set' instead of 'export' when using Windows "cmd.exe" Command Prompt

**Seed the backend with data**
Make sure to activate the virtual environment.

```
export SEED_DATA=True && python -m backend.app
```

Use 'set' instead of 'export' when using Windows "cmd.exe" Command Prompt

**Test application script**
Make sure to activate the virtual environment.

```
python -m backend.scripts.test_app
```

**Change into the 'frontend' directory to setup the frontend**

```
cd frontend
```

**Install all the packages**

```
npm install
```

**Run the frontend**
In the frontend directory:

```
npm run start
```
