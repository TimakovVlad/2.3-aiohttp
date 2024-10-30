from aiohttp import web
from datetime import datetime

# Временное хранилище для объявлений
ads = []

def find_ad(ad_id):
    for ad in ads:
        if ad['id'] == ad_id:
            return ad
    return None

class AdView(web.View):
    async def get(self):
        ad_id = self.request.match_info.get('ad_id')
        if ad_id:
            ad_id = int(ad_id)
            ad = find_ad(ad_id)
            if ad:
                return web.json_response(ad)
            return web.json_response({'message': 'Объявление не найдено'}, status=404)
        return web.json_response(ads)

    async def post(self):
        data = await self.request.json()
        ad = {
            'id': len(ads) + 1,
            'title': data.get('title'),
            'description': data.get('description'),
            'created_at': datetime.now().isoformat(),
            'owner': data.get('owner')
        }
        ads.append(ad)
        return web.json_response(ad, status=201)

    async def delete(self):
        ad_id = int(self.request.match_info['ad_id'])
        ad = find_ad(ad_id)
        if ad:
            ads.remove(ad)
            return web.json_response({'message': 'Объявление удалено'}, status=200)
        return web.json_response({'message': 'Объявление не найдено'}, status=404)

# Настройка маршрутов
app = web.Application()
app.router.add_view('/ads', AdView)                    # Обработчик для всех объявлений
app.router.add_view('/ads/{ad_id:\d+}', AdView)        # Обработчик для конкретного объявления по ID

if __name__ == '__main__':
    web.run_app(app)
