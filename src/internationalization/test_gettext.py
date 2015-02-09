#-*- coding: MS949 -*-
import gettext

# Set up message catalog access
t = gettext.translation('gettext_example', 'locale', fallback=True)
_ = t.ugettext

print _('This message is in the script.')