from ConfigParser.config import Config
import sys

def main():
    # cfg = Config.fromfile('test/config.py')
    # print(cfg)
    parser, cfg = Config.auto_argparser()
    print(cfg)
    print()
    args = parser.parse_args()
    print(args.__dict__)
    for k,v in args.__dict__.items():
        print(k,v)
    
    cfg.merge_from_options(args)

    print(cfg)

if __name__ == "__main__":
    main()