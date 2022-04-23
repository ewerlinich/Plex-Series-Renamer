# Plex-Series-Renamer
A simple and lightweight cross-platform script made to help you organize your plex TV library. It dynamically renames the seasons and episode of a given TV series based on [Plex's recommended naming conventions.](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/)

## Installation
Only requires python installed on the host machine. Simply download the python file in this repository and run in terminal/command line/PowerShell.

## Usage

```
plex_tv_renamer.py [-h] [-v] [-a] [-y YEAR] directory name season
```

Directory is the location of the content. This can be either a single season or a full show. For example, "C:\Plex\TV\Game of Thrones" on Windows or "/home/user/Plex/TV/Game of Thrones" on Linux.

Name is the name of the show. For example, "Game of Thrones".

Season is a number representing the season of the show. Pass 0 to rename a full series instead of a single season.