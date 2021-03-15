"""
This module implements the main functionality of py-files.
Author: Mateo Hurtado
URL = https://teodev1611.github.io
"""

__author__ = "Mateo Hurtado, TeoDev1611"
__email__ = "teodev1611@gmail.com"
__status__ = "planning"

import os
import glob
import shutil


class FilePropierties():
    """
    Rename the file, File Dir,Delete the file
    """

    def __init__(self) -> None:
        pass

    def FileDir(self):
        """FileDir

        Returns:
            string: return the current dir
        """
        return os.getcwd()

    def RenameFile(self, fileToRename, newName):
        """RenameFile

        Args:
            fileToRename (string): Directory of File to Rename
            newName (string): Directory an New Name of the file

        Returns:
            bool: [True if rename succesfuly and false if not succesfuly]
        """
        try:
            os.rename(fileToRename, newName)
            status = True
            return status
        except Exception as err:
            status = False
            return status + err

    def DeleteFile(self, fileToDelete):
        """Delete File

        Args:
            fileToDelete (string): Name of the file to rename

        Returns:
            bool: True if no have error False if have errors and error
        """
        try:
            os.remove(fileToDelete)
            status = True
            return status
        except Exception as err:
            status = False
            return status + err

    def ClasifyFilesWithExtensions(self, fileDir, extToSearch):
        """Clasify Files

        Args:
            fileDir (string): Directory where search
            extToSearch (string): Extension to search

        Returns:
            String: Return the files if not have error
        """
        try:
            os.chdir(fileDir)
            for i in glob.glob(extToSearch):
                return i
        except Exception as err:
            return f"Error: {err}"


# MOVE OPERATIONS


class FileMoveOperations():
    def __init__(self) -> None:
        pass

    def copyFile(self, fileRoute, distFile):
        """copyFile

        Args:
            fileRoute (string): Actually Route
            distFile (string): New Route

        Returns:
            bool: Return True
        """
        try:
            shutil.copy(fileRoute, distFile)
            return True
        except Exception as err:
            return False + err

    def moveFile(self, fileRoute, distFile):

        """moveFile

        Args:
            fileRoute (string): Actually Route
            distFile (string): New Route

        Returns:
            bool: Return a Bool if is succesfuly
        """

        try:
            shutil.move(fileRoute, distFile)
            return True
        except Exception as err:
            return False + err
