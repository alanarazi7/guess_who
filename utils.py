from datetime import datetime


def print_ts(s: str):
    now_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now_ts}] {s}")


def normalize_str(s: str):
    return s.lower().replace(".", '').strip()