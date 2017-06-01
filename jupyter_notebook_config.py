# Configuration file for jupyter-notebook.

#------------------------------------------------------------------------------
# NotebookApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## The IP address the notebook server will listen on.
c.NotebookApp.ip = '*'

## The port the notebook server will listen on.
c.NotebookApp.port = 8888

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
c.NotebookApp.open_browser = False

## Whether to allow the user to run the notebook as root.
c.NotebookApp.allow_root = True
