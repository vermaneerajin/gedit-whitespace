from gettext import gettext as _
from gi.repository import GObject, Gtk, Gedit

# Add tool option in menu
ui_str = """<ui>
  <menubar name="MenuBar">
    <menu name="ToolsMenu" action="Tools">
      <placeholder name="ToolsOps_2">
        <menuitem name="Whitespace" action="gedit-whitespace"/>
      </placeholder>
    </menu>
  </menubar>
</ui>
"""

class WhitespaceWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "WhitespaceWindowActivatable"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        # Insert menu items
        self._insert_menu()

    def do_deactivate(self):
        # Remove any installed menu items
        self._remove_menu()

        self._action_group = None

    def do_update_state(self):
        self._action_group.set_sensitive(self.window.get_active_document() != None)
        
    def _insert_menu(self):
        # Get the Gtk.UIManager
        manager = self.window.get_ui_manager()

        # Create a new action group
        self._action_group = Gtk.ActionGroup("WhitespacePluginActions")
        self._action_group.add_actions([("gedit-whitespace", None, _("Clear whitespace"),
                                         None, _("Clear whitespace from the document"),
                                         self.on_clear_document_activate)])

        # Insert the action group
        manager.insert_action_group(self._action_group, -1)

        # Merge the UI
        self._ui_id = manager.add_ui_from_string(ui_str)

    def _remove_menu(self):
        # Get the Gtk.UIManager
        manager = self.window.get_ui_manager()

        # Remove the ui
        manager.remove_ui(self._ui_id)

        # Remove the action group
        manager.remove_action_group(self._action_group)

        # Make sure the manager updates
        manager.ensure_update()
        
    # Menu activate handlers
    def on_clear_whitespace_activate(self, action):
        doc = self.window.get_active_document()
        if not doc:
            return

        doc.set_text('')
        
class WhitespaceViewActivatable(GObject.Object, Gedit.ViewActivatable):
    __gtype_name__ = "WhitespaceViewActivatable"

    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        print("Plugin created for", self.view)

    def do_deactivate(self):
        print("Plugin stopped for", self.view)

    def do_update_state(self):
        # Called whenever the view has been updated
        print("Plugin update for", self.view)
