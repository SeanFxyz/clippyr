from setuptools import setup

setup(
    name='clippyr',
    version='0.1',
    py_modules=['clippyr'],
    install_requires=['click', 'youtube-dl', 'ffmpeg_python'],
    entry_points='''
        [console_scripts]
        clippyr=clippyr:cmd
    ''',
)
