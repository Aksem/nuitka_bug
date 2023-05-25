import asyncio


async def iterator():
    yield ((1, 'path11'),)
    await asyncio.sleep(1)
    yield ((2, 'path2'),)
    await asyncio.sleep(1)
    yield ((2, 'path3'),)


async def iterate_changes() -> None:
    print(f"Start")
    async for changes in iterator():
        print(f"Iteration: {changes}")
        print('before')
        filtered_items = set(
            [
                change
                for change in changes
                if any(
                    change[1].endswith(suffix)
                    for suffix in [".txt", ".toml"]
                )
            ]
        )
        print('after')


if __name__ == '__main__':
    asyncio.run(iterate_changes())
