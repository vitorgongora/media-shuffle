# Media Shuffle

**Media Shuffle** shuffles your media files (photos, videos, etc.) for reproduction in systems that don't have a Shuffle Mode (such as Smart TV's playing content from USB storage).

## First use
If your files haven't already been ordered before, that is their names aren't in one of the formats below:

**[000] file_name
(20) file_name
15 file_name**

Then put all your files in a folder with the script **media_shuffle.py** and run the command below inside the folder

    python media_shuffle.py -n

If you run the script without the **-n** flag and your file's name start with a number or a bracket/parenthesis the content inside (), [], and the number will be overwritten. 

## Shuffling ordered files
When your files have already been ordered for the first time and you wish to change that order run the command below and a new random order will be used to name the files.

    python media_shuffle.py


## Flags

|Flag| Description | Default |
|--|--|--|
| -h | Show help message | n/a
| -n | Ignores previous ordering numbers if existent and adds new ones without overwriting | false
| -s | Selects separator for the file ordering number (br for "[]", pa for "()") | none

