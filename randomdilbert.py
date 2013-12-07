#!/usr/bin/env python
import pygtk
pygtk.require("2.0")
import gtk

import random
import urllib
import re

def pixbuf_from_url(url):
    image_data = urllib.urlopen(url)
    loader = gtk.gdk.PixbufLoader()
    loader.write(image_data.read())
    loader.close()
    return loader.get_pixbuf()

class RandomDilbert:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_default_size(670, 430)
        self.window.set_title("RandomDilbert Client by GKBRK")
        
        self.image = gtk.Image()
        self.show_random_image()
        
        self.random_button = gtk.Button("Random Image")
        self.random_button.connect("clicked", self.show_random_image)
        
        self.vbox = gtk.VBox()
        self.vbox.pack_start(self.image)
        self.vbox.pack_start(self.random_button)
        
        self.window.add(self.vbox)
        
        self.window.connect("destroy", self.destroy_window)
    
    def show(self):
        self.window.show_all()
        gtk.main()
    
    def destroy_window(self, widget=None, data=None):
        gtk.main_quit()
    
    def get_random_image(self):
        year = random.choice(["2011", "2012", "2013"])
        month = random.choice(range(1, 13))
        day = random.choice(range(29))
        url_to_dilbert_page = "http://www.dilbert.com/%s-%s-%s/" % (year, month, day)
        page_contents = urllib.urlopen(url_to_dilbert_page).read()
        image_url = re.search('<a href="/strips/comic/.*?/"><img onload=".*?" src="(.*?)" alt="The Official Dilbert Website featuring Scott Adams Dilbert strips, animations and more" border="0" /></a>', page_contents).group(1)
        image_url = "http://www.dilbert.com" + image_url
        #print image_url
        return image_url
    
    def show_random_image(self, widget=None, data=None):
        self.image.set_from_pixbuf(pixbuf_from_url(self.get_random_image()))

RandomDilbert().show()
