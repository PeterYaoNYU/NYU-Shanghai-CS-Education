import copy
from re import L
from turtle import pos
from unicodedata import name

from matplotlib.pyplot import show
def show_team_driver(names, team_size):
    show_team(names, team_size, [], 0)

def show_team(names, team_size, result_list=[], position=0):
    """
    # Base case 1: we get enough person in the result_list.
    # Base case 2: we have checked all the players.
    
    # Create two branches
    # Branch 1 add current person to result_list
    # Branch 2 does not add current person to result_list(copy)
    # Move on to the next person

    :param names: List[String] -- list of players
    :param team_size: Int -- choose how many players
    :param result_list: List[String] -- Additional list parameter for recursion
    :param position: Int -- Additional index parameter for recursion

    :return: Nothing to return
    :print: All the combinations players
    """
    if team_size==0:
        for i in result_list:
            print(i)
        return 
    if position==len(names):
        return 
    position+=1
    show_team(names, team_size, result_list, position)
    temp=copy.deepcopy(result_list)
    n=len(temp)
    if n==0:
        temp=[[names[position-1]]]
    else:
        for i in range(n):
            temp[i].append(names[position-1])
    team_size-=1
    show_team(names, team_size, temp, position)
    
players = ["Dey", "Ruowen", "Josh", "Kinder", "Mario", "Rock", "LOL"]
show_team_driver(players, 4)