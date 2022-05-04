"""
The :module:`dir_selector` module stores the :class:`DirSelector` class.
"""

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
        self._dir_path = filedialog.askdirectory(title=self.title)
    
    def dir_path(self):
        """
        str: The filepath to the selected directory.
        """
        return self._dir_path
