import requests

BASE_URL = "http://127.0.0.1:8080"

file_path = "example.jpg"

with open(file_path, "rb") as img_file:
    files = {'image': img_file}
    upload_response = requests.post(f"{BASE_URL}/upload", files=files)

if upload_response.status_code != 201:
    print("Завантаження не відбулося:", upload_response.text)
    exit(1)

image_url = upload_response.json()["image_url"]
filename = image_url.split("/")[-1]
print("Завантажено:", image_url)

headers = {"Content-Type": "text"}
get_response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)

if get_response.status_code == 200:
    print("Посилання на зображення:", get_response.json()["image_url"])
else:
    print("Не вдалося отримати зображення:", get_response.text)


delete_response = requests.delete(f"{BASE_URL}/delete/{filename}")

if delete_response.status_code == 200:
    print("Видалено:", delete_response.json()["message"])
else:
    print("Не вдалося видалити:", delete_response.text)
