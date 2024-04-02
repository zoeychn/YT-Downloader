from pytube import YouTube

def download_video(url, output_path='./'):
    try:
        yt = YouTube(url)
        print("Downloading:", yt.title)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        print("Download complete!")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output directory (press Enter for current directory): ").strip()
    if output_path == '':
        output_path = './'
    
    download_video(url, output_path)
