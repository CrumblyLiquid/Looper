import discord
from discord.ext import commands, tasks

class Looper(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.index = 0

    @tasks.loop(seconds=3)
    async def tasker(self, spec):
        print(f'{self.index}: {spec}')
        self.index += 1

    @commands.command()
    async def ton(self, ctx, arg):
        if self.tasker.is_running():
            self.tasker.stop()
        else:
            self.tasker.start(spec=arg)

def setup(client):
    client.add_cog(Looper(client))