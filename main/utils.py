from tensorflow import keras
import numpy as np
import tensorflow as tf

def predict(u):
	model = keras.models.load_model('C:/Users/Tanu/Documents/BE p')
	img_url = str(u)
	img_height = 200
	img_width = 200
	class_names =['Hexagon', 'Parallelogram', 'circle', 'square', 'triangle']

	img = keras.preprocessing.image.load_img(
    	img_url, target_size=(img_height, img_width)
	)
	img_array = keras.preprocessing.image.img_to_array(img)
	img_array = tf.expand_dims(img_array, 0) # Create a batch

	predictions = model.predict(img_array)
	#print(predictions,"ppppppppppppppppppppppppppppppppppppppp")
	score = tf.nn.softmax(predictions[0])
	r=format(class_names[np.argmax(score)])
	return r