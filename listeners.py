import sublime
import sublime_plugin

class MagicCommentListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        sublime.active_window().run_command("magic_comment")
