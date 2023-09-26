# BlandAI Python Library

## Description

`blandai` is a Python wrapper for the Bland.ai API, designed to simplify the process of making AI phone calls. With this package, you can easily integrate Bland.ai's functionalities into your Python applications.

## Features

- Make a phone call with a specific task
- Retrieve logs for a call
- Wait on hold
- End a phone call

## Installation

Install the package via pip:

```bash
pip install blandai
```

## Usage

Here's a quick example to get you started:

```python
from blandai import BlandAI

# Initialize the wrapper with your API key
blandai = BlandAI(api_key="YOUR_API_KEY_HERE")

# Make a phone call
response = blandai.call(
    phone_number="NUMBER_TO_CALL",
    task="YOUR_TASK"
)
print(response)

# Retrieve logs
logs = blandai.logs(call_id="YOUR_CALL_ID_HERE")
print(logs)

# Wait on hold
wait_on_hold = blandai.hold(
    phone_number='NUMBER_TO_INITIALLY_CALL',
    hold_connect='YOUR_NUMBER'
)

# End a phone call
end_call = blandai.end_call(call_id="YOUR_CALL_ID_HERE")
```

## Parameters

- `call(phone_number, task, voice_id=0, request_data=None, reduce_latency=True, amd=True)`
  - `phone_number`: The phone number to call.
  - `task`: The task for the call.
  - `voice_id`: Voice ID from 0 - 3. Defaults to 0.
  - `request_data`: Key-value store if you want the AI to know specific facts.
  - `reduce_latency`: Improves response time. Defaults to 'true'
  - `amd`: automatic machine detection. Defaults to 'false'
  - `webhook`: Callback url. Call_id + transcripts will be sent.

- `logs(call_id)`
  - `call_id`: The ID of the call for which to retrieve logs.

- `hold(phone_number, hold_connect, task)`
  - `phone_number`: The phone number to call.
  - `hold_connect`: Once the AI detects a human has answered the call, it will call this number.
  - `task`: Special instructions. Deafaults to 'None'.

- `end_call(call_id)`
  - `call_id`: The ID of the call for which to retrieve logs.

## Contributing

If you find any bugs or have a feature request, please open an issue on [GitHub](https://github.com/lankabelgezogen/blandailibrary).

## License

MIT
