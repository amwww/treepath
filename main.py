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

