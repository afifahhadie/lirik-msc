import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.14):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nI'm going under", 0.14),
        ("Storm, lightning, thunder", 0.13),
        ("I'm drowning in the deepest of truths", 0.14),
        ("Fuck, I think I'm falling for you\n", 0.15),
    ]
    delays = [0.3, 4.9, 9.6, 14.8]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
