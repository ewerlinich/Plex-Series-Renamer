import argparse
import os

def vPrint(message) :
    """
    Prints certain messages only if the verbose flag has been set.

    Args:
        message (str): The text to be printed.
    """
    if(verbose) :
        print(message)


def renameSeason(dir, name, season) :
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
    vPrint(f'Entering {dir}')
    counter = 0
    season_str = str(season)
    
    for count, f in enumerate(sorted(os.listdir())) :
        f_name, f_ext = os.path.splitext(f)
        count_str = str(count + 1)

        f_name = f'{name}'
        if not (year is None) :
            f_name = f'{f_name} ({year})'

        if(season > 9) :
            if((count + 1) > 99) :
                f_name = f'{f_name} - S{season_str}E{count_str}'
            elif((count + 1) > 9) :
                f_name = f'{f_name} - S{season_str}E0{count_str}'
            else :
                f_name = f'{f_name} - S{season_str}E00{count_str}'
        else :
            if((count + 1) > 99) :
                f_name = f'{f_name} - S0{season_str}E{count_str}'
            if((count + 1) > 9) :
                f_name = f'{f_name} - S0{season_str}E0{count_str}'
            else :
                f_name = f'{f_name} - S0{season_str}E00{count_str}'
                
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
        counter += 1
            
    return counter
    
def renameShow(dir, name) :
    """
    Rename every season for a particular TV show at once, including all of the
    episodes within their respective seasons.

    Args:
        dir (str): The file directory that the seasons are contained in.
        name (str): The name of the TV show.

    Returns:
        tuple (int, int): The total amount of seasons and episodes over the whole show.
    """
    vPrint(f'Renaming a full show.')
    os.chdir(dir)
    vPrint(f'Changing directory to {directory}')

    ep_num_one = 1
    ep_num_two = 0
    count_str = 0

    # f is the current file/folder name
    for count, f in enumerate(sorted(os.listdir())) :
        count_str = str(count + 1)
        if(f == "Specials" or f == "specials") :  
            print("Skipping Specials folder.")
            count -= 1
            continue

        if(opsys == 'nt') :
            new_dir = directory + "\\" + f
        else :
            new_dir = directory + "/" + f

        ep_num_two += renameSeason(new_dir, show_name, count + 1)
        vPrint(f'Finished renaming current season.')
        ep_num_one_str = str(ep_num_one)
        ep_num_two_str = str(ep_num_two)
        os.chdir(directory)
        vPrint(f'Returning to {dir}')    
        
        new_name = ""
        if((count + 1) > 9) :
            new_name = f'Season {count_str}'
        else :
            new_name = f'Season 0{count_str}'

        if(absolute) :
            new_name = f'{new_name} (Episodes '
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
        vPrint(f'Renaming {f} to {new_name}')
        
        ep_num_one = ep_num_two + 1

    return (count_str, ep_num_two)

# 'nt' if Windows, 'posix' if Linux or OSX. Needed to determine
# forward vs backward slashes in directory names
opsys = os.name

all_args = argparse.ArgumentParser()
all_args.add_argument("directory", help="The directory containing the seasons/episodes to be renamed")
all_args.add_argument("name", help="The name of the TV show")
all_args.add_argument("season", type=int, help="The season number. Pass 0 to rename a full series instead of a single season")
all_args.add_argument("-v", "--verbose", help="Use this to display more information", action="store_true")
all_args.add_argument("-a", "--absolute", help="Add absolute (cumulative) episode counts in the folder name for the seasons", action="store_true")
all_args.add_argument("-y", "--year", type=int, help="Include the given year in the folder names for the seasons")
args = vars(all_args.parse_args())

verbose =       args["verbose"]
directory =     args["directory"]
show_name =     args["name"]
season_num =    args["season"]
absolute =      args["absolute"]
year =          args["year"]
vPrint(f'Program set to verbose mode.')
vPrint(f'Directory: {directory}')
vPrint(f'Name: {show_name}')
vPrint(f'Release year: {year}')
vPrint(f'Season number: {season_num}')
vPrint(f'Absolute numbering: {absolute}')

counts = (0, 0)
if(season_num == 0) :
    counts = renameShow(directory, show_name)
else :
    epcount = renameSeason(directory, show_name, season_num)
    counts = (1, epcount)
print(f'Done. Renamed {str(counts[0])} seasons containing {str(counts[1])} episodes.')
