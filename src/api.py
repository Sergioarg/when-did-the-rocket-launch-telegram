""" Moduel to manage the interactions whit FrameX API"""
from os import getenv
from requests import get

API_BASE = getenv("API_BASE", "https://framex-dev.wadrid.net/api/video")
VIDEO_NAME = getenv(
    "VIDEO_NAME", "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)

class FrameXAPI:
    """ Class to manage actions of the API """

    def get_frames_data(self) -> int:
        """Return the number of frames avalible to search

        Returns:
            int: count of total frames
        """
        frames = 0
        response = get(API_BASE, timeout=30)

        if response.status_code == 200:
            r = response.json()
            frames = r[0]['frames']
        else:
            print("Error to get the API")

        return frames

    def get_link_frame(self, frame: int, total_frames: int) -> str:
        """Create a link whit the frame specified

        Args:
            frame (int): frame to search at api

        Returns:
            str: url whit the link of the frame
        """

        if frame < 0 or frame > total_frames:
            print(f"Error, frame value must be between 0 and {total_frames}")
            return None

        url = f'{API_BASE}/{VIDEO_NAME}/frame/{frame}'
        return url
