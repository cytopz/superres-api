from base64 import b64decode, b64encode
from .image import Image
import os
import cv2
import numpy as np

class Upscaler():
    """ wrapper class for cv2 dnn_superres
    """
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, method: str = 'fsrcnn', scale: int = 3):
        self.scale = scale
        self.method = method
        self.__init_upscaler()
    
    def __init_upscaler(self):
        """initializes dnn superres
        """
        self.upscaler = cv2.dnn_superres.DnnSuperResImpl_create()
        self.upscaler.readModel(f'{self.CURR_DIR}/models/{self.method.upper()}/x{self.scale}.pb')
        self.upscaler.setModel(self.method, self.scale)

    def __read_b64_img(self, img: str): 
        """reads base64 encoded image and converts it to np array
        """
        b64 = img
        b64 = b64decode(b64)
        nparr = np.fromstring(b64, dtype=np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    def __encode_b64_img(self, img: np.ndarray, ext: str):
        """converts back np array from opencv to base64 encoded image
        """
        _, img = cv2.imencode(f'.{ext}', img)
        return b64encode(img).decode()

    def upscale(self, img: Image):
        """upscales an image
        """
        img_cv = self.__read_b64_img(img.b64)
        img_upscaled = self.upscaler.upsample(img_cv)
        return self.__encode_b64_img(img_upscaled, img.ext)
