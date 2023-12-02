import argparse
import datetime
import fileinput
import pathlib
import shutil

def gen_day_dir(day: str, year: str):
    tpl_path = pathlib.Path("day_tpl")
    year_path = pathlib.Path(year)

    if not year_path.exists():
        year_path.mkdir()

    day_fmt = f"{int(day):02d}"
    nb_path = year_path / f"{day_fmt}.ipynb"
    input_path = year_path / f"{day_fmt}_input.txt"

    shutil.copy(tpl_path / "input.txt", input_path)
    shutil.copy(tpl_path / "main.ipynb", nb_path)

    with fileinput.FileInput(nb_path, inplace=True) as f:
        for line in f:
            new_line = line \
                .replace("Day n", f"Day {day_fmt}") \
                .replace("input.txt", input_path.name)
            print(new_line, end="")

    print(f"Day {day_fmt} created.")


if __name__ == "__main__":
    today_day = str(datetime.date.today().day)
    today_year = str(datetime.date.today().year)

    parser = argparse.ArgumentParser()
    parser.add_argument("--day", default=today_day)
    parser.add_argument("--year", default=today_year)
    args = parser.parse_args()

    gen_day_dir(day=args.day, year=args.year)
