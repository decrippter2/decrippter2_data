from pathlib import Path

from decrippter2_data.main import entrypoint_cicd

if __name__ == "__main__":
    datadir = Path(__file__).parent.parent.joinpath("data/")
    entrypoint_cicd(datadir)
