
import numpy as np
from PIL import Image


class ImageProcessing:
    def __init__(self, target_img) -> None:
        self.target_img = target_img
        self.T_H, self.T_W = self.target_img.size

    def images_to_arrays(self, image1, image2):
        """Represent images as arrays."""
        img1_arr = np.array(image1)
        img2_arr = np.array(image2)
        return img1_arr, img2_arr

    def blending(self, image1, image2):
        """Blend to images together with 0.5 alpha."""
        return Image.blend(image1, image2, alpha=0.5)

    def random_horizontal_swap(self, image1, image2):
        """Swap random rows of two images."""
        img1_arr, img2_arr = self.images_to_arrays(image1, image2)
        horizontal_random_choice = np.random.choice(self.T_W,
                                                    int(self.T_W/2),
                                                    replace=False)
        img1_arr[horizontal_random_choice] = img2_arr[horizontal_random_choice]
        return Image.fromarray(img1_arr)

    def random_vertical_swap(self, image1, image2):
        """Swap random columns of two images."""
        img1_arr, img2_arr = self.images_to_arrays(image1, image2)
        vertical_random_choice = np.random.choice(self.T_H,
                                                  int(self.T_H/2),
                                                  replace=False)
        img1_arr[:, vertical_random_choice] = img2_arr[:,
                                                       vertical_random_choice]
        return Image.fromarray(img1_arr)

    def half_vertical_swap(self, image1, image2):
        """Swap images halfs (verticaly)."""
        img1_arr, img2_arr = self.images_to_arrays(image1, image2)
        img1_half = img1_arr[0:int(self.T_H/2),]
        img2_half = img2_arr[int(self.T_H/2):self.T_H,]
        return np.vstack((img1_half, img2_half))

    def half_horizontal_swap(self, image1, image2):
        """Swap images halfs (horizontaly)."""
        img1_arr, img2_arr = self.images_to_arrays(image1, image2)
        img1_half = img1_arr[:, 0:int(self.T_W/2)]
        img2_half = img2_arr[:, int(self.T_W/2):self.T_W]
        return np.hstack((img1_half, img2_half))
