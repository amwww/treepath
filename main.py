# Imports
from treelib import Tree

# Structs
"""
Tree:
main = Path('prompt', {'outcome':Path()}, 'err_branch_non_existent', 'err_branch_outcome_none')
Errors:
'err_branch_non_existent', 'err_branch_outcome_none' (dict)
"""

# Classes
class Path:
    """A Path in a Tree, recursive."""
    def __init__(self, prompt:str, outcomes:dict, onactive:str, errors:dict={'err_branch_not_found':'That wasn\'t one of the options.'}) -> None:
        outcomes:dict[str,Path] = outcomes
        self.prompt = prompt
        self.outcomes = outcomes
        self.errors = errors
        self.onactive = onactive

    def add_outcome(self, outcomename:str, prompt:str, outcomes:list, onactive:str='', errors:dict={'err_branch_not_found':'That wasn\'t one of the options.'}):
        if type(outcomes) == Path:
            path = Path(outcomes.prompt, outcomes.outcomes, onactive, outcomes.errors)#outcomes
        else:
            path = Path(prompt, {outcome:'' for outcome in outcomes}, onactive, errors)
        self.outcomes[outcomename] = path
        return path

    def get_outcomes(self, delimiter:str=" | ") -> str:
        return delimiter.join(list(self.outcomes.keys()))
    
    def list_outcomes(self) -> list:
        return list(self.outcomes.keys())

    def get_branch_not_found(self) -> str:
        return self.errors['err_branch_not_found']

class Tree:
    def __init__(self) -> None:
        self.main = None
        self.currentbranch  = self.main
        print('BranchLib -> __init__')

    def getinput(self) -> Path:
        path = self.currentbranch
        print(path.prompt)
        print(path.get_outcomes())
        branchname = input()    
        try:
            branch = path.outcomes[branchname]
            return branch
        except KeyError as f:
            try:
                branch = path.outcomes[path.list_outcomes()[int(branchname)]]
                return branch
            except IndexError as e:
                print(path.get_branch_not_found(), e)
                pass
            except TypeError as e:
                print(path.get_branch_not_found(), e)
                pass
            except ValueError as e:
                print(path.get_branch_not_found(), e)
                pass
            self.getinput()

    def step(self) -> None: 
        branch = self.getinput()
        self.currentbranch = branch
        print(branch.onactive)
        if type(branch.outcomes) == Path:
            self.currentbranch = branch.outcomes

    def add_main(self, *, prompt:str, outcomes:list, errors:dict={'err_branch_not_found':'That wasn\'t one of the options.'}) -> Path:
        if self.main == None:
            self.main = Path(prompt, {outcome:'' for outcome in outcomes}, '', errors)
            self.currentbranch = self.main
        else:
            raise KeyError('Main Branch already created.')

main = Tree()

main.add_main(prompt='Hello and Welcome to your adventure! What would you like to do?', outcomes=['Take a bath', 'Go outside', 'Touch grass'])
main.main.add_outcome('Take a bath', 'result', main.main, 'You took a bath. Why would you wanna be cleaner?')
main.main.add_outcome('Touch grass', 'result', main.main, 'You touched grass. Your immune cells didn\'t know what it is and formed an alergic reaction.\nYou died.')
main.main.add_outcome('Go outside', 'What would you like to do now?', ['Go back inside', 'Stare at the sun', 'Cross the road', 'Stay outside', 'Talk to the neighbour', 'Sit and chill'], 'You went outside to enjoy some fresh air.')

main.main.outcomes['Go outside'].add_outcome('Go back inside', 'You walk inside your house. What\'s next?', ['Go back to your room', 'Lock the door', 'Go outside again'], 'You went back inside.')
main.main.outcomes['Go outside'].outcomes['Go back inside'].add_outcome('Go back to your room', 'result', main.main, 'You went back into your room.')
main.main.outcomes['Go outside'].outcomes['Go back inside'].add_outcome('Lock the door', 'result', main.main, 'You realise you didn\'t lock the door this whole time. You lock the door, and go back to your room.')
main.main.outcomes['Go outside'].outcomes['Go back inside'].add_outcome('Go outside again', 'result', main.main.outcomes['Go outside'], 'You go back outside.')

main.main.outcomes['Go outside'].add_outcome('Stare at the sun', 'result', main.main, 'You look at the sun considering your life choices. As the sun burns your eyes, you realise how worthless you are to make this desicion. You died.')

main.main.outcomes['Go outside'].add_outcome('Cross the road', 'result', main.main, 'Your neighbour watches you cross the road. He watches as he screams at you, "FOR THE SIX MILIIONTH NINE HUNDRED FOUR HUNDRED AND SENVENTY THIRD TIME, THERES NO OTHER SIDE OF THE ROAD. ITS A CLIFF, STEVE." You died of fall damage.')


while True: 
    main.step()