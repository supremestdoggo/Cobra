import click
import os
from .ast_optimizer import optimize_src


def optimize_file(path):
    with open(path, "r+") as _file:
        content = "\n".join(_file.readlines())
        optimized_content = optimize_src(content)
        _file.seek(0)
        _file.truncate()
        _file.write(optimized_content)

def optimize_dir(path, recursive):
    for _path in os.listdir(path):
        if os.isdir(_path):
            if recursive:
                optimize_dir(path)
        else:
            if _path.endswith(".py"):
                optimize_file(_path)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option("-d", "--directory",help="Optimize a directory rather than a single file", is_flag=True)
@click.option("-r", "--recursive", help="Recursively optimize directories (requires the directory flag be used)", is_flag=True)
@click.argument("path")
def optimize_path(directory, recursive, path):
    """Optimize Python files and directories."""
    if directory:
        optimize_dir(directory, recursive)
    else:
        optimize_file(path)

optimize_path()