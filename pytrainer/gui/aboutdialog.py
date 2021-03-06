# -*- coding: utf-8 -*-

#Copyright (C) Fiz Vazquez vud1@sindominio.net
# Jakinbidea & Grupo Ikusnet Developer
# vud1@grupoikusnet.com
# Heavily modified by dgranda

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

from gi.repository import Gtk, GdkPixbuf

class About:
    def __init__(self,data_path = None, version = None):
        self.data_path = data_path
        self.version = version

    def run(self):
        authors = [
            "Fiz Vázquez <vud1@sindominio.net>",
            "David García Granda <dgranda@gmail.com>",
            "John Blance <john.blance@gmail.com>",
            "Arnd Zapletal <a.zapletal@gmail.com>",
            "Nathan Jones <nathan@ncjones.com>",
            "Arto Jantunen <viiru@iki.fi>",
        ]
        # Translators: See
        # https://developer.gnome.org/gtk3/stable/GtkAboutDialog.html#gtk-about-dialog-set-translator-credits
        # for details on how this is used.
        translator_credits = _("translator-credits")
        license = "pytrainer – The free sport tracking center\nCopyright © 2005-09 Fiz Vázquez\n\nThis program is free software; you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation; either version 2 of the License, or\n(at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program; if not, write to the Free Software\nFoundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"
        about_dialog = Gtk.AboutDialog()
        about_dialog.set_destroy_with_parent(True)
        about_dialog.set_name("pytrainer")
        about_dialog.set_version(self.version)
        about_dialog.set_copyright("Copyright © 2005-09 Fiz Vázquez")
        about_dialog.set_website("https://github.com/pytrainer/pytrainer")
        about_dialog.set_website_label("https://github.com/pytrainer/pytrainer")
        about_dialog.set_comments("The free sport tracking center")
        about_dialog.set_license(license)
        
        about_dialog.set_authors(authors)
        about_dialog.set_translator_credits(translator_credits)
        about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file(self.data_path+"glade/pytrainer_mini.png"))

        # callbacks for destroying the dialog
        def close(dialog, response, editor):
            editor.about_dialog = None
            dialog.destroy()
        def delete_event(dialog, event, editor):
            editor.about_dialog = None
            return True
        
        about_dialog.connect("response", close, self)
        about_dialog.connect("delete-event", delete_event, self)  
        self.about_dialog = about_dialog
        about_dialog.show()
        
    def present(self):
        if self.about_dialog is None:
            self.run()
        self.about_dialog.present()
