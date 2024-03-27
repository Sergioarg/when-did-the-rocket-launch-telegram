from requests import get
from os import getenv

API_BASE = getenv("API_BASE", "https://framex-dev.wadrid.net/api/video")
VIDEO_NAME = getenv(
    "VIDEO_NAME", "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)

class FrameXAPI:
    def __init__(self):
        self.api_base = API_BASE
        self.video_name = VIDEO_NAME

    def get_frames_data(self) -> int:
        """
        Get the number of frames from API
        """
        response = get(self.api_base)

        if response.status_code == 200:
            r = response.json()
            self.frames = r[0]['frames']
            return self.frames
        else:
            print("Error to get the API")
            return 0

    def get_link_frame(self, frame: int) -> str:
        """
        Create a link with the frame to show
        """
        url = f'{self.api_base}/{self.video_name}/frame/{frame}'
        return url


api = FrameXAPI(API_BASE)
frames = api.get_frames_data()
print(f'Frames: {frames}')


# def binary_search(array, target):
#     low = 0
#     high = len(array) - 1

#     if len(array) < 1:
#         raise ValueError("Cannot bissect an empty array")

#     while low <= high:
#         mid = (low + high) // 2
#         print(f"¿Es el valor {array[mid]} el objetivo? (y/n)")
#         user_input = input().lower()

#         if user_input == "y":
#             return mid
#         elif user_input == "n":
#             if array[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         else:
#             print("Entrada inválida. Por favor, responda con 'y' o 'n'.")
#     return -1

# array = list(range(1, frames))
# target = frames

# index = binary_search(array, target)

# frame_link = api.get_link_frame(index)

# print(f'Link: {frame_link}')
