import sublime

class Error(Exception):
    def __init__(self, message):
        super().__init__(message)
        sublime.error_message(message)

class CommentMisconfigError(Error):
    def __init__(self, attribute, explanation):
        super().__init__(f"Comment is misconfigured! {attribute} {explanation}")
