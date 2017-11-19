from gi.repository import GObject, Gedit

class WhitespaceWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "WhitespaceWindowActivatable"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        print("Plugin created for", self.window)

    def do_deactivate(self):
        print("Plugin stopped for", self.window)

    def do_update_state(self):
        # Called whenever the window has been updated (active tab
        # changed, etc.)
        print("Plugin update for", self.window)
        
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
