class CommentSettings:
    def __init__(self, settings):
        self.settings = settings

    def text(self):
        return self.settings.get("text")

    def line(self):
        return self.settings.get("line", 0)

    def included(self):
        return self.__files_settings().get("include", [])

    def excluded(self):
        return self.__files_settings().get("exclude", [])

    def __files_settings(self):
        return self.settings.get("files", {})
