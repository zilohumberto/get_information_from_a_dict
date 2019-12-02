import os
import subprocess
from solver import Solver

TEMP = "temp"
EXAMPLE_SOURCE = "{}/enterprise-attack/attack-pattern/".format(TEMP)


def download_repo():
    subprocess.run(["rm", "-r", TEMP])
    subprocess.run(["git", "clone", "https://github.com/mitre/cti.git", TEMP])


def get_data_from_repo():
    json_files = [
        os.path.join(EXAMPLE_SOURCE, f) for f in os.listdir(EXAMPLE_SOURCE)
        if (os.path.isfile(os.path.join(EXAMPLE_SOURCE, f)) and
            os.path.splitext(f)[1].lower() in [".json"])
    ]
    data_files = []
    for _file in json_files:
        with open(_file, 'r', encoding='utf-8') as info:
            data_files.append(info.read())
            info.close()
    return data_files


if __name__ == "__main__":
    for data in get_data_from_repo():
        result = Solver(
            data=data,
            expected_data=[
                "id",
                "objects[0].name",
                "objects[0].kill_chain_phases"
            ]
        ).start()
        print(result)
