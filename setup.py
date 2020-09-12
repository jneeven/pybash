import re
from pathlib import Path


def update_bashrc():
    bashrc = Path.home() / ".bashrc"
    contents = bashrc.read_text()
    to_write = Path("bashrc_code").read_text()

    contents, replacements = re.subn(
        r"\# \<START OF PYBASHRC CODE\>\n(.|\n)*\n\# \<END OF PYBASHRC CODE\>",
        to_write,
        contents,
    )
    if replacements == 0:
        contents += "\n" + to_write

    bashrc.write_text(contents)
    print(f"Modified {bashrc}")


if __name__ == "__main__":
    pybashrc_file = Path.home() / ".pybashrc.py"
    if not pybashrc_file.exists():
        pybashrc_file.write_text((Path("pybashrc") / "pybashrc_default.py").read_text())
        print(f"Created pybashrc file at {pybashrc_file}.")

    alias_file = Path.home() / ".pybashrc_aliases"
    if not alias_file.exists():
        alias_file.write_text((Path("pybashrc") / "pybashrc_aliases").read_text())
        print(f"Created pybashrc alias file at {alias_file}.")

    update_bashrc()
