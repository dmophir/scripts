import ffmpeg
import os
import sys

# Get mp4 names
def get_video_names(path: str):
    return [path+'/'+video for video in os.listdir(path) if '.mp4' in video]

def get_sub_names(path: str):
	return [path+'/'+sub for sub in os.listdir(path) if '].en.' in sub]

def embed_sub(video_path: str, sub_path: str):
	nas_path = '/mnt/NAS/videos/TV Shows/Live/Forged in Fire/'
	season = video_path.split('/')[0] + '/'
	title = video_path.split('/')[1][:-4]
	output_file = nas_path + season + title + '.mkv'
	#print(f'output_file:\t{output_file}')

	input_ffmpeg = ffmpeg.input(video_path)
	input_ffmpeg_sub = ffmpeg.input(sub_path)

	input_video = input_ffmpeg['v']
	input_audio = input_ffmpeg['a']
	input_subtitle = input_ffmpeg_sub['s']
	output_ffmpeg = ffmpeg.output(
		input_video,
		input_audio,
		input_subtitle,
		output_file,
		vcodec='copy',
		acodec='copy',
		**{
			'metadata': f'title={title}',
			'metadata:s:s:0': 'language=en',
			'metadata:s:s:0': 'title=English',
		}
	)

	output_ffmpeg = ffmpeg.overwrite_output(output_ffmpeg)
	print(ffmpeg.compile(output_ffmpeg))
	ffmpeg.run(output_ffmpeg)

def match_pair(video: str, subs):
	sub = ''
	title = video.split('/')[1][22:-4]
	#print(f'path:\t{video}')
	#print(f'title:\t{title}')
	for s in subs:
		if title in s:
			sub = s
	#print(f'sub:\t{sub}')
	if len(sub) > 2:
		#print(f'merging video:\t{video} {sub}')
		embed_sub(video, sub)
	else:
		print(f'no subs for:\t{video}')

	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("no arg, quitting")
		quit()
	if sys.argv[1] == '--all':
		seasons = [season for season in os.listdir() if 'Season ' in season]
		print(f'seasons:\t{seasons}')
		for season in seasons[-1:]:
			#print(f'Season:\t{season}')
			videos = get_video_names(season)
			subs = get_sub_names(season)
			# print(videos)
			# print(subs)
			for vid in videos:
				#print(f'merging video:\t{vid}')
				match_pair(vid, subs)
		quit()
	else:
		videos = get_video_names(sys.argv[1])
		subs = get_sub_names(sys.argv[1])
		#print(videos)
		#print(subs)
		for vid in videos:
			match_pair(vid, subs)
		# match_pair(videos[0], subs)
		quit()