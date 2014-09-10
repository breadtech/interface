##
# title: breadinterface.py
# by: Aaron Philips, Brian Kim
# description: sets up the whole interface with nonfunctional inputs
#

import gtk

# app
w = gtk.Window()

# controller
frame = gtk.VBox()

# frame
top = gtk.HBox()
bottom = gtk.HBox()
tree = gtk.TreeView()

# button labels
tl_label = unichr(9776)     # menu
tm_label = "breadinterface" # title
tr_label = "i"				# info
bl_label = "_"				# remove
bm_label = "these buttons don't do anything"
br_label = "+"				# add

button_dict = {
  tl_label : "clicking the menu button opens a subframe of menu items",
  tm_label : "clicking the title button does not do anything",
  tr_label : "clicking the info button will display more information about this (nothing)",
  bl_label : "clicking the remove button will remove nothing",
  bm_label : "clicking the bottom middle button will do absolutely nothing",
  br_label : "clicking the add button will add nothing"
}

# bar
tl = gtk.Button(tl_label)
tm = gtk.Button(tm_label)
tr = gtk.Button(tr_label)
bl = gtk.Button(bl_label)
bm = gtk.Button(bm_label)
br = gtk.Button(br_label)

def init():
  w.set_size_request( 320, 480)
  w.connect("delete-event", gtk.main_quit)

  tl.set_size_request( 44, 44 )
  tr.set_size_request( 44, 44 )
  bl.set_size_request( 44, 44 )
  br.set_size_request( 44, 44 )

  top.pack_start(tl,False)
  top.pack_start(tm,True)
  top.pack_start(tr,False)

  bottom.pack_start(bl,False)
  bottom.pack_start(bm,True)
  bottom.pack_start(br,False)

  frame.pack_start(top,False)
  frame.pack_start(tree,True)
  frame.pack_start(bottom,False)

  w.add(frame)

def display_button_info( button, info ):
  message = gtk.MessageDialog(parent=w, 
                            flags=0, 
                            type=gtk.MESSAGE_QUESTION, 
                            buttons=gtk.BUTTONS_OK, 
                            message_format=None)
  message.set_markup( "" )

def start():
  w.show_all()
  gtk.main()

def main():
  init()
  start()

if __name__ == "__main__":
  main()