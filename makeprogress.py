import math
import time
import sys


def render_progress(max_value, width=20):
    def wrapper(progress):
        return render_bar(progress, max_value, width)
    return wrapper


def render_message(message=''):
    def wrap(inner):
        def wrapper(*args, **kwargs):
            return ' '.join([inner(*args, **kwargs), message])
        return wrapper
    return wrap


def render_percent(inner):
    def wrapper(progress, max_value, *args, **kwargs):
        percentage = int(math.floor(progress * 100 / max_value))
        pct_text = '{:>3}%'.format(percentage)
        return ' '.join([inner(progress, max_value,
                               *args, **kwargs), pct_text])
    return wrapper


def render_label(inner, label='Progress'):
    def wrapper(*args, **kwargs):
        return ' '.join([label, inner(*args, **kwargs)])
    return wrapper


def render_borders(inner, left_char='[', right_char=']'):
    def wrapper(*args, **kwargs):
        return ''.join([left_char, inner(*args, **kwargs), right_char])
    return wrapper


@render_message('This is a test')
@render_percent
@render_label
@render_borders
def render_bar(progress, max_value, width,
               empty_char='-', filled_char='=', bumper_char='>'):
    filled = int(math.floor(progress * width / max_value))
    remaining = width - filled

    bar_parts = []
    bar_parts.append(filled_char * filled)

    if remaining:
        bar_parts.append(bumper_char)
        remaining = remaining - len(bumper_char)

    bar_parts.append(empty_char * remaining)
    return ''.join(bar_parts)


if __name__ == '__main__':
    MAX_VALUE = 10
    WIDTH = 20
    if len(sys.argv) > 1:
        MAX_VALUE = int(sys.argv[1])

    if len(sys.argv) > 2:
        WIDTH = int(sys.argv[2])

    progress = render_progress(MAX_VALUE, WIDTH)
    print('')
    for n in range(MAX_VALUE + 1):
        sys.stdout.write('\r' + progress(n))
        sys.stdout.flush()
        time.sleep(1)
