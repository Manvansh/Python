from pytube import YouTube

link = input("Link : ")
yt = YouTube(link)

print("Title Of Your Video : ", yt.title)

yd = yt.streams.first().download(output_path=r'C:\Users\manva\OneDrive\Desktop\YT_Vids')
yd = yt.streams.filter(progressive=True, file_extension='mp3')