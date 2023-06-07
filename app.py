import argparse
from ytd import download
import webscraper


def get_args() -> dict:

    # Get cli arguments, format and URL required 
    # Download directory optional, defaults to current working directory 
    parser = argparse.ArgumentParser(prog="YT-CLI", description="YouTube Search & Download Tool", epilog="\nSearch\n [-s Required]\nDownload\n [-f-u Required] [-d Optional]")
    # Download arguments 
    parser.add_argument("-f", type=str, metavar="Format", required=False)
    parser.add_argument("-u", type=str, metavar="URL", required=False)
    parser.add_argument("-d", type=str, metavar="Directory", required=False)
    
    # Search arguments
    parser.add_argument("-s", type=str, metavar="Search", required=False)
    
    args: dict = parser.parse_args()
    return args

def search(term: str):
    results = webscraper.YouTube(term)
    results.parse()
    results.get_html()
    results.scrape()
    return results

def main() -> int:
    args: dict = get_args()
    
    if args.s: 
        results: webscraper.YouTube = search(args.s)
        print(results)

    elif args.u and args.f:
        download(args)
    
    else:
        raise ValueError("Invalid or Missing Arguments")
        return 1
    
    return 0    

if __name__ == "__main__":
    ext_code: int = main()
    print(f"Program exited with code {ext_code}")

