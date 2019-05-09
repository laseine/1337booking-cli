#!bin/python3
import click, datetime
from src import Auth, Api

# TODO: login + logout + status

auth = Auth.Auth("http://localhost")


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
    else:
        command = ctx.invoked_subcommand
        allowed = ['login', 'logout', 'status']
        if not auth.isLogged() and command not in allowed:
            click.echo(click.style("You need to login first.", fg="red"))
            exit(1)


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


@main.command(help="Ban user from booking/taking meals for the given period of time")
@click.option('--user', '-u', help='Username to ban')
def ban(user):
    click.echo("Banning "+user)


if __name__ == '__main__':
    main()
