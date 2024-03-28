""" Module to abstracts the logic of the moment of the launch """
class LaunchService:
    """ Class with methods to interact the launch service """

    def __init__(self, api):
        self.api = api
        self.total_frames = self.api.get_frames_data()
        self.left = 0
        self.right = self.total_frames
        self.launch_frame = None
        self.current_frame = self.get_next_mid(0, self.total_frames)
        self.image_url = self.api.get_link_frame(self.current_frame, self.total_frames)


    def get_next_mid(self, left: int, right: int) -> int:
        """Calculates the middle frame index between the `left` and `right` indices.

        Args:
            left (int): Index of the leftmost frame in the current search range.
            right (int): Index of the rightmost frame in the current search range.

        Returns:
            int: Mid-frame index between `left` and `right`.
        """

        mid_frame = int((left + right) / 2)

        return mid_frame

    def bitsect(self, discard_left: bool) -> None:
        """Updates the `left` and `right` indices based on whether the left or
            right side of the current search range is discarded.

        Args:
            discard_left (bool): Flag indicating whether to discard
            the left side of the current search range.
        """

        if discard_left:
            self.left = self.current_frame
        else:
            self.right = self.current_frame

        self.current_frame = self.get_next_mid(self.left, self.right)

    def find_launch_frame(self, discard_left: bool) -> bool:
        """Find the frame where the rocket launch.

        Args:
            discard_left (bool): Flag indicating whether to discard the
            left side of the current search range.

        Returns:
            bool: Returns `True` if the launch frame is found, `False` otherwise.
            frame is found, `False` otherwise.
        """

        if self.left < self.right and self.left - self.right == -1:
            if not discard_left:
                self.launch_frame = self.current_frame
            elif self.current_frame == self.left:
                self.launch_frame = self.right
            else:
                self.launch_frame = self.left

            self.image_url = self.api.get_link_frame(self.launch_frame, self.total_frames)
            return True

        self.bitsect(discard_left)
        self.image_url = self.api.get_link_frame(self.current_frame, self.total_frames)

        return False
