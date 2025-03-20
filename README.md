Play with asyncio
=====================

Python 3.13: https://github.com/python/cpython/blob/3.13/Lib/asyncio/

- [0001-call-run-twice](./0001-call-run-twice): raises an exception when run is called twice. Going through the code.

```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate an I/O operation
    print("Data fetched")
    return 42


# main is called a coroutine.
# all methods executed in a runner (this is the code
# called under the hood by the entry point `run`, see
# https://github.com/python/cpython/blob/3.13/Lib/asyncio/runners.py#L86
async def main():
    result = await fetch_data()
    print(f"Result: {result}")

asyncio.run(main())
```
