# Python API

```python
from truffle import TruffleClient

truffle = TruffleClient('truffle-8008.local')

calculator = truffle.apps.get('calculator')

print(calculator.generate_text('What is 100 * 100?'))

chat_1234154 = truffle.apps.get('chat_1234154')

print(chat_1234154.submit_user_prompt('Im tired of doing work by hand'))
```

# TODO: this is the ideal but our acutal codebase is not there yet. You will need to do an overhaul of the codebase to make this work like this.