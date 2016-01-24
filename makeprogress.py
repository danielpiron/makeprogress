import math


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


def render_bar(cells_filled, cell_count,
               empty_char='-', filled_char='=', bumper_char='>'):
    ''' Render the status bar'''
    assert cells_filled >= 0 and cell_count >= 0, \
        'cells_filled and cell_count must be positive values.'
    cells_filled = min(cell_count, cells_filled)
    cells_empty = cell_count - cells_filled
    if cells_empty == 0:
        bumper_char = ''
    cells_empty = cells_empty - len(bumper_char)
    return ''.join([cells_filled * filled_char, bumper_char,
                    cells_empty * empty_char])
