from pathlib import Path

PYBASH_FILE = Path.home() / ".pybash.py"
EXECUTE_FILE = Path.home() / ".pybash_execute.py"  # TODO: this can be in install diir


def generate_executable():
    # Read contents of pybash file
    pybash = PYBASH_FILE.read_text().replace("    ", "\t") + "\n\n"
    # Read the pybash execute file template
    execute = Path("pybash_execute_default.py").read_text().replace("    ", "\t")

    # Create pybash execute file consisting of pybash file and a main function that
    # calls the appropriate user functions
    EXECUTE_FILE.write_text(f"{pybash}\n\n{execute}")


if __name__ == "__main__":
    generate_executable()
