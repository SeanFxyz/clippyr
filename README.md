# clippyr
A script that extracts a specified series of clips from a larger video file, which can be an existing local file or downloaded by the script via [youtube-dl](https://github.com/ytdl-org/youtube-dl).


Usage: clippyr.py [OPTIONS]

Options:
  -f, --file TEXT    File to clip from. Cannot be used with -u.
  -u, --url TEXT     The URL of a video to be downloaded. Cannot be used with
                     -f.
  -c, --clip TEXT    The section of the last specified video to extract.
  -o, --output TEXT  Directory to store output files.
  --help             Show this message and exit.
