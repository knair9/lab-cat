'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    chunk_size = 4096
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)
        sys.stdout.buffer.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        # Use sys.stdin if it's a TTY, otherwise use sys.stdin.buffer
        if sys.stdin.isatty():
            for line in sys.stdin:
                sys.stdout.write(line)
        else:
            cat(sys.stdin.buffer)
