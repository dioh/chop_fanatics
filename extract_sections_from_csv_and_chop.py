#!/usr/bin/env python3

import pandas as pd
import os
import sys
import time
import datetime

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

filename = sys.argv[1]
df = pd.read_csv(filename)


def from_time_to_sec(time_):
    patterns = ['%H', '%M:%S', "%H:%M:%S"]
    for pattern in patterns:
        try:
            x = time.strptime(time_.strip(), pattern)
            return datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        except Exception as e:
            pass

for row_index, row in df.iterrows():
    ft = row['From-To']
    start = from_time_to_sec(ft.split('-')[0])
    end = from_time_to_sec(ft.split('-')[1])
    ffmpeg_extract_subclip(row['File'], start, end, targetname=f"{row['Volume']}_{row['Section']}_{row['Title']}.mp4")




