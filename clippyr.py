import os, sys, youtube_dl, ffmpeg, click, re, json, ast
from pathlib import PurePath
from glob import glob

# Download video from URL, return output file name
def ydl_download(url, ydl_opts={}):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        ydl.process_info(info_dict)
        return ydl.prepare_filename(info_dict)

# Check a list of clip specifier strings and return a list of the bad ones.
def check_time_specs(specs, spec_type='clip'):
    re_sec = re.compile('^[0-9]+\.*[0-9]*$')
    re_stamp = re.compile('^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9]+$')
    is_bad = lambda t : re_sec.fullmatch(t) == None and re_sec.fullmatch(t) == None
    bad_specs = []
    for s in specs:
        if '-' in s:
            if spec_type == 'image':
                bad_specs.append(s)
            else:
                for t in s.split('-'):
                    if is_bad(s):
                        bad_specs.append(s)
        elif spec_type == 'clip' or is_bad(s):
            bad_specs.append(s)
    return bad_specs

# Unpacks a single timestamp to a float value in seconds. If not in
# timestamp format, returns original spec converted to float.
def unpack_spec(spec):
    if ':' in spec:
        h, m, s = spec.split(':')
        if '.' in s:
            s, ms = s.split('.')
        else:
            ms = 0
        return int(h) * 3600 + int(m) * 60 + int(s) + float(ms) / (10 ** len(ms))
    else:
        return float(spec)

# Extract clips from input_file, specified by time specifiers in clips.
def extract_clips(input_file, clips, output_dir='output_clippyr'):
    for i in range(len(clips)):
        clip = clips[i]
        start, end = clip.split('-')
        start, end = unpack_spec(start), unpack_spec(end)
        start = str(start)
        clip_len = str(end - float(start))
        path = PurePath(input_file)
        output_file = str(path.with_name(path.stem + '__clip' + format(i, '0' + str(int( (len(clips) / 10) ))) + path.suffix ))

        ffmpeg.input(input_file, ss=start).output(output_file, t=clip_len).overwrite_output().run()

# Extract still images from input_file, specified by time specifiers in images.
def extract_images(input_file, images, output_dir='output_clippyr'):
    for i in range(len(images)):
        image = images[i]
        image = str(unpack_spec(image))
        path = PurePath(input_file)
#        output_file = str(path.with_name(path.stem + '__image' + format(i, '0' + str(int( (len(images) / 10) ))) + '.png'))

        ffmpeg.input(input_file, ss=image).output(output_file, vframes=1).overwrite_output().run()

@click.command(context_settings={'ignore_unknown_options': True})
@click.option('-f', '--file', 'in_file', default='', multiple=False, help='File to clip from. Cannot be used with -u.')
@click.option('-u', '--url', default='', multiple=False, help='The URL of a video to be downloaded. Cannot be used with -f.')
@click.option('-c', '--clip', default=None, multiple=True, help='A clip to extract from the source file, specified by HH:MM:SS[.x]-HH:MM:SS[.x] or [seconds]-[seconds].')
@click.option('-i', '--image', default=None, multiple=True, help='A still image to extract from the source file, specified by HH:MM:SS[.x] or [seconds].')
@click.option('-o', '--output', help='With -u, specifies youtube-dl output option. With -f, specifies output directory.')
def clippyr(url, in_file, clip, image, output):

    if in_file and url:
        click.echo('Cannot use -f/--file and -u/--url simultaneously.')
        exit(1)
    elif in_file == '' and url == '':
        click.echo('Must provide a url with -u or file name with -f')
        exit(1)

    if output == '':
        if url:
            output = os.path.join('output_clippyr', '%(title)s-%(id)s.%(ext)s')
        elif in_file:
            output = 'output_clippyr'

    if url:
        output_dir = str(PurePath(output).parent)
    elif in_file:
        output_dir = output

    if os.path.isdir(output_dir) == False:
        if output_dir == 'output_clippyr':
            os.mkdir('output_clippyr')
        else:
            click.echo('Nonexistent non-default output directory ' + output_dir, err=True)
            exit(1)

    if url:
        source_file = ydl_download(url, ydl_opts={'outtmpl': output})
    elif in_file:
        source_file = in_file

    bad_specs = check_time_specs(clip, 'clip')
    bad_specs += check_time_specs(image, 'image')
    if len(bad_specs):
        for s in bad_specs:
            print('Bad clip specifier "' + s + '"')
        exit(1)

    extract_clips(source_file, clip)
    extract_images(source_file, image)

if __name__=='__main__':
    clippyr()
    exit(0)
