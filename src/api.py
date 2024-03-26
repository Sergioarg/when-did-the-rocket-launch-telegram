from requests import get
from os import getenv
# URL de la API que devuelve la imagen
url = "https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/3000/"

API_BASE = getenv("API_BASE", "https://framex-dev.wadrid.net/api/video")
VIDEO_NAME = getenv(
    "VIDEO_NAME", "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)


# Realizar la solicitud a la API
def get_video_data(url):
    response = get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        r = response.json()
        count = r[0]['frames']
        print(count)
    else:
        print("Error al obtener la imagen desde la API")


get_video_data(API_BASE)
