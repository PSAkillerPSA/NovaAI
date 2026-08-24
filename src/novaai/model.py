from pathlib import Path
from urllib.request import urlopen
import sys

from llama_cpp import Llama


MODEL_URL = "http://78.154.103.11:16292/novaV1.gguf"

MODEL_DIR = Path.home() / ".novaai" / "models"
MODEL_PATH = MODEL_DIR / "novaV1.gguf"


def download_model():
    """Download NovaV1 if it is not already installed."""

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    print("NovaV1 model not found.")
    print("Downloading NovaV1...")

    try:
        with urlopen(MODEL_URL, timeout=30) as response:
            total_size = response.headers.get("Content-Length")

            if total_size is not None:
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
    """Return the local NovaV1 path, downloading it if necessary."""

    if not MODEL_PATH.exists():
        download_model()

    return MODEL_PATH


class NovaAI:
    """NovaAI interface for the NovaV1 model."""

    def __init__(
        self,
        context_size=2048,
        temperature=0.7,
        max_tokens=256,
        verbose=False,
    ):
        self.temperature = temperature
        self.max_tokens = max_tokens

        model_path = get_model_path()

        print("Loading NovaV1...")

        self.model = Llama(
            model_path=str(model_path),
            n_ctx=context_size,
            verbose=verbose,
        )

        print("NovaV1 loaded!")

    def ask(
        self,
        prompt,
        max_tokens=None,
        temperature=None,
    ):
        """Send a prompt to NovaV1 and return its response."""

        if max_tokens is None:
            max_tokens = self.max_tokens

        if temperature is None:
            temperature = self.temperature

        response = self.model(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )

        return response["choices"][0]["text"].strip()
