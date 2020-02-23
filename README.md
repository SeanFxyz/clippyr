# clippyr
A script that extracts a specified series of clips from a larger video file, which can be an existing local file or downloaded by the script via [youtube-dl](https://github.com/ytdl-org/youtube-dl).

	Usage: clippyr [OPTIONS]
	
	Options:
	  -f, --file TEXT    File to clip from. Cannot be used with -u.
	  -u, --url TEXT     The URL of a video to be downloaded. Cannot be used with
	                     -f.
	  -c, --clip TEXT    A clip to extract from the source file, specified by
	                     HH:MM:SS.x-HH:MM:SS.x or [seconds]-[seconds].
	  -i, --image TEXT   A still image to extract from the source file, specified
	                     by HH:MM:SS.x or [seconds].
	  -o, --output TEXT  youtube-dl output option. Stores files in
	                     ./output_clippyr/ by default.
	  --help             Show this message and exit.
