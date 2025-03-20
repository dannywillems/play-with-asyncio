import asyncio


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate an I/O operation
    print("Data fetched")
    return 42


async def main():
    asyncio.run(fetch_data())
    result = await fetch_data()
    print(f"Result: {result}")


asyncio.run(main())
