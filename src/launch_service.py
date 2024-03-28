""" Service to abstract the logic of the moment of the launch """
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
        """Get mid of the data

        Args:
            left (int): data to check between the option
            right (int): data to check between the option

        Returns:
            int: frame of the middle
        """

        mid_frame = int((left + right) / 2)

        return mid_frame

    def bitsect(self, discard_left: bool):
        """Search according if the values is close to left or right

        Args:
            discard_left (bool): flag to check which side dicard
        """

        if discard_left:
            self.left = self.current_frame
        else:
            self.right = self.current_frame

        self.current_frame = self.get_next_mid(self.left, self.right)

    def find_launch_frame(self, discard_left: bool) -> bool:
        """find the frame where the rocket launch

        Args:
            discard_left (bool): flag to check which side dicard

        Returns:
            bool: flag according if they find a frame
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
