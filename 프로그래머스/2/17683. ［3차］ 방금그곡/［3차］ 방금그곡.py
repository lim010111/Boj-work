from typing import List

def solution(m: str, musicinfos: List[str]):
    
    # melodies = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    melody_mapping = {
        "C#": "0",
        "D#": "1",
        "F#": "2",
        "G#": "3",
        "A#": "4",
        "B#": "5",
    }
    for key in melody_mapping:
            m = m.replace(key, melody_mapping[key])

    vaild_melodies = []
    for index, musicinfo in enumerate(musicinfos):
        start, end, title, melody = musicinfo.split(',')
        for key in melody_mapping:
            melody = melody.replace(key, melody_mapping[key])
            
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        duration = 60 * (end_h - start_h) + (end_m - start_m)
        total_melody = melody * (duration // len(melody)) + melody[:(duration % len(melody))]

        if m in total_melody:
            vaild_melodies.append((total_melody, title, index))

    vaild_melodies = sorted(vaild_melodies, key=lambda info: (-len(info[0]), info[2]))
    # print(vaild_melodies)
    if not vaild_melodies:
        return "(None)"
    return vaild_melodies[0][1]