import sys
import time


SAVE_POSITION = "\033[s"
RESTORE_SAVED = "\033[u"

animation = (
    (" \\ / ",
     "*   -",
     " / \\ "),
    (" * / ",
     "-   -",
     " / \\ "),
    (" \\ * ",
     "-   -",
     " / \\ "),
    (" \\ / ",
     "-   *",
     " / \\ "),
    (" \\ / ",
     "-   -",
     " / * "),
    (" \\ / ",
     "-   -",
     " * \\ "))

def print_animation(index):
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write(animation[index][0] + '\n')
    sys.stdout.write(animation[index][1] + '\n')
    sys.stdout.write(animation[index][2] + '\n')
    sys.stdout.flush()
    index += 1
    if index == len(animation):
        index = 0
    return index


MAX = 100

sys.stdout.write('\n\n\n')
animation_index = 0
for i in range(MAX):
    animation_index = print_animation(animation_index)
    time.sleep(0.2)

# for i in range(MAX):
#     sys.stdout.write(f"\rProgress: {i*100//MAX}%")
#     sys.stdout.flush()
#     time.sleep(0.1)
# sys.stdout.write(f"\rProgress: {MAX//MAX*100}%\nComplete\n")
