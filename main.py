from pytube import YouTube
import yaml
import os


class YT:

    def __init__(self):
        self.url = ''
        self.config_path = 'config.yml'
        self.config = ''

    '''load config file'''
    def load_config(self):
        with open(self.config_path, 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as error:
                print(error)

    '''download YouTube video'''
    def download(self):
        # load config
        self.load_config()

        # get informations
        self.url = input('Enter YouTube Url: ')
        yt_url = YouTube(self.url)
        yt_video = yt_url.streams.get_audio_only()

        # start download
        print('Downloading ...')
        os.chdir(self.config['download_path'])
        yt_video.download()
        print('Download completed!')


if __name__ == '__main__':
    obj = YT()
    obj.download()
