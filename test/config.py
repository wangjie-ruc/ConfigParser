
root = '/data/DomainNet'

domains = {'c':'clipart', 'r':'real', 's':'sketch'}

source = 'c'
target = 'r'

source_train_list = f'{root}/ImageSets/{domains[source]}_train.txt'
target_train_list = f'{root}/ImageSets/{domains[target]}_train.txt'

batch_size = 32

gpus = [0, 1, 2]

model_kwargs = dict(num_classes=10, kwargs=dict(pretrained=True))