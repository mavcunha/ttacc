#!/usr/bin/env python3

import logging
import click

from ttacc.lib.aws.constants import REGIONS

log = logging.getLogger('aws')

@click.group()
@click.option('-d', '--debug', is_flag=True, help='Enable debug information')
def cli(debug):
    """General operations on AWS information"""
    if debug:
        log.setLevel('DEBUG')


@cli.command()
@click.option('-n', '--name', is_flag=True, help='Display full region names')
@click.option('-e', '--emission', is_flag=True, help='Display emission factor')
def regions(name, emission):
    """List all known AWS regions"""
    log.debug(f'Listing all regions from {REGIONS=}')
    for r in REGIONS.regions:
        msg = (
            f'{r.name}'
            f'{"," + r.display_name if name else ""}'
            f'{"," + str(r.emission_factor) if emission else ""}'
        )
        click.echo(msg)


if __name__ == '__main__':
    cli()
