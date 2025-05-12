import click
import asyncio
from robocore_api.client import RobotClient

@click.group()
def main():
    """RoboCore CLI"""
    pass

@main.command()
@click.argument('uri')
def info(uri):
    """Show sensor data."""
    click.echo(f"Connecting to {uri}…")
    client = RobotClient(uri)
    asyncio.run(client.connect())
    data = asyncio.run(client.read_sensors())
    click.echo(f"Sensors: {data}")
    asyncio.run(client.disconnect())

@main.command()
@click.argument('uri')
@click.argument('speed', type=float)
def forward(uri, speed):
    """Move forward at SPEED (m/s)."""
    click.echo(f"Moving {uri} forward at {speed} m/s…")
    client = RobotClient(uri)
    asyncio.run(client.connect())
    asyncio.run(client.move_forward(speed))
    click.echo("Done.")
    asyncio.run(client.disconnect())

if __name__ == "__main__":
    main()
