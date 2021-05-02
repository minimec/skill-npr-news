# Copyright 2020 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import urllib.request

def srf():
    """Custom news fetcher for SRF Swiss German News Broadcast"""
    # Be sure that variables are empty
    line = None
    match = None

    # Get and format RSS feed file
    feed = 'https://www.srf.ch/feed/podcast/sd/4d8995b0-8492-4e6c-b97d-1030781d815f.xml'
    data = urllib.request.urlopen(feed).read().decode('utf-8').splitlines(True)

    # Isolate newest (first) news feed in RSS file (first match)
    pattern = re.compile("enclosure")
    for line in data:
        for match in re.finditer(pattern, line):
          continue
        if match != None:
          break

    # Isolate mp3 link
    url = line.split('url="') [1].lstrip().split('?asset') [0]

    return url
    
def rts():
    """Custom news fetcher for RTS Swiss French News Broadcast"""
    # Be sure that variables are empty
    line = None
    match = None

    # Get and format RSS feed file
    feed = 'https://www.rts.ch/la-1ere/programmes/le-journal-horaire/podcast/?flux=rss'
    data = urllib.request.urlopen(feed).read().decode('utf-8').splitlines(True)

    # Isolate newest (first) news feed in RSS file (first match)
    pattern = re.compile("enclosure")
    for line in data:
        for match in re.finditer(pattern, line):
          continue
        if match != None:
          break

    # Isolate mp3 link
    url = line.split('url="') [1].lstrip().split('?media') [0]

    return url
    
def rsi():
    """Custom news fetcher for RSI Swiss Italian News Broadcast"""
    # Be sure that variables are empty
    line = None
    match = None

    # Get and format RSS feed file
    feed = 'https://www.rsi.ch/rete-uno/programmi/informazione/radiogiornale/?f=podcast-xml&type=itunes'
    data = urllib.request.urlopen(feed).read().decode('utf-8').splitlines(True)

    # Isolate newest (first) news feed in RSS file (first match)
    pattern = re.compile("enclosure")
    for line in data:
        for match in re.finditer(pattern, line):
          continue
        if match != None:
          break

    # Isolate mp3 link
    url = line.split('url="') [1].lstrip().split('"') [0]

    return url         
