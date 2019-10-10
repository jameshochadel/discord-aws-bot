# Discord AWS Bot for Minecraft

## Purpose

I host a Minecraft server on AWS that a number of friends use. We keep the server off when it's not in use. This keeps the AWS bill low, but means that everyone needs a way to turn the EC2 instance off and on, ideally without knowing how to use the AWS console or CLI. This bot provides lets anyone in a discord channel the ability to do that.

## Usage

From within Discord, issue commands to the bot using the `/mc` prefix:

```
<you> /mc hello
<bot> 🤖 Hello!
<you> /mc help
<bot> 💫 I am a bot for interacting with the Minecraft server! Try '/mc on'.
```

## Installation

### Prerequisites

The bot has the following prerequisites:

* The [AWS CLI](https://aws.amazon.com/cli/), authenticated with a user account
* Python 3.7.2

TODO: Describe the process of creating an AWS service account and enumerate the minimum permissions required to control the EC2 instance's state

### Discord and AWS Accounts

The bot requires the following environment variables to be set:

* `DISCORD_TOKEN`: A token provided by Discord that allows the bot to log into your Discord server and read/post messages.
* `EC2_INSTANCE_ID`: The ID of the EC2 instance to manage.

TODO: Describe the process of getting a Discord token

### Install and Run

With Python installed, run the following from the repo:

```sh
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python main.py

# Bot running...

# When done, quit with ^C and:
deactivate  # Deactivate the virtual environment.
```

## Development

This bot is developed against Python 3.7.2 on macOS and intended for use on Linux. I use [pyenv](https://github.com/pyenv/pyenv) to manage my Python versions locally.

If you add a dependency to the project, add it to `requirements-prefreeze.txt` and run the following (with the `venv` activated):

```sh
pip freeze > requirements.txt
```

This works around pip's flattening of the requirements tree by preserving the top-level dependencies.
