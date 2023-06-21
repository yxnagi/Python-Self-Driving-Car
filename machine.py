import os
import tensorflow as tf

image = tf.data.Dataset.list_files(os.join.path('data', '*.png'))
