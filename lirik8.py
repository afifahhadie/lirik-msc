import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.13):
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
        ("\nKapan terakhir kali kamu dapat tertidur tenang", 0.13),
        ("Tak perlu memikirkan tentang apa yang akan datang di esok hari", 0.12),
        ("Tubuh yang berpatah hati bergantung pada gaji", 0.13),
        ("Berlomba jadi asri mengais validasi", 0.13),
        ("Dan aku pun terhadir", 0.14),
        ("Seakan paling mahir", 0.14),
        ("Menenangkan dirimu", 0.13),
        ("Yang merasa terpinggirkan dunia", 0.13),
        ("Tak pernah adil", 0.14),
        ("Kita semua gagal", 0.13),
        ("Angkat minumanmu", 0.13),
        ("Bersedih bersama-sama", 0.14),
    ]
    delays = [0.3, 5.4, 10.5, 15.2, 19.6, 23.0, 26.4, 30.2, 34.1, 37.5, 41.0, 44.0]

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
