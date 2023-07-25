import subprocess

def open_app(app_name):
  """Opens the specified Windows app."""

  if app_name == 'notepad':
    subprocess.Popen(['notepad.exe'])
  elif app_name == 'edge':
    app_id = 'Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge'
    subprocess.Popen(['start', app_id])
  else:
    print('The app name is not recognized.')

if __name__ == '__main__':
  open_app('open  notepad')
  open_app('edge')
