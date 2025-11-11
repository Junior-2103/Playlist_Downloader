"""."""

from pytubefix import Playlist
import flet as ft


class Main(ft.Container):
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.always_on_top = True
        self.page.window.width = 800
        self.page.window.height = 600
        self.page.title = "Playlst downloader"
        self._main()

    def _get_playlist(self, e: ft.Control):
        url = e.control.value
        if url.strip():
            playlist = Playlist(url)

            videos_generator = playlist.videos_generator()

            videos = [
                {
                    "image": video.thumbnail_url,
                    "channel": video.author,
                    "title": video.title,
                    "description": video.description,
                    "likes": video.likes,
                    "views": video.views,
                    "data": video.publish_date.strftime("%d/%m/%Y"),
                }
                for video in videos_generator
            ]

            self.page.add(
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(video["image"]),
                                        ft.Column(
                                            [
                                                ft.Text(video["title"]),
                                                ft.Text(
                                                    spans=[
                                                        ft.TextSpan(
                                                            f"{video['channel']} • {video['views']} • {video['likes']} • {video['data']}",
                                                            ft.TextStyle(
                                                                color="#888888"
                                                            ),
                                                        )
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                    height=100,
                                )
                            )
                            for video in videos
                        ],
                        scroll=ft.ScrollMode.ALWAYS,
                        height=500,
                    )
                )
            )

    def _main(self):
        url = ft.TextField(
            label="Digite a URL", tooltip="Oque é isso?", on_submit=self._get_playlist
        )
        self.page.add(url)


if __name__ == "__main__":
    ft.app(Main)
