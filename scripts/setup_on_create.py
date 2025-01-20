#!/usr/bin/env python3
import argparse
import logging
import os
import pathlib
import shutil

SCRIPT_DIR = pathlib.Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent.absolute()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("setup")


def create_compose_override():
    path = BASE_DIR / "docker-compose.override.yaml"
    if path.exists():
        return
    log.info("create %s", path)
    shutil.copy(SCRIPT_DIR / "docker-compose.default.yaml", path)

def main(args=None):
    parser = argparse.ArgumentParser(
        description="Setup the work directory for development of Odoo.",
    )
    parser.add_argument(
        "action",
        choices=["devcontainer", "compose"],
        help="how to set up the envrionment",
    )
    args = parser.parse_args(args)
    action = args.action

    if action in ('devcontainer', 'compose'):
        log.info("setup %s in %s", action, BASE_DIR)
        create_compose_override()

if __name__ == '__main__':
    main()
