from discord import file
from helpers.emoji_management import Emoji
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--name', help="Name of the emoji", required=True)
parser.add_argument('-a', '--alt', help="Alternate name of the emoji", required=True)
parser.add_argument('-d', '--desc', help="Description of the emoji", required=True)
parser.add_argument('-f', '--file', help="Emoji Filepath", required=True)

args = parser.parse_args()

emoji = Emoji(json_path="emojis.json")

emoji.add_emoji(name=args.name, alt=args.alt, file_path=args.file, description=args.desc)