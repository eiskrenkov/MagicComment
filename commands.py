import sublime
import sublime_plugin

from .lib.comment_settings import CommentSettings
from .lib.view_verifier import ViewVerifier

class MagicCommentInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("MagicComment.sublime-settings")

        for raw_comment_settings in settings.get("comments", []):
            comment_settings = CommentSettings(raw_comment_settings)

            if ViewVerifier(self.view, comment_settings).should_run():
                self.__insert_comment(edit, comment_settings)

    def __insert_comment(self, edit, comment_settings):
        comment_text = comment_settings.text() + ("\n" * comment_settings.blank_lines())
        self.view.insert(edit, comment_settings.line(), comment_text)
