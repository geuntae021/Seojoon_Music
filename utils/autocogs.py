import os

def AutoCogs(self):
    cogs = [i.replace(".py", "") for i in os.listdir('./cogs') if i.endswith('.py')]
    for i in cogs:
        self.load_extension(f'cogs.{i}')
        print(f'{i}.py on Ready.')