from pathlib import Path
import pymupdf.layout
import pymupdf4llm

def parse_pdf(filename: str) -> str:
    """
    Parses the specified pdf file and returns json text.
    
    Raises:
        ValueError: If filename is empty or not a .pdf file.
        FileNotFoundError: If the file does not exist.
        RuntimeError: If an unexpected error occurs during parsing.
    """
    path = Path(filename)

    if not filename:
        raise ValueError("Filename cannot be empty.")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"File '{filename}' is not a PDF.")
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {filename}")

    try:
        return pymupdf4llm.to_json(
            pymupdf.open(filename),
            show_progress=True
        )
    except Exception as e:
        raise RuntimeError(f"Failed to parse PDF '{filename}': {e}")
