import sublime
import sublime_plugin

class MagicCommentListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        settings = sublime.load_settings("MagicComment.sublime-settings")

        if settings.get("run_on_save"):
            sublime.active_window().run_command("magic_comment_insert")
