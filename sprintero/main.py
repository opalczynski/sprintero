# -*- coding: utf-8 -*-

import click

import sys
sys.path.append('/home/sopalczy/projects/sprintero-core')

from sprintero.commands import top_level

cli = click.CommandCollection(
    sources=[top_level]
)


def main():
    cli(obj={})

if __name__ == '__main__':
    cli(obj={})
