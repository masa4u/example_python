import asyncio


async def ticker(delay, to):
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


# async def async_comprehensions():
#     comp_with_async = [i async for i in ticker(1, 10) if i % 2]
    # comp_with_await = [await fun() for fun in ticker(110) if await i% 2]

ticker(1, 10)

# async_comprehensions()