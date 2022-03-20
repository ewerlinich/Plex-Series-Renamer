import argparse
import enum
import os

def vPrint(message) :
    """
    Prints certain messages only if the verbose flag has been set.

    Args:
        message (str): The text to be printed.
    """
    if(verbose) :
        print(message)


def renameEpisodes(dir, name, season) :
    """
    Renames a season of a TV show following Plex's recommended naming conventions.

    Args:
        dir (str): The file directory that the season's files are contained in.
        name (str): The name of the TV show.
        season (int): The season number.

    Returns:
        int: The amount of episodes in the season. The return is not used if a single
             season is being renamed.
    """
    os.chdir(dir)
    vPrint(f'Changing directory to {dir}')
    counter = 0
    season_str = str(season)
    
    for count, f in enumerate(os.listdir()) :
        f_name, f_ext = os.path.splitext(f)
        count_str = str(count + 1)
        if(season > 9) :
            if((count + 1) > 99) :
                f_name = f'{name} - S{season_str}E{count_str}'
            elif((count + 1) > 9) :
                f_name = f'{name} - S{season_str}E0{count_str}'
            else :
                f_name = f'{name} - S{season_str}E00{count_str}'
        else :
            if((count + 1) > 99) :
                f_name = f'{name} - S0{season_str}E{count_str}'
            if((count + 1) > 9) :
                f_name = f'{name} - S0{season_str}E0{count_str}'
            else :
                f_name = f'{name} - S0{season_str}E00{count_str}'
                
            new_name = f'{f_name}{f_ext}'
            os.rename(f, new_name)
            counter += 1
            
    return counter
    
def renameSeason(dir, name) :
    """
    Rename a set of seasons for a particular TV show, including all of the episodes
    within their respective seasons.

    Args:
        dir (str): The file directory that the seasons are contained in.
        name (str): The name of the TV show.
    """
    vPrint(f'Renaming a set of seasons.')
    os.chdir(dir)
    vPrint(f'Changing directory to {directory}')
    ep_num_one = 1
    ep_num_two = 0
    for count, f in enumerate(os.listdir()) :
        count_str = str(count + 1)
        if(f == "Specials" or f == "specials") :
            print("Skipping Specials folder.")
            count -= 1
            continue
        new_dir = directory + "\\" + f
        ep_num_two += renameEpisodes(new_dir, show_name, count + 1)
        vPrint(f'Finished renaming current season.')
        ep_num_one_str = str(ep_num_one)
        ep_num_two_str = str(ep_num_two)
        os.chdir(directory)
        vPrint(f'Changing directory to {dir}')    
        
        new_name = ""
        if((count + 1) > 9) :
            new_name = f'{name} - Season {count_str} (Episodes '
        else :
            new_name = f'{name} - Season 0{count_str} (Episodes '
            
        if(ep_num_one > 99) :
            new_name = f'{new_name}{ep_num_one_str}-'
        elif(ep_num_one > 9) :
            new_name = f'{new_name}0{ep_num_one_str}-'
        else :
            new_name = f'{new_name}00{ep_num_one_str}-'
            
        if(ep_num_two > 99) :
            new_name = f'{new_name}{ep_num_two_str})'
        elif(ep_num_two > 9) :
            new_name = f'{new_name}0{ep_num_two_str})'
        else :
            new_name = f'{new_name}00{ep_num_two_str})'
        os.rename(f, new_name)
        vPrint(f'Changing {f} to {new_name}')
        
        ep_num_one = ep_num_two + 1

all_args = argparse.ArgumentParser()
all_args.add_argument("directory", help="The directory containing the seasons/episodes to be renamed")
all_args.add_argument("name", help="The name of the TV show")
all_args.add_argument("season", type=int, help="The season number. Pass 0 to rename a collection of seasons instead of a single one")
all_args.add_argument("-v", "--verbose", help="Use this to display more information", action="store_true")
args = vars(all_args.parse_args())

verbose = args["verbose"]
directory = args["directory"]
show_name = args["name"]
season_num = args["season"]
vPrint(f'Program set to verbose mode.')
vPrint(f'Directory: {directory}')
vPrint(f'Name: {show_name}')
vPrint(f'Season number: {season_num}')

if(season_num == 0) :
    renameSeason(directory, show_name)
    print(f'All done!')
else :
    renameEpisodes(directory, show_name, season_num)
    print(f'All done!')

