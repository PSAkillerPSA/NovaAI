from pathlib import Path
from urllib.request import urlopen
import sys

MODEL_URL = "http://78.154.103.11:16292/novaV1.gguf"

MODEL_DIR = Path.home() / ".novaai" / "models"
MODEL_PATH = MODEL_DIR / "novaV1.gguf"


def download_model():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    print("NovaV1 model not found.")
    print("Downloading NovaV1...")

    try:
        with urlopen(MODEL_URL, timeout=30) as response:
            total_size = response.headers.get("Content-Length")

            if total_size:
                total_size = int(total_size)

            downloaded = 0

            with open(MODEL_PATH, "wb") as file:
                while True:
                    chunk = response.read(1024 * 1024)

                    if not chunk:
                        break

                    file.write(chunk)
                    downloaded += len(chunk)

                    if total_size:
                        percent = downloaded / total_size * 100
                        sys.stdout.write(
                            f"\rDownloading NovaV1: {percent:.1f}%"
                        )
                        sys.stdout.flush()

        print("\nNovaV1 downloaded successfully.")

    except Exception:
        if MODEL_PATH.exists():
            MODEL_PATH.unlink()

        print("\nFailed to download NovaV1.")
        raise


def get_model_path():
    if not MODEL_PATH.exists():
        download_model()

    return MODEL_PATH
