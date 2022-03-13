from .errors import CommentMisconfigError

class CommentSettings:
    def __init__(self, settings):
        self.settings = settings

    def text(self):
        text = self.settings.get("text")

        if not text:
            raise CommentMisconfigError("Text", "must be filled")

        return text + "\n"

    def line(self):
        line = self.settings.get("line", 1)

        if line < 1:
            raise CommentMisconfigError("Line", "should be greater than or equal to 1")

        return line

    def blank_lines(self):
        return self.settings.get("blank_lines", 0)

    def included(self):
        return self.__files_settings().get("include", [])

    def excluded(self):
        return self.__files_settings().get("exclude", [])

    def __files_settings(self):
        return self.settings.get("files", {})
