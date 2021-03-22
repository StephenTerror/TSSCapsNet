import tensorflow as tf
from utils import Dataset, plotHistory
from models import TSSCapsNet
from models import TSSEfficientCapsNet
from models import EfficientCapsNet
from models import CapsNet


# model_name = 'DCT_CapsNet_Attention'      # TSSCapsNet
# model_name = 'DCT_CapsNet_GumbelGate'     # TSSCapsNet
# model_name = 'DCT_CapsNet'                # TSSCapsNet
# model_name = 'DCT_Efficient_CapsNet'      # TSSEfficientCapsNet
model_name = 'RFFT_Efficient_CapsNet'       # TSSEfficientCapsNet
# model_name = 'Efficient_CapsNet'          # EfficientCapsNet
# model_name = 'CapsNet'                    # CapsNet


# data_name = 'MNIST'
# data_name = 'MNIST_SHIFT'
# data_name = 'FASHION_MNIST'
data_name = 'FASHION_MNIST_SHIFT'

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_visible_devices(gpus[3], 'GPU')
tf.config.experimental.set_memory_growth(gpus[3], True)

# 1.0 Import the Dataset
dataset = Dataset(data_name, config_path='config.json')

# 2.0 Load the Model
model = TSSCapsNet(data_name, model_name=model_name, mode='test', verbose=True)
# model = TSSEfficientCapsNet(data_name, model_name=model_name, mode='test', verbose=True)
# model = EfficientCapsNet(data_name, model_name=model_name, mode='test', verbose=True)
# model = CapsNet(data_name, model_name=model_name, mode='test', verbose=True)

# 3.0 Train the Model
dataset_train, dataset_val = dataset.get_tf_data()
history = model.train(dataset, initial_epoch=0)

# 4.0 Plot history
plotHistory(history)