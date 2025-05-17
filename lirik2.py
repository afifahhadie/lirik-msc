import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
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
        ("\nTalk about our future like we had a clue", 0.09),
        ("Never planned that one day, I'd be losing you", 0.08),
        ("In another life", 0.09),
        ("I would be your girl", 0.08),
        ("We keep all our promises", 0.09),
        ("Be us against the world", 0.08),
    ]
    delays = [0.3, 4.5, 9.1, 13.5, 17.8, 22.3]

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
