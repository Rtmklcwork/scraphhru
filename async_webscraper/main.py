import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def fetch_page(url,session):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = response.text()
            print(f"Ответ с {url} получен")
            return content
    except aiohttp.ClientConnectionError as e:
        print(f"Возникла ошибка {e}")
    except aiohttp.HTTPError as e:
        print(f"Ошабка HTTP для {url}: {e}")
    except Exception as e:
        print(f"Возникла ошибка при обработке {url}: {e}")
    finally:
        print(f"Запрос к {url} завершен")
    