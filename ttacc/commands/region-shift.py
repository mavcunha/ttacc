import click
import pandas

from pathlib import Path

from ttacc.lib.utils import log

def parse_csv(filename):
    # get region carbon data
    f = pandas.read_csv(Path.cwd().joinpath(filename))
    f_data = dict(zip(f.region, f.co2eq))
    return f_data

def convert_to_energy(entries):
    for (k, v) in entries.items():
        print(k)
        print(v)

@click.group(invoke_without_command=True)
@click.option('-d', '--debug', is_flag=True, help='Enable debug information')
@click.option('--global', '_global_shift', help='Sets the shift to be global', is_flag=True)
@click.argument('file')
def cli(file, debug, _global_shift):
    """Show possible carbon savings by moving regions"""
    log.set('region-shift')
    if debug:
        log.setLevel('DEBUG')

    log.debug(f'parsing {file=}')
    print(parse_csv(file))

