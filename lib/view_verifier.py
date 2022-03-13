class ViewVerifier:
    WILDCARD = "*"

    def __init__(self, view, settings):
        self.view = view
        self.settings = settings

    def should_run(self):
        return self.__file_supported() and not self.__comment_already_inserted()

    def __file_supported(self):
        file_name = self.view.file_name().split("/")[-1]

        if file_name is None:
            return False

        if self.__file_name_listed(file_name, self.settings.excluded()):
            return False

        return self.__file_name_listed(file_name, self.settings.included())

    def __file_name_listed(self, file_name, array):
        for element in array:
            if file_name == element or (element.startswith(self.WILDCARD) and file_name.endswith(element[1:])):
                return True

        return False

    def __comment_already_inserted(self):
        line = self.view.line(self.settings.line())
        line_contents = self.view.substr(line)

        return line_contents == self.settings.text().strip()
