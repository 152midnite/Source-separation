import io
import sys
import builtins
import traceback
from functools import wraps


def opener(old_open):
    @wraps(old_open)
    def tracking_open(*args, **kw):
        file = old_open(*args, **kw)

        old_close = file.close
        @wraps(old_close)
        def close():
            old_close()
            open_files.remove(file)
        file.close = close
        file.stack = traceback.extract_stack()

        open_files.add(file)
        return file
    return tracking_open


def print_open_files():
    print(f'### {len(open_files)} OPEN FILES: [{", ".join(f.name for f in open_files)}]', file=sys.stderr)
    for file in open_files:
        print(f'Open file {file.name}:\n{"".join(traceback.format_list(file.stack))}', file=sys.stderr)


open_files = set()
io.open = opener(io.open)
builtins.open = opener(builtins.open)