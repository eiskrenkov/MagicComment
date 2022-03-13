import sublime
import sublime_plugin

from .lib.comment_settings import CommentSettings
from .lib.view_verifier import ViewVerifier

class MagicCommentInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("MagicComment.sublime-settings")

        for raw_comment_settings in settings.get("comments", []):
            comment_settings = CommentSettings(raw_comment_settings)
            view_verifier = ViewVerifier(self.view, comment_settings)

            if view_verifier.should_run():
                self.view.insert(edit, comment_settings.line(), comment_settings.text())
