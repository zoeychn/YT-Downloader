# YT-Downloader

This is the basic functionality of the YouTube downloader script:

1. Import the `YouTube` class from the `pytube` library. This class allows us to interact with YouTube videos and download them.

2. Define a function called `download_video(url, output_path='./')`. This function takes two parameters:
   - `url`: The URL of the YouTube video to be downloaded.
   - `output_path`: The directory where the downloaded video will be saved. By default, it's set to our current directory.

3. Inside the `download_video` function, we download the video using a try-except block:
   - Create a `YouTube` object by passing the video URL.
   - Print the title of the video to indicate which video is being downloaded.
   - Get the highest resolution stream of the video using `yt.streams.get_highest_resolution()` to download the best quality available.
   - Call the `download` method on the stream object to initiate the download - we provide the output path where the video will be saved.

4. If any error occurs during the download process, it will be caught by the except block, and an error message will be printed.

5. The `__main__` block:
   - Prompts the user to enter the YouTube video URL.
   - Prompts the user to specify the output directory where the video will be saved. If the user doesn't provide any input, the default output directory is set to the current directory.
   - Calls the `download_video` function with the provided URL and output directory.

So, when you run the script:
- You'll be asked to enter the YouTube video URL.
- You can optionally specify the output directory where the video will be saved.
- The script will then download the video from the provided URL, save it to the specified output directory, and print a message indicating that the download is complete.
