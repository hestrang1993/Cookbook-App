from tkinter import Tk, filedialog


class DirSelector(Tk):
    
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


if __name__ == '__main__':
    input_selector_title = "Select Input Directory"
    input_dir_selector = DirSelector(title=input_selector_title)
    input_dir = input_dir_selector.dir_path
    print(input_dir)