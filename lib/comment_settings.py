from .errors import CommentMisconfigError

class CommentSettings:
    def __init__(self, settings):
        self.settings = settings

    def text(self):
        text = self.settings.get("text")

        if not text:
            raise CommentMisconfigError("Text")

        return text + "\n"

    def line(self):
        return self.settings.get("line", 0)

    def blank_lines(self):
        return self.settings.get("blank_lines", 0)

    def included(self):
        return self.__files_settings().get("include", [])

    def excluded(self):
        return self.__files_settings().get("exclude", [])

    def __files_settings(self):
        return self.settings.get("files", {})
