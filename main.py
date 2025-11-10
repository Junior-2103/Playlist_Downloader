"""."""

from pytubefix import Playlist, YouTube
import flet as ft


class Main(ft.Container):
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.always_on_top = True
        self.page.window.width = 500
        self.page.window.height = 500
        self.page.title = "Playlist downloader"
        self.main()

    def main(self):
        self.page.add(ft.Text("Hello World!"))


# https://youtube.com/playlist?list=PLf0A4V8_hvaOXgkIeIWBZfLGgjrW8hZz4&si=eXep1MHGyPMCefoi

if __name__ == "__main__":
    ft.app(Main)
