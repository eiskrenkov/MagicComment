import sublime
import sublime_plugin

from .lib import comment_settings
from .lib import view_verifier

class MagicCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("MagicComment.sublime-settings")

        for object in settings.get("comments", []):
            comment_settings = CommentSettings(object)

            if ViewVerifier(self.view, comment_settings).should_run():
                self.view.insert(edit, comment_settings.line(), comment_settings.text())
