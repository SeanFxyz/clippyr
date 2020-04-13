# clippyr
A script that extracts a specified series of clips and/or still images from a larger video file, which can be an existing local file or downloaded by the script via [youtube-dl](https://github.com/ytdl-org/youtube-dl).

	Usage: clippyr [OPTIONS]
	
	Options:
	  -f, --file TEXT    File to clip from.
	  -u, --url TEXT     The URL of a video to be downloaded
	  -c, --clip TEXT    A comma-separated list of clips or still images to
	                     extract from the specified url or file, specified by
	                     HH:MM:SS[.x][-HH:MM:SS[.x]] or [seconds][-[seconds]].
	  -o, --output TEXT  With -u, specifies youtube-dl output option. With -f,
	                     specifies output directory.
	  --help             Show this message and exit.


## Demo
[![asciicast](https://asciinema.org/a/u72Y9B848yjfhnuawb38pg9Zg.svg)](https://asciinema.org/a/u72Y9B848yjfhnuawb38pg9Zg)

## INSTALL
Currently, you can install clippyr by cloning this repository and from within the directory using `pip install .`. Use `pip install --editable .` if you'd like to install it while being able to modify it.

### Requirements
Other than those prerequisites installed automatically by pip, you will need to have ffmpeg installed.

Note: On some Linux distributions you may need to use 'python3' in place of 'python' and/or 'pip3' in place of 'pip'.

### Installation without venv (Unix/Linux):

	$git clone https://github.com/SeanaldSeanson/clippyr.git
	Cloning into 'clippyr'...
	remote: Enumerating objects: 51, done.
	remote: Counting objects: 100% (51/51), done.
	remote: Compressing objects: 100% (33/33), done.
	remote: Total 51 (delta 24), reused 41 (delta 17), pack-reused 0
	Unpacking objects: 100% (51/51), done.
	$cd clippyr/
	$pip install --editable .

### Installation with venv (Unix/Linux):

	$git clone https://github.com/SeanaldSeanson/clippyr.git
	Cloning into 'clippyr'...
	remote: Enumerating objects: 51, done.
	remote: Counting objects: 100% (51/51), done.
	remote: Compressing objects: 100% (33/33), done.
	remote: Total 51 (delta 24), reused 41 (delta 17), pack-reused 0
	Unpacking objects: 100% (51/51), done.
	$cd clippyr/
	$python -m venv venv
	$source venv/bin/activate
	(venv) $pip install --editable .

## EXAMPLES
	$clippyr -f example.mkv -c 4,2-6,00:00:10.05-00:23:05.5
	-- OUTPUT REDACTED --
	$ls output_clippyr
	example__clip0.mkv  example__clip1.mkv  example__image0.png
