import subprocess
import re

SOURCE = "Playlist.m3u"
OUTPUT = "Playlist-live.m3u"

with open(SOURCE, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

out = []

for line in lines:

    url = line.strip()

    if ("youtube.com/" in url or "youtu.be/" in url):

        print("Resolving:", url)

        try:

            result = subprocess.check_output(
                [
                    "yt-dlp",
                    "-g",
                    url
                ],
                text=True,
                timeout=90
            )

            stream = result.splitlines()[0].strip()

            out.append(stream + "\n")

        except Exception:

            print("Offline:", url)

            out.append(url + "\n")

    else:

        out.append(line)

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.writelines(out)

print("Generated", OUTPUT)
