import re
from pathlib import Path


def update_bashrc():
    bashrc = Path.home() / ".bashrc"
    contents = bashrc.read_text()
    to_write = Path("bashrc_code").read_text()

    contents, replacements = re.subn(
        r"\# \<START OF PYBASH CODE\>\n(.|\n)*\n\# \<END OF PYBASH CODE\>",
        to_write,
        contents,
    )
    if replacements == 0:
        contents += "\n" + to_write

    bashrc.write_text(contents)
    print(f"Modified {bashrc}")


if __name__ == "__main__":
    pybash_file = Path.home() / ".pybash.py"
    if not pybash_file.exists():
        pybash_file.write_text((Path("pybash") / "pybash_default.py").read_text())
        print(f"Created pybash file at {pybash_file}.")

    alias_file = Path.home() / ".pybash_aliases"
    if not alias_file.exists():
        alias_file.write_text((Path("pybash") / "pybash_aliases").read_text())
        print(f"Created pybash alias file at {alias_file}.")

    update_bashrc()
