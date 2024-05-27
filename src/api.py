""" Module to manage the interactions whit FrameX API"""
from os import getenv
from requests import get

API_BASE = getenv("API_BASE", "https://framex-dev.wadrid.net/api/video")
VIDEO_NAME = getenv(
    "VIDEO_NAME", "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)

class FrameXAPI:
    """ Class to manage interactions with the FrameX API. """
    def __init__(self, video_name: str = VIDEO_NAME) -> None:
        self.video_name = video_name
        self.api_base = API_BASE

    def get_total_frames(self) -> int:
        """Return the number of frames avalible to search

        Returns:
            int: count of total frames
        """
        total_frames = 0
        response = get(API_BASE, timeout=30)

        if response.status_code == 200:
            res = response.json()
            total_frames = res[0]['frames']
        else:
            print("Error to get the FrameX API")
            exit(1)

        return total_frames

    def get_link_frame(self, frame: int, total_frames: int) -> str:
        """Create a link whit the frame specified

        Args:
            frame (int): Frame for which the link will be created.
            total_frames (int): Total number of frames available for search.

        Returns:
            str: URL with the link to the specified frame.
        """

        if frame < 0 or frame > total_frames:
            print(f"Error, frame value must be between 0 and {total_frames}")
            return None

        url = f'{API_BASE}/{VIDEO_NAME}/frame/{frame}'
        return url
