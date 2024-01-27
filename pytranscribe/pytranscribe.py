#!/usr/bin/env python3
"""
Contains functions for transcribing audio streams.
"""

import argparse
import sys


def load_stream_from_file(file_path: str) -> bytes:
    """
    Loads a stream from the given path.

    file_path (str): The path to the file.

    Raises:
        OSError if the file could not be read.

    Returns:
        bytes: The loaded audio stream.
    """
    with open(file_path, "rb") as file:
        data = file.read()
        return data


def transcribe_stream(stream: bytes) -> list:
    """
    Transcribes an audio stream.

    stream (bytes): An audio stream.

    Returns:
        list: A list containing each word and their respective timestamp.
    """


def main() -> None:
    """
    Loads an audio stream from the provided path and transcribes it.
    """
    parser = argparse.ArgumentParser(
        prog="pytranscribe",
        description="Transcribe audio streams locally and efficiently.",
        epilog="Refer to the documentation for further help.",
    )
    parser.add_argument("filename")
    args = parser.parse_args()
    try:
        stream = load_stream_from_file(args.filename)
    except OSError as err:
        sys.exit(f"Could not load stream: {str(err)}")

    print(stream)


if __name__ == "__main__":
    main()
