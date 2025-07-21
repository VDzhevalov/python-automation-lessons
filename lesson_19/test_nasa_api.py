import requests
import os

def test_nasa_mars_api_response():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'sol': 1000,
        'camera': 'fhaz',
        'api_key': 'DEMO_KEY'
    }

    response = requests.get(url, params=params)

    data = response.json()

    photos = response.json().get('photos', [])

    num_photos = min(2, len(photos))

    assert response.status_code == 200, f"Очікувався 200, але отримано {response.status_code}"
    assert 'photos' in data, "У відповіді немає ключа 'photos'"
    assert num_photos > 0, "API не повернув фото для завантаження"

    for i in range(num_photos):
        img_url = photos[i]['img_src']
        img_data = requests.get(img_url).content
        filename = f"mars_photo{i+1}.jpg"
        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f"Збережено: {filename} з {img_url}")

    assert os.path.exists(filename), f"Файл {filename} не знайдено після збереження"
    assert os.path.getsize(filename) > 0, f"Файл {filename} існує, але порожній"
