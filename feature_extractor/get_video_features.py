import numpy as np
import cv2
from video_summary.VGG.vgg16 import VGG16
from keras.models import Model
from sklearn.decomposition import PCA


def get_cnn_feat(frames_raw):
    frames = []
    pca = PCA(n_components=500)
    for im in frames_raw:
        im = cv2.resize(im, (350, 350)).astype(np.float32)
        im[:, :, 0] -= 103.939
        im[:, :, 1] -= 116.779
        im[:, :, 2] -= 123.68
        im = np.expand_dims(im, axis=0)
        frames.append(np.asarray(im))
    frames = np.array(frames)

    base_model = VGG16(weights='imagenet', include_top=True)
    model = Model(input=base_model.input, output=base_model.get_layer('fc2').output)

    i = 0
    features = np.ndarray((frames.shape[0], 4096), dtype=np.float32)
    for x in frames:
        features[i, :] = model.predict(x)
        i += 1
    return pca.fit_transform(features)


