import os, sys, youtube_dl, ffmpeg, click, re, logging, json, ast
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
def check_clip_specs(specs):
    re_sec = re.compile('^[0-9]+\.*[0-9]*$')
    re_stamp = re.compile('^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9]+$')
    bad_specs = []
    for s in specs:
        for t in s.split('-'):
            if re_sec.fullmatch(t) == None and re_sec.fullmatch(t) == None:
                bad_specs.append(s)
    return bad_specs

def unpack_spec(spec):
    l = spec.split('-')
    if len(l) == 1:
        return (l[0], l[0])
    elif len(l) == 2:
        return (l[0], l[1])
    exit(1)

# Extract clip from input_file, specified by 
def extract_clips(input_file, clips):
    for i in range(len(clips)):
        clip = clips[i]
        start, end = unpack_spec(clip)
        path = PurePath(input_file)
        output_file = str(path.with_name(path.stem + '__clip' + format(i, '0' + str(int( (len(clips) / 10) ))) + path.suffix ))

        clip_l = clip.split('-')
        if len(clip_l) == 1:
            start = clip
            end = start
        elif len(clip_l) == 2:
            start, end = clip_l
            
        ffmpeg.input(input_file, ss=start).output(output_file, to=end).run()


@click.command(context_settings={'ignore_unknown_options': True})
@click.option('-u', '--url', default='', help='The URL of a video to be downloaded.')
@click.option('-c', '--clip', default=None, multiple=True, help='The section of the last specified video to extract.')
@click.option('-o', '--output', default=os.path.join('output_clippyr', '%(title)s-%(id)s.%(ext)s'), help='Directory to store output files.')
@click.argument('ydl_opts', nargs=-1)
def cmd(url, clip, ydl_opts, output=os.path.join('output_clippyr', '%(title)s-%(id)s.%(ext)s')):


    output_dir = str(PurePath(output).parent)
    if os.path.isdir(output_dir):
        if output_dir == 'output_clipper':
            os.mkdir('output_clippyr')
        else:
            click.echo('Nonexistant non-default output directory ' + output_dir, err=True)

    source_file = ydl_download(url, ydl_opts={'outtmpl': output})

    for s in check_clip_specs(clip):
        print('Bad clip specifier "' + s + '"')
        exit(1)

    extract_clips(source_file, clip)

if __name__=='__main__':
    cmd()
    exit(0)
