import os


class DirFileLister:

    def __init__(self):
        self._os_root = os.path.dirname(os.path.abspath(__file__))

    @property
    def os_root(self):
        return self._os_root

    def create_file_path_list(self, root_dir):
        """
        Parse through a specific directory.
        Then, create an absolute path string for every file in a directory (exclude subdirectories).
        Finally, return all these paths as a list.
    
        Parameters
        ----------
        root_dir : str
            The absolute path to the directory.
        Returns
        -------
        list:
            A list of all absolute filepaths for all files in a specific directory.
        """
        files = [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f))]
        files_list = []
        for file in files:
            file_path = os.path.join(self.os_root, root_dir, file)
            files_list.append(file_path)
        return files_list
