# ConfigParser

## usage


```python
# test/config.py

root = '/home/zhangsan/data'
batch_size = 32
gpus = [0, 1, 2]
model_kwargs = dict(num_classes=10, kwargs=dict(pretrained=False))
```

```python test/test1.py```

```python
#  test/test1.py

from ConfigParser import Config

def main():
    cfg = Config.fromfile('test/config.py')
    print(cfg.root)
    print(cfg.gpus)

if __name__ == '__main__':
    main()

```

```python test/test2.py test/config.py --gpus 0 1 2 3 --model_kwargs.num_classes 100   --model_kwargs.kwargs.pretrained```

```python
# test/test2.py

from ConfigParser import Config

def main():
    parser, cfg = Config.auto_argparser()
    args = parser.parse_args()
    cfg.merge_from_options(args)

    print(cfg.gpus)
    print(cfg.model_kwargs)

if __name__ == '__main__':
    main()

```

## Notice

code are copied and modified from addict and mmcv