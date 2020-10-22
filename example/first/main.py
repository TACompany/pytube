from pytube import YouTube

video_path = '/Python/YouTube/video/'
audio_path = '/Python/YouTube/audio/'
videos_file = 'videos.txt'
video_list = []
download_type = [1, 2] # if 1 it download video, elif 2 it download audio, elif 1 and 2 it video and audio all
a = 1
c = 0

with open(videos_file, 'r') as f:
    videos_file = f.read().split('\n')

    for url in videos_file:
        video_list.append(url)

print(f"All added! : {len(video_list)}")

for url in video_list:
    yt = YouTube(url)
    try:
        if download_type == [1, 2]:
            st = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(video_path)
            print(f"Downloaded - {yt.title} ({a}/{len(video_list)})")
            st = yt.streams.filter(only_audio=True, adaptive=True).order_by('abr').desc()[0].download(audio_path)
            print(f"Downloaded - {yt.title} ({a}/{len(video_list)})")
        elif 1 in download_type:
            st = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(video_path)
    except Exception as e:
        print(f"Error on download: {e} ({a}/{len(video_list)})")
        c += 1

    a += 1

if c == 0:
    print(f'All downloaded! : {a - 1}') # Because after "for" it add another 1
else:
    print(f'Downloaded')