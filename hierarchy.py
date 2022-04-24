class User:
    """
    Represent a user in our system. Gets the username, password and user_type (regular user or system administrator).
    """
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type
        self.files = []


class UserManagementSystem:
    """
    Represent the user management system. Holds a list of users.
    """
    def __init__(self):
        self.users = []


class File:
    """
    Represent a file in our system. Gets the file_name, username, weight of the file and its content.
    """
    def __init__(self, file_name, username, weight, content):
        self.file_name = file_name
        self.username = username
        self.weight = weight
        self.content = content

    def read(self, checked_username):
        """
        The function gets checked_username -  username that want to read a file.
        And return - if the user created the file or he is the system administrator, the contents of the file will be
        returned, else None.
        :param checked_username: username that want to read a file.
        :return: The content of file or None.
        """
        if checked_username == self.username or checked_username == "system administrator":
            return self.content

        else:
            return None


class Folder:
    """
    Represent a folder in our system. Gets the folder_name.
    """
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.files = []


class TextFile(File):
    """
    Represent a TextFile in our system. Gets the folder_name. An heir from the File class.
    """
    def count(self, wanted_string):
        """
        The function gets wanted_string and returns how many times the wanted_string appeared in the file content.
        :param wanted_string: The string that searched.
        :return: Integer of the times that wanted_string appeared in the file.
        """
        return (
            f"The {wanted_string} appears in file: {self.content.count(wanted_string)} times."
        )


class BinaryFile(File):
    """
    Represent a BinaryFile in our system. An heir from the File class.
    """
    def get_dimensions(self):
        """
        :return:The length and width of the image.
        """
        pass
