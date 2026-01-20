"""app_case.py - Project script (example).

Author: Denise Case
Date: 2026-01

Practice key Python skills:
- docstring comments used at the start of each module and function
- pathlib for cross-platform file paths
- creating and writing files
- type hints (explicit types)
- logging (preferred over print)
- repetition patterns:
  - for year in range(...)
  - for item in list
  - list comprehension
  - while loop
- standard Python entry point pattern (if __name__ == "__main__":)

OBS:
  Don't edit this file - it should remain a working example.

REQ: All my files start with `case` in the filename to identify them as mine.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import time
from typing import Final

# External (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P02", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Find the current working directory (cwd) using pathlib.
# Use UPPER_SNAKE_CASE for constant names.
# Use `type hints` with Final for constants.

ROOT_DIR: Final[Path] = Path.cwd()


# === HERE IS A HELPER FUNCTION THAT WRITES A FILE AND LOGS IT ===


def write_text_file(path: Path, content: str) -> None:
    """Write content to a text file (overwriting if it exists).

    Arguments:
        path: Full path to the file to create/write.
        content: Text content to write.

    Returns:
        None
    """
    path.write_text(content, encoding="utf-8")
    LOG.info(f"WROTE file: {path.name}")


# === DECLARE REPETITION FUNCTION 1: FOR EACH IN NUMERIC RANGE ===


def create_files_from_numeric_range() -> None:
    """Create one file per quarter for a given inclusive quarter range.

    Arguments: None

    Returns:  None
    """
    # Log the start of this function
    LOG.info("START FUNCTION 1: create_files_from_numeric_range()")

    # Define a variable for the start
    start_quarter: int = 1
    # Define a variable for the end
    end_quarter: int = 4

    # LOG the starting name and value
    LOG.info(f"Starting quarter: {start_quarter}")

    # LOG the ending name and value
    LOG.info(f"Ending quarter: {end_quarter}")

    # For each number in the range (add one to the end to be INCLUSIVE)
    for quarter_number in range(start_quarter, end_quarter + 1):
        # Define a filename that starts with my name and uses the quarter number
        filename: str = f"case_quarter_{quarter_number}.txt"
        # Define the path for my new file
        path: Path = ROOT_DIR / filename
        # Define some content to put in the new file
        content: str = f"Here is my report for quarter number: {quarter_number}\n"
        # Call the provided helper function to write the file and log it
        write_text_file(path, content)


# === DECLARE REPETITION FUNCTION 2: FOR ITEM IN LIST ===


def create_files_from_list() -> None:
    """Create files based on a list of pet names.

    Arguments: None
    Returns:  None
    """
    # Log the start of this function
    LOG.info("START FUNCTION 2: create_files_from_list()")

    # Define a pet list
    pet_list: list[str] = ["dog", "cat", "fish"]

    # Log my pet list
    LOG.info(f"Pet list ={pet_list}")

    # For each pet name in the pet list (must have a colon and indentation matters!)
    for pet_name in pet_list:
        # Define a filename that starts with my name and uses this pet name
        filename: str = f"case_{pet_name}.txt"
        # Define the path for my new file
        path: Path = ROOT_DIR / filename
        # Define some content to put in the new file
        content: str = f"Here is my pet data for pet: '{pet_name}'\n"
        # Call the provided helper function to write the file and log it
        write_text_file(path, content)


# === DECLARE REPETITION FUNCTION 3: USING LIST COMPREHENSION ===


def create_files_using_list_comprehension() -> None:
    """Create files by transforming names using list comprehension.

    Arguments: None

    Returns: None
    """
    # Log the start of this function
    LOG.info("START FUNCTION 3: create_files_using_list_comprehension()")
    LOG.info("WHY: Use list comprehension to TRANSFORM a list into a new list.")
    LOG.info("WHY: They are super compact list transformations.")
    LOG.info("Read it as <do this logic> FOR each <item> IN <list>.")

    # Define my pet list
    pet_list: list[str] = ["dog", "cat", "fish"]
    # Log my pet list
    LOG.info(f"Pet list ={pet_list}")

    # Define a prefix (or any other transformation logic)
    prefix = "favorite_"

    # Use list comprehension syntax to create a new list from the pet list
    favorite_list: list[str] = [f"{prefix}{name}" for name in pet_list]

    # For each favorite name in the new favorite list
    for favorite in favorite_list:
        # Define a file name that starts with my name and uses this favorite name
        filename: str = f"case_{favorite}.txt"
        # Define the path for my new file
        path: Path = ROOT_DIR / filename
        # Define some content to put in the new file
        content: str = f"Here is the special data about my '{favorite}'\n"
        # Call the provided helper function to write the file and log it
        write_text_file(path, content)


# === DECLARE REPETITION FUNCTION 4: WHILE LOOP (PERIODIC) ===


def create_files_periodically() -> None:
    """Create a small number of files with a delay between each creation.

    Arguments: None
    Returns:   None
    """
    # Log the start of this function
    LOG.info("START FUNCTION 4: create_files_periodically()")
    LOG.info("WHY: Use while loop for REPETITIVE tasks with a WAIT or DELAY.")

    # Define wait_seconds: Seconds to wait between file writes.
    wait_seconds: int = 1
    # Define count: How many files to create.
    count: int = 3

    # Log the wait_seconds
    LOG.info(f"Waiting seconds between files: {wait_seconds}")
    # Log the count
    LOG.info(f"Number of files to create: {count}")

    # Define a counter variable
    i: int = 1

    # While the counter is less than or equal to the count
    while i <= count:
        # Define a filename that starts with my name and uses the counter
        # Use 02d formatting for leading zeros and two digits
        filename: str = f"case_{i:02d}.txt"
        # Define the path for my new file
        path: Path = ROOT_DIR / filename
        # Define some content to put in the new file
        content: str = f"If we accidentally make an infinite loop, this will go forever... We're on file count:  {i}\n"
        # Call the provided helper function to write the file and log it
        write_text_file(path, content)

        # Log the wait time
        LOG.info(f"Waiting {wait_seconds} seconds...")

        # Call the time.sleep() function to wait for the given number of wait_seconds
        time.sleep(wait_seconds)
        # IMPORTANT: Remember to increment the counter variable to avoid an infinite loop!
        # Set the value of i to itself plus one (this is the same as i = i + 1)
        i += 1


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point for the script.

    Creates files as visible artifacts which will be committed to Git.

    Arguments: None
    Returns:   None
    """
    log_header(LOG, "Automation: Creating Files with Repetition Patterns")

    LOG.info("START main()")

    # Task 1. Create one file for each number in a range
    create_files_from_numeric_range()

    # Task 2. Create one file for each item in a list
    create_files_from_list()

    # Task 3. Use a list comprehension to make a list from a list - then create a file for each
    create_files_using_list_comprehension()

    # Task 4. Create files periodically
    create_files_periodically()

    # To Delete these text files while working, run this command in terminal:
    # rm *.txt

    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
