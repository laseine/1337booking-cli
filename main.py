#!bin/python3
import click
from src import Auth

# TODO: login + logout + status

auth = Auth.Auth("http://localhost")


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command(help='Login to your admin account')
def login():
    if auth.isLogged():
        click.echo(click.style("You are already logged in.", fg="red"))
        return
    usr = click.prompt('Username', type=str)
    pwd = click.prompt('Password', type=str, hide_input=True)
    res = auth.login(usr, pwd)
    if 'error' in res:
        click.echo(click.style(res['error'], fg="red"))
        return
    click.echo(click.style("Logged in successfully.", fg="green"))


@main.command(help='Logout from your account')
def logout():
    if not auth.isLogged():
        click.echo(click.style("You are not logged in.", fg="red"))
        return
    res = auth.logout()
    if 'error' in res:
        click.echo(click.style(res['error'], fg="red"))
        return
    click.echo(click.style("Logged out successfully.", fg="green"))


@main.command(help='Print your current status')
def status():
    if auth.isLogged():
        click.echo("You are logged in.")
        return
    click.echo("You are not logged in.")


if __name__ == '__main__':
    main()
