import click

@click.command
@click.argument('name')
def cli(name):
    """Just a hello world example"""
    click.echo(f'Hello {name}!')
