"""
This type stub file was generated by pyright.
"""

import os

class abstract_filesystem:
    def __init__(self) -> None:
        ...
    
    def current_directory(self): # -> None:
        """Return a string representing the current directory."""
        ...
    
    def listdir(self, path, long=...): # -> None:
        """Return a listing of the directory at 'path' The empty string
        indicates the current directory.  If 'long' is set, instead
        return a list of (name, stat_info) tuples
        """
        ...
    
    def open(self, path, mode): # -> None:
        """Return an open file object"""
        ...
    
    def stat(self, path): # -> None:
        """Return the equivalent of os.stat() on the given path."""
        ...
    
    def isdir(self, path): # -> None:
        """Does the path represent a directory?"""
        ...
    
    def isfile(self, path): # -> None:
        """Does the path represent a plain file?"""
        ...
    
    def cwd(self, path): # -> None:
        """Change the working directory."""
        ...
    
    def cdup(self): # -> None:
        """Change to the parent of the current directory."""
        ...
    
    def longify(self, path): # -> None:
        """Return a 'long' representation of the filename
        [for the output of the LIST command]"""
        ...
    


def safe_stat(path): # -> tuple[Unknown, stat_result] | None:
    ...

class os_filesystem:
    path_module = os.path
    do_globbing = ...
    def __init__(self, root, wd=...) -> None:
        ...
    
    def current_directory(self): # -> Unknown | str:
        ...
    
    def isfile(self, path): # -> bool:
        ...
    
    def isdir(self, path): # -> bool:
        ...
    
    def cwd(self, path): # -> Literal[0, 1]:
        ...
    
    def cdup(self): # -> Literal[0, 1]:
        ...
    
    def listdir(self, path, long=...): # -> list_producer:
        ...
    
    def stat(self, path): # -> stat_result:
        ...
    
    def open(self, path, mode): # -> TextIOWrapper:
        ...
    
    def unlink(self, path): # -> None:
        ...
    
    def mkdir(self, path): # -> None:
        ...
    
    def rmdir(self, path): # -> None:
        ...
    
    def rename(self, src, dst): # -> None:
        ...
    
    def normalize(self, path): # -> str:
        ...
    
    def translate(self, path): # -> str:
        ...
    
    def longify(self, path_stat_info_tuple): # -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    


if os.name == 'posix':
    class unix_filesystem(os_filesystem):
        ...
    
    
    class schizophrenic_unix_filesystem(os_filesystem):
        PROCESS_UID = ...
        PROCESS_EUID = ...
        PROCESS_GID = ...
        PROCESS_EGID = ...
        def __init__(self, root, wd=..., persona=...) -> None:
            ...
        
        def become_persona(self): # -> None:
            ...
        
        def become_nobody(self): # -> None:
            ...
        
        def cwd(self, path): # -> Literal[0, 1]:
            ...
        
        def cdup(self): # -> Literal[0, 1]:
            ...
        
        def open(self, filename, mode): # -> TextIOWrapper:
            ...
        
        def listdir(self, path, long=...): # -> list_producer:
            ...
        
    
    
class msdos_filesystem(os_filesystem):
    def longify(self, path_stat_info_tuple): # -> str:
        ...
    


class merged_filesystem:
    def __init__(self, *fsys) -> None:
        ...
    


def msdos_longify(file, stat_info): # -> str:
    ...

def msdos_date(t): # -> str:
    ...

months = ...
mode_table = ...
def unix_longify(file, stat_info): # -> str:
    ...

def ls_date(now, t): # -> str:
    ...

class list_producer:
    def __init__(self, list, func=...) -> None:
        ...
    
    def more(self): # -> str:
        ...
