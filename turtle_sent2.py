class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message(self.message_id, message_body, sender, 0)

        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=None):
        """
        The function receives username and n - the number of messages he wants to read.
        The function will return the first n messages in the user's inbox, if n not been forwarded,
        return all messages in the user's inbox.
        The messages will be marked as read and will not be returned to the user on the next call.
        :param str username: The username that want to read message.
        :param int n: The number of messages username wants to read.
        :return: List of - the first n messages in the user's inbox or all messages in the user's inbox.
        :rtype: list
        :raises KeyError: if the username does not exist and
        if the value of n is greater than the number of messages of username.
        """
        read_messages = []
        user_box = self.boxes[username]

        if n is not None:
            for message in user_box[0:n]:
                if not message.message_body:
                    message.read = True
                    read_messages.append(message.message_body)
            return read_messages

        else:
            return [message.message_body for message in user_box]

    def search_inbox(self, username, wanted_string):
        """
        The function gets username and wanted_string and return list of all the messages
        that contain the wanted_string in their body.
        :param str username: The username that want to search a string in his inboxes.
        :param str wanted_string: The string that looking for in inboxes.
        :return: List of the body's messages that contain the wanted_string in their body.
        :rtype: list
        :raises KeyError: if the username does not exist.
        """
        return [message.message_body for message in self.boxes[username] if wanted_string in message.message_body]


class Message:
    """A Message class. Manages the user's message, can present the message.
        :ivar int message_id: Incremental id of the message.
        :ivar string message_body: The body of the message.
        :ivar string sender: The name of the sender.
        :ivar boolean read: Indicates whether the message was read or not.
        """
    def __init__(self, message_id, message_body, sender, read):
        self.message_id = message_id
        self.sender = sender
        self.message_body = message_body
        self.read = read

    def __str__(self):
        """
        The function styles the message and returns string.
        :return:
        """
        return f"""The message from {self.sender},\n{self.message_body}."""


if __name__ == "__main__":
    m = Message(0, "hello", "avihay", True)
    print(m)
