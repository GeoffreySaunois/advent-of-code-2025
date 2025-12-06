from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import typer

app = typer.Typer(help="Advent of Code helpers.")

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = REPO_ROOT / "template.py"


@app.command()
def setup(
    day: int = typer.Option(..., "--day", "-d", help="Day number to scaffold"),
) -> None:
    """Creates a new day folder, copy template, and download inputs."""
    day_str = f"{day:02d}"
    day_dir = REPO_ROOT / f"Day{day_str}"

    if day_dir.exists():
        typer.echo(f"{day_dir} already exists; nothing to do.")
        raise typer.Exit(code=0)

    if not TEMPLATE.exists():
        typer.echo(f"Template not found at {TEMPLATE}")
        raise typer.Exit(code=1)

    day_dir.mkdir(parents=True, exist_ok=True)

    target_py = day_dir / f"day{day_str}.py"
    shutil.copy(TEMPLATE, target_py)

    (day_dir / "test").touch()

    try:
        subprocess.run(
            [
                "aoc",
                "download",
                f"--day={day}",
            ],
            check=True,
            cwd=day_dir,
        )
    except FileNotFoundError:
        typer.echo("`aoc` command not found on PATH.")
        raise typer.Exit(code=1)
    except subprocess.CalledProcessError as exc:
        typer.echo(f"`aoc download` failed with exit code {exc.returncode}.")
        raise typer.Exit(code=exc.returncode)

    typer.echo(f"Created {day_dir} and downloaded inputs.")


if __name__ == "__main__":
    app()
