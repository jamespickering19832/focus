"""Utility helpers for the Focus application."""

ALLOWED_EXTENSIONS = {"csv"}


def allowed_file(filename: str) -> bool:
    """Check if the uploaded file has an allowed extension.

    The check is case-insensitive and currently only allows CSV files.

    Parameters
    ----------
    filename: str
        Name of the file to validate.

    Returns
    -------
    bool
        True if the file extension is permitted, otherwise False.
    """

    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
