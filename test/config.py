
root = '/home/zhangsan/data'

imagelist = f'{root}/coco/train.txt'

batch_size = 32

gpus = [0, 1, 2]

model_kwargs = dict(num_classes=10, kwargs=dict(pretrained=True))