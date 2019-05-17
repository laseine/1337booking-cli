# 1337booking-cli
1337booking CLI tool

# Requirements
You need to have **python3** installed.

Running `python3 --version` should print something like:

`Python 3.7.2`

# Install
Run the following commands:

```sh
git clone https://github.com/mehdibo/1337booking-cli.git booking-cli
cd booking-cli
./install.sh
```
That's it, now you can run:

```sh
./run.sh
```
Or:

```sh
booking-cli
```

If you answered Yes to Installing *booking-cli* globally.

If you got something like this:

```sh
Usage: booking-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  ban     Ban user from booking/taking meals for the given period of time
  login   Login to your admin account
  logout  Logout from your account
  status  Print your current status
```
Then congrats! otherwise, open a new issue with the error.