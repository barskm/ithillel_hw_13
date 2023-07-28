class Player:

    def __init__(self, name, video_link, duration=''):
        self.name = name
        self.video_link = video_link
        self.duration = duration

    def play(self):
        import requests

        try:
            r = requests.get(self.video_link)
        except:
            r = 0

        if r == 0:
            print(f'Film \"{self.name}\" with link {self.video_link} not exist')
        else:
            print(f'Film \"{self.name}\" with link {self.video_link} OK')

    def pause(self):
        pass

    def save_last_time(self):
        pass

    def change_quality(self):
        pass

