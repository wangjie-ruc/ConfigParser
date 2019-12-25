from apcs import Config

def main():
    parser, cfg = Config.auto_argparser()
    print(cfg)
    args = parser.parse_args()
    print(args)
    cfg.merge_from_options(args)
    print(cfg.gpus)
    print(cfg.model_kwargs)

if __name__ == '__main__':
    main()