"""Day 3 · The speed run

20 pages, 0.2 seconds each. One by one that's 4 seconds. Together it's about 0.2.
Use fake_web.fetch(url) for every request.

Run `python quest.py 3` after each TODO.
"""
import asyncio  # noqa: F401

from quests.day03 import fake_web


async def fetch_one(url: str) -> tuple[str, int]:
    """TODO 3.1 · Fetch one page with `await fake_web.fetch(url)` and return (url, length of the page)."""
    site = await fake_web.fetch(url)
    return (url, len(site))
    # raise NotImplementedError


async def fetch_all(urls: list[str]) -> list[tuple[str, int]]:
    """TODO 3.2 · Fetch every url AT THE SAME TIME (hint: asyncio.gather) and return results in the same order."""
    results = await asyncio.gather(*(fetch_one(url) for url in urls))
    return results
    # raise NotImplementedError


async def fetch_all_limited(urls: list[str], limit: int = 3) -> list[tuple[str, int]]:
    """TODO 3.3 · Same as fetch_all, but never more than `limit` fetches at once (hint: asyncio.Semaphore)."""
    semaphore = asyncio.Semaphore(limit)

    async def limited_fetch(url: str):
        async with semaphore:
            return await fetch_one(url)

    results = await asyncio.gather(
        *(limited_fetch(url) for url in urls)
    )
    return results    
    # raise NotImplementedError


async def fetch_all_safe(urls: list[str], timeout: float = 0.5) -> list[tuple[str, int | None]]:
    """TODO 3.4 · Same as fetch_all, but a page that takes longer than `timeout` seconds
    gives (url, None) instead of making everyone wait (hint: asyncio.wait_for and TimeoutError)."""

    async def fetch_with_timeout(url: str):
        try:
            return await asyncio.wait_for(
                fetch_one(url),
                timeout=timeout
            )
        except TimeoutError:
            return (url, None)

    rets= await asyncio.gather( *(fetch_with_timeout(url) for url in urls) )        

    return rets
    # raise NotImplementedError
