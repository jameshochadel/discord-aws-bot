import boto3
import discord
import os

from botocore.exceptions import ClientError

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/mc hello"):
        await message.channel.send("🤖 Hello!")

    if message.content.startswith("/mc help"):
        await message.channel.send("💫 I am a bot for interacting with the Minecraft server! Try '/mc on'.")

    if message.content.startswith("/mc on"):
        await message.channel.send("🚀 Under way, captain")
        response = instance_on()
        await message.channel.send(response)

    if message.content.startswith("/mc off"):
        response = instance_off()
        await message.channel.send(response)


def _get_instance():
    instance_id = os.environ["EC2_INSTANCE_ID"]

    ec2 = boto3.resource("ec2")
    instance = ec2.Instance(instance_id)

    return instance


def instance_off() -> str:
    instance = _get_instance()
    state = instance.state["Name"]

    if state == "stopped":
        return "😵 Server is already off!"
    else:
        result = instance.stop(DryRun=dry_run)
        return f"😴 Turned off server. Good night!"


def instance_on() -> str:
    """Attempt to turn on the Minecraft server.
    """
    instance = _get_instance()

    state = instance.state["Name"]
    if state == "running":
        return "✅ Server is already running!"
    elif state == "stopped":
        instance.start()
        return "🏃‍♂️ Server is starting up!"
    else:
        return "🛑 Server was not started. Instance status must be 'stopped';"\
        f" instead, was {state}"


if __name__ == "__main__":
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        print("Environment variable DISCORD_TOKEN was not set.")

    client.run(token)
