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
        """Return the number of frames avalible to search

        Returns:
            int: count of total frames
        """
        frames = 0
        response = get(self.api_base)

        if response.status_code == 200:
            r = response.json()
            frames = r[0]['frames']
        else:
            print("Error to get the API")

        return frames

    def get_link_frame(self, frame: int) -> str:
        """Create a link whit the frame specified

        Args:
            frame (int): frame to search at api

        Returns:
            str: url whit the link of the frame
        """
        if frame < 0 or frame > frames:
            print(f"Error, frame value must be between 0 and {frames}")
            return None

        frames = self.get_frames_data()

        url = f'{self.api_base}/{self.video_name}/frame/{frame}'
        return url


api = FrameXAPI()
frames = api.get_frames_data()
print(f'Frames: {frames}')
