import yt_dlp
import os

def download_playlist(playlist_url, download_path, video_range=None):
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': False,
    }

    if video_range:
        ydl_opts['playlist_items'] = video_range

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Error downloading playlist: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    playlist_url = input("Enter the YouTube playlist URL: ")
    folder_title = input("Enter the Folder title: ")
    download_path = os.path.join("/app/download", folder_title)
    video_range = input("Enter the video range (e.g., '1-3,5,7-9') or leave blank to download all: ")

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    download_playlist(playlist_url, download_path, video_range)
    print("Download completed!")
