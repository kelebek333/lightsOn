#!/usr/bin/python
# -*- coding: UTF-8 -*-
import gettext
from gettext import ngettext
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("lights-on", "preferences-desktop-screensaver-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

# i18n
gettext.install("lights-on", "/opt/lights-on/locale", names="ngettext")

def menu():
  menu = gtk.Menu()
  
  command_one = gtk.MenuItem(_("Start"))
  command_one.connect('activate', run)
  menu.append(command_one)

  command_two = gtk.MenuItem(_("Stop"))
  command_two.connect('activate', stop)
  menu.append(command_two)

  exittray = gtk.MenuItem(_("Exit"))
  exittray.connect('activate', quit)
  menu.append(exittray)

  exittrayclose = gtk.MenuItem(_("Stop and Exit"))
  exittrayclose.connect('activate', quitstop)
  menu.append(exittrayclose)
  
  menu.show_all()
  return menu
  
def run(_):
  os.system("(/opt/lights-on/start &)")

def stop(_):
  os.system("(/opt/lights-on/stop &)")

def quitstop(_):
  os.system("pkill lightsOn.sh")
  gtk.main_quit()

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()
