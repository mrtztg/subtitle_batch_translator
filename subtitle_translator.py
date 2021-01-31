import os
import time
from utils import translate_and_compose
import re

for root, dirs, files in os.walk("."):
    for name in files:
        if re.match(r".*(?<!-\w{2})\.srt$", name):
            folder = os.path.abspath(root)
            source_file = os.path.join(folder, name)
            dest_file = os.path.join(folder, f'{os.path.splitext(name)[0]}-fa.srt')
            if os.path.isfile(dest_file):
                print(f'"{name}" translated before')
            else:
                print(f"translating {name}")
                file_must_update = False
                with open(source_file, 'r') as srt_file:
                    srt_content = srt_file.read()
                    # remove extra numbers
                    new_srt_content = re.sub(r"(\d+)(\n+)(\d+\n+)", r"\n\1\n", srt_content)

                    # remove newLine from file beginning
                    new_srt_content = re.sub(r"^\n+", "", new_srt_content)

                    # replace &amp;
                    new_srt_content = new_srt_content.replace("&amp;", "&")
                if srt_content is not new_srt_content:
                    with open(source_file, 'w') as srt_file_w:
                        srt_file_w.write(new_srt_content)
                translate_and_compose(source_file, dest_file, 'en', 'fa', mode='naive', both=False)
                print(f'translated "{name}"')
                time.sleep(3)
