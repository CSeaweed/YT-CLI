from pytube import YouTube
import pathlib
from time import sleep


def resolve_dir(args: dict, cwd: pathlib.WindowsPath) -> pathlib.WindowsPath:
    if args.d: dir = args.d 
    else: dir = cwd
    return pathlib.Path(dir)

def fix_suffix(media: str, original: str, new: str):
    to_fix: pathlib.WindowsPath = pathlib.Path(media)
    to_fix.rename(media.replace(original, new))

def get_video(video: YouTube, dir: pathlib.WindowsPath) -> bool:
    attempt: int = 1
    title: str = video.title
    
    while attempt <= 10: 
        print(f"Downloading.. attempt: {attempt}/10", end="\r")
        
        try:
            media = video.streams.get_highest_resolution()
            media.download(dir)
            return True
        except:
            attempt += 1
            sleep(0.2)
    
    # Only in reach if attempts run out 
    return False

def get_audio(video: YouTube, dir: pathlib.WindowsPath) -> bool:
    attempt: int = 1
    title: str = video.title
    
    while attempt <= 10: 
        print(f"Downloading.. attempt: {attempt}/10", end="\r")
        
        try:
            media = video.streams.filter(only_audio=True).first()
            media = media.download(dir)
            fix_suffix(media, "mp4", "mp3")
            return True
        except:
            attempt += 1
            sleep(0.2)
    
    # Only in reach if attempts run out 
    return False

def download(args: dict) -> bool:
     
    # Validate args 
    dir: pathlib.WindowsPath = resolve_dir(args, pathlib.Path.cwd())
    format: str = args.f 
    url: str = args.u
    
    # Init video and validate availability 
    video: YouTube = YouTube(url)
    video.check_availability()
    
    # Continue if check_availability doesn't raise errors 
    match(format):
        case "mp4": 
            success = get_video(video, dir)
        case "mp3": 
            success = get_audio(video, dir)
        case _: 
            raise ValueError(f"Media format '{format}' not supported")

    if success: 
        print(f"{'Download Successful!':<30}")
    else:
        print(f"{'Download Failed':<30}")


