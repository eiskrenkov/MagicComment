import re

class ViewVerifier:
    FILE_EXTENSION_WILDCARD_REGEX = "\\A[*.].{1}\\w+$"

    def __init__(self, view, settings):
        self.view = view
        self.settings = settings

    def should_run(self):
        return self.__file_supported() and not self.__comment_already_inserted()

    def __file_supported(self):
        full_file_name = self.view.file_name()

        if full_file_name is None:
            return

        file_name = full_file_name.split("/")[-1]

        if self.__file_name_listed(file_name, self.settings.excluded()):
            return False

        return self.__file_name_listed(file_name, self.settings.included())

    def __file_name_listed(self, file_name, file_name_matchers):
        for file_name_matcher in file_name_matchers:
            if self.__file_name_matches(file_name, file_name_matcher):
                return True

        return False

    def __file_name_matches(self, file_name, file_name_matcher):
        if file_name == file_name_matcher:
            return True

        if not re.search(self.FILE_EXTENSION_WILDCARD_REGEX, file_name_matcher):
            return False

        return file_name.endswith(file_name_matcher[1:])

    def __comment_already_inserted(self):
        line = self.view.line(self.settings.line())
        line_contents = self.view.substr(line)

        return line_contents == self.settings.text().strip()
