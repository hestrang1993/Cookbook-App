# -*- coding: utf-8 -*-
"""
The :module:`dir_selector` module stores the :class:`DirSelector` class.
"""
import os
from tkinter import Tk, filedialog


class DirSelector(Tk):
    """
    The :class:`DirSelector` extends :class:`Tk` to make selecting a directory easy.
    """
    
    def __init__(self, title, topmost=True):
        """
        Create a new :class:`DirSelector` instance.
        
        Parameters
        ----------
        title : str
            The title of the directory selection window.
        topmost : bool
            Whether the directory selection window will be the topmost window or not. 
        """
        super().__init__()
        self.withdraw()
        self.topmost = topmost
        self.attributes('-topmost', self.topmost)
        self.title = title
        self._initial_dir = os.path.dirname(os.path.abspath(__file__))
        self._dir_path = filedialog.askdirectory(title=self.title, initialdir=self.initial_dir)
    
    @property
    def dir_path(self):
        """
        str: The filepath to the selected directory.
        """
        return self._dir_path
    
    @property
    def initial_dir(self):
        """
        str: The directory the window will start on.
        """
        return self._initial_dir
