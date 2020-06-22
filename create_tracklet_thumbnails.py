import os
import glob

import cv2
import numpy as np


OUT_HEIGHT = 12000  # px
MAX_LEN = 12  # truncate tracklets to this length

tracklet_images = []
for tracklet_folder in glob.glob('data/13*'):
    tracklet_images.append([
        cv2.imread(img_filename) for img_filename in sorted(glob.glob(os.path.join(tracklet_folder, '*.jpg')))
    ])

height = OUT_HEIGHT // len(tracklet_images)
width = height // 2
thumbnail_size = (width, height)

tracklet_images = [[cv2.resize(img, thumbnail_size) for img in tracklet[:10]] for tracklet in tracklet_images]

out_image = np.zeros((OUT_HEIGHT, width * MAX_LEN, 3))

for i, tracklet in enumerate(tracklet_images):
    for j, image in enumerate(tracklet):
        out_image[i * height:(i+1) * height, j * width:(j+1) * width, :] = image

cv2.imwrite('out.jpg', out_image)
