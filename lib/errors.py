import sublime

class Error(Exception):
    def __init__(self, message):
        super().__init__(message)
        sublime.error_message(message)

class CommentMisconfigError(Error):
    def __init__(self, attribute):
        super().__init__(f"{attribute} attribute is misconfigured for the comment")
