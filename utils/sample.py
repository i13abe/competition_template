import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample', help='sample', type=str, default="sample")
    args = parser.parse_args()
    return args

def sample(args):
    print(args)

def main():
    # parse the arguments
    args = parse_args()
    
    sample(args.sample)
    

if __name__ == '__main__':
    main()