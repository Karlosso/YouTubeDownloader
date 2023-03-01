import sys

from pytube import YouTube
import os
import argparse
import logging as log

class YT:

    def __init__(self, args):
        self.url = args.url
        self.format = args.format
        self.out = args.out
        self.only_audio = False
        self.download()

    '''download YouTube video'''
    def download(self):

        # Set Format
        if self.format == 'mp3':
            self.only_audio = True
        elif self.format == 'mp4':
            self.only_audio = False

        # Filter
        log.info(msg='[#] Check YouTube Video')
        yt_url = YouTube(self.url)
        yt_video = yt_url.streams.filter(only_audio=self.only_audio).first()

        # Start Download
        log.info(msg='[#] Downloading ...')
        out_file = yt_video.download(output_path=self.out)
        base, ext = os.path.splitext(out_file)
        new_file = base + f'.{self.format}'
        os.rename(out_file, new_file)
        print('[+] Download completed!')

if __name__ == '__main__':

    log.basicConfig(level=log.ERROR)
    log.getLogger().addHandler(log.StreamHandler(sys.stdout))

    parser = argparse.ArgumentParser(
        prog='YouTubeDownloader',
        description='YouTubeDownloader downloads your Youtube Videos in MP3 or MP4 Format',
    )

    # Parse Arguments
    parser.add_argument('url', type=str, action='store', help='Url from the YouTube video')
    parser.add_argument('-f', '--format', choices=['mp4', 'mp3'], help='Format in which your Youtube video will be downloaded', nargs='?', default='mp3', type=str, dest='format')
    parser.add_argument('-o', '--out', help='Output path for the downloaded YouTube file', nargs='?', default=os.curdir, type=str, dest='out')
    args = parser.parse_args()

    try:
        obj = YT(args)
    except Exception as error:
        log.error(msg=f'[!] Exception: {error}')
