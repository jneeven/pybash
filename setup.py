import re
from pathlib import Path


def update_bashrc():
    bashrc = Path.home() / ".bashrc"
    contents = bashrc.read_text()
    to_write = Path("bashrc_template").read_text()

    contents, replacements = re.subn(
        r"\# \<START OF PYBASHRC CODE\>\n(.|\n)*\n\# \<END OF PYBASHRC CODE\>\n",
        to_write,
        contents,
    )
    if replacements == 0:
        contents += "\n" + to_write

    bashrc.write_text(
        contents.replace("<INSTALL_DIR>", str(Path("pybashrc").absolute())),
    )
    print(f"Modified {bashrc}")


if __name__ == "__main__":
    pybashrc_file = Path.home() / ".pybashrc.py"
    if not pybashrc_file.exists():
        pybashrc_file.write_text(
            (Path("pybashrc") / "pybashrc_template.py").read_text()
        )
        print(f"Created pybashrc file at {pybashrc_file}.")

    alias_file = Path("pybashrc") / ".pybashrc_aliases"
    alias_file.write_text((Path("pybashrc") / "alias_template").read_text())
    print(f"Created pybashrc alias file at {alias_file}.")

    update_bashrc()
