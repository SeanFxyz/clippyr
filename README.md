# clippyr
A script that extracts a specified series of clips and/or still images from a larger video file, which can be an existing local file or downloaded by the script via [youtube-dl](https://github.com/ytdl-org/youtube-dl).

	Usage: clippyr [OPTIONS]
	
	Options:
	  -f, --file TEXT    File to clip from. Cannot be used with -u.
	  -u, --url TEXT     The URL of a video to be downloaded. Cannot be used with
	                     -f.
	  -c, --clip TEXT    A clip to extract from the source file, specified by
	                     HH:MM:SS[.x]-HH:MM:SS[.x] or [seconds]-[seconds].
	  -i, --image TEXT   A still image to extract from the source file, specified
	                     by HH:MM:SS[.x] or [seconds].
	  -o, --output TEXT  With -u, specifies youtube-dl output option. With -f,
	                     specifies output directory.
	  --help             Show this message and exit.

## INSTALL
Currently, you can install clippyr by cloning this repository and from within the directory using `pip install .`. Use `pip install --editable .` if you'd like to install it while being able to modify it.

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

Note: On some Linux distributions you may need to use 'python3' in place of 'python' and/or 'pip3' in place of 'pip'.

## EXAMPLES
	$clippyr -f example.mkv -i 4 -c 2-6 -c 00:00:10.05-00:23:05.5
	-- OUTPUT REDACTED --
	$ls output_clippyr
	example__clip0.mkv  example__clip1.mkv  example__image0.png  example.mkv
