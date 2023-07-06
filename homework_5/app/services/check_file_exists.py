from app.config import FILES_INPUT_DIR


def check_file_exists():
    gitkeep_file_path = FILES_INPUT_DIR.joinpath(".gitkeep")
    if gitkeep_file_path.exists():
        print(f"File exists: {gitkeep_file_path.as_uri()}")
    else:
        raise FileNotFoundError(f"File not found: {gitkeep_file_path.as_uri()}")
