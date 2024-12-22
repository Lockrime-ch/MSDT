import asyncio
import aiohttp
import random


async def fetch_api(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json()
            print(f'Fetched data from "{URL}"')
            return data


async def unpack_json(json):
    await asyncio.sleep(random.uniform(0.5, 3))
    print(f'post {json["id"]}: {json["title"].upper()}')
    result = f'post {json["id"]}: {json["title"].upper()}\n{json["body"]}'
    return result


async def main():
    URLs = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3',
        'https://jsonplaceholder.typicode.com/posts/4'
    ]
    fetched_data = [fetch_api(URL) for URL in URLs]
    responses = await asyncio.gather(*fetched_data)
    unpacked_data = [unpack_json(json) for json in responses]
    results = await asyncio.gather(*unpacked_data)
    print()
    for elem in results:
        print(elem)
    print('Работа завершена.')


if __name__ == '__main__':
    asyncio.run(main())
