"""Log output: generates a random string on startup and prints it every 5 seconds."""

import time
import uuid
from datetime import datetime, timezone

INTERVAL_SECONDS = 5


def main() -> None:
    random_string = str(uuid.uuid4())  # generated once, kept in memory

    while True:
        timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
        print(f"{timestamp.replace('+00:00', 'Z')}: {random_string}", flush=True)
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
