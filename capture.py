"""
    kindle2pdf 2022
"""
import os
import time
import cv2
import pyautogui

class Capture:
    """
    Class for taking a screenshot of the specified range
    """

    def window_manager(self) -> int:
        """
        :function:
            - window_manager
        :brief:
            - Get window coordinates

        :Args:
            - None
        :Return:
            - int: upper_left position, bottom_right position
        """
        # Get upper left coordinates
        print("Move the mouse cursor to the upper left of the area you want to capture within 10 seconds")
        time.sleep(10)
        upper_left_x, upper_left_y= pyautogui.position()
        print(f'coordinates: {upper_left_x}, {upper_left_y}')

        # Get bottom right coordinates
        print("Move the mouse cursor to the bottom right of the area you want to capture within 10 seconds")
        time.sleep(10)
        bottom_right_x, bottom_right_y = pyautogui.position()
        print(f'coordinates: {bottom_right_x}, {bottom_right_y}')

        return upper_left_x, upper_left_y, bottom_right_x, bottom_right_y

    def window_capture(
        self,
        x_1: int,
        y_1: int,
        x_2: int,
        y_2: int
    ) -> None:
        """
        :function:
            - window_capture
        :brief:
            - Take a Screenshot of Each Kindle Page

        :Args:
            - x_1: Upper left x cartesian coordinates
            - y_1: Upper left y cartesian coordinates
            - x_2: Bottom right x cartesian coordinates
            - y_2: Bottom right y cartesian coordinates
        :Return:
            - None
        """
        # Maximum number of pages
        max_page = 3000

        # Screenshot interval
        span = 0.1

        # Waiting 10 seconds to start the Kindle
        time.sleep(10)

        # Setting the output folder
        os.chdir("D:/KindlePDF/test/test_png")

        # First page shot
        file_name = 'picture_0.png'
        screen_shot = pyautogui.screenshot(region=(
                x_1,
                y_1,
                x_2 - x_1,
                y_2 - y_1
            ))
        screen_shot.save(file_name)
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')
        time.sleep(span)

        # Remaining screenshots
        for page in range(1, max_page):
            file_name = f'picture_{page}.png'
            screen_shot = pyautogui.screenshot(region=(
                x_1,
                y_1,
                x_2 - x_1,
                y_2 - y_1
            ))
            screen_shot.save(file_name)
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')
            img_prev_name = f'picture_{page-1}.png'
            img_prev = cv2.imread(img_prev_name)
            img_current = cv2.imread(file_name)
            time.sleep(span)

            # Compare previous screenshot with current screenshot
            mask = cv2.absdiff(img_prev, img_current)
            mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            # Stop screenshot if max_page is reached or the difference is zero
            if page == max_page or not cv2.countNonZero(mask_gray):
                break
