import os
import logging
import click

PROJECT_FOLDER = os.path.dirname(__file__)
COMMANDS_FOLDER = os.path.join(PROJECT_FOLDER, 'tools')

LOGLEVEL = os.environ.get('TTACC_LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)
log = logging.getLogger(__name__)


# https://click.palletsprojects.com/en/8.1.x/commands/#custom-multi-commands
class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(COMMANDS_FOLDER):
            if not filename.startswith('.') and filename.endswith('.py'):
                log.debug(f'found command {filename}')
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(COMMANDS_FOLDER, name + '.py')
        if os.path.exists(fn):
            with open(fn) as f:
                log.debug(f'loading command {fn=!r}')
                code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
            return ns['cli']
        else:
            click.secho(f'ERR: {fn} not found', err=True, bold=True, fg='red')
            click.echo(ctx.get_help())
            ctx.exit()


@click.command(cls=MyCLI)
def cli():
    pass
