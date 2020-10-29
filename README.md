# Code for "How to use Python logging QueueHandler with dictConfig"

Оригинальная статья:

https://rob-blackbourn.medium.com/how-to-use-python-logging-queuehandler-with-dictconfig-1e8b1284e27a

The following script was tested on Ubuntu 18.04 with Python 3.7

```bash
# Set up the project
cd medium-queue-logging
python3.7 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Run the example
export PYTHONPATH=.:$PYTHONPATH
python examples/main.py
```
