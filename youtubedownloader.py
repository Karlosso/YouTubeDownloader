from pytube import YouTube
import os
import argparse


class YT:

    def __init__(self, args):
        self.url = args.url
        self.format = args.format[0]
        self.audio = False
        self.download()

    '''download YouTube video'''
    def download(self):

        # Set Format
        if self.format == 'mp3':
            self.audio = True
        elif self.format == 'mp4':
            self.audio = False

        # Filter
        print('[#] Check YouTube Video')
        yt_url = YouTube(self.url)
        yt_video = yt_url.streams.filter(only_audio=self.audio).first()

        # Start Download
        print('[#] Downloading ...')
        out_file = yt_video.download(output_path=os.curdir)
        base, ext = os.path.splitext(out_file)
        new_file = base + f'.{self.format}'
        os.rename(out_file, new_file)
        print('[+] Download completed!')



if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='YouTubeDownloader',
        description='YouTubeDownloader downloads your Youtube Videos in MP3 or MP4 Format',
    )

    # Parse Arguments
    parser.add_argument('url', type=str, action='store')
    parser.add_argument('-f', '--format', choices=['mp4', 'mp3'], help='Format in which your Youtube video will be downloaded', nargs=1, default='mp3', type=str, dest='format')
    args = parser.parse_args()

    try:
        obj = YT(args)
    except Exception as error:
        print(f'[!] Exception: {error}')
