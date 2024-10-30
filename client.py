import aiohttp
import asyncio

BASE_URL = 'http://127.0.0.1:8080/ads'


async def test_create_ad():
    async with aiohttp.ClientSession() as session:
        data = {
            'title': 'Продам велосипед',
            'description': 'В отличном состоянии, использовался один сезон',
            'owner': 'Алексей'
        }
        async with session.post(BASE_URL, json=data) as response:
            print(f'POST /ads: {response.status}')
            print('Ответ:', await response.json())


async def test_get_all_ads():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as response:
            print(f'GET /ads: {response.status}')
            print('Ответ:', await response.json())


async def test_get_ad(ad_id):
    async with aiohttp.ClientSession() as session:
        url = f'{BASE_URL}/{ad_id}'
        async with session.get(url) as response:
            print(f'GET /ads/{ad_id}: {response.status}')
            print('Ответ:', await response.json())


async def test_delete_ad(ad_id):
    async with aiohttp.ClientSession() as session:
        url = f'{BASE_URL}/{ad_id}'
        async with session.delete(url) as response:
            print(f'DELETE /ads/{ad_id}: {response.status}')
            print('Ответ:', await response.json())


async def main():
    await test_create_ad()
    await test_get_all_ads()
    await test_get_ad(1)
    await test_delete_ad(1)
    await test_get_all_ads()


# Запуск тестов
if __name__ == '__main__':
    asyncio.run(main())
