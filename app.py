import argparse
from ytd import download


def get_args() -> dict:

    # Get cli arguments, format and URL required 
    # Download directory optional, defaults to current working directory 
    parser = argparse.ArgumentParser(prog="YT-CLI", description="Downloads media from YouTube in userspecified format", epilog="\nYT-CLI")
    parser.add_argument("-f", type=str, metavar="Format", required=True)
    parser.add_argument("-u", type=str, metavar="URL", required=True)
    parser.add_argument("-d", type=str, metavar="Directory", required=False)
    args: dict = parser.parse_args()
    return args

def main():
    args: dict = get_args()
    success: bool = download(args)   


if __name__ == "__main__":
    main()


