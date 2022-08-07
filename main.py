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
        yt_video = yt_url.streams.filter(only_audio=True).first()

        # start download
        print('Downloading ...')
        out_file = yt_video.download(output_path=self.config['download_path'])
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print('Download completed!')


if __name__ == '__main__':
    obj = YT()
    obj.download()
