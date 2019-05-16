#!/usr/bin/env python
import click, datetime, sys
from src import Auth, Api
from datetime import datetime


# TODO: login + logout + status

auth = Auth.Auth("http://localhost")
api = Api.Api("http://localhost", auth.getToken())

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
@click.option('--start', '-s', help='Start date (YYYY-MM-DD)', required=True)
@click.option('--end', '-e', help='End date (YYYY-MM-DD)', required=True)
@click.option('--stdin', help='Get users from stdin', is_flag=True)
@click.option('--format', help='Format for stdin, default is username per line.', type=click.Choice(['line']),
              default='line')
@click.pass_context
def ban(ctx, user, start, end, stdin, format):
    # Validate date format (same format as the `who` command)
    try:
        startdate = datetime.strptime(start.strip(), '%Y-%m-%d')
        enddate = datetime.strptime(end.strip(), '%Y-%m-%d')
    except ValueError:
        click.echo(click.style("Invalid date format", fg="red"))
        return
    if not stdin and user is None:
        click.echo(ctx.get_help())
        click.echo(click.style('Error: missing option "--user" / "-u".', fg="red"))
        return
    if stdin:
        for login in sys.stdin:
            login = login.strip()
            res = api.ban(login, startdate, enddate)
            if res['error'] is not None:
                click.echo(click.style(res['error'], fg="red"))
            else:
                click.echo(click.style("Banned " + login + " from " + start + " to " + end, fg="green"))
        return

    res = api.ban(user, startdate, enddate)
    if res['error'] is not None:
        click.echo(click.style(res['error'], fg="red"))
        return
    click.echo(click.style("Banned "+user+" from "+start+" to "+end, fg="green"))


if __name__ == '__main__':
    main()
