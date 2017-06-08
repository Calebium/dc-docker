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

#------------------------------------------------------------------------------
# FileContentsManager(FileManagerMixin,ContentsManager) configuration
#------------------------------------------------------------------------------

## Python callable or importstring thereof
#
#  to be called on the path of a file just saved.
#
#  This can be used to process the file on disk, such as converting the notebook
#  to a script or HTML via nbconvert.
#
#  It will be called as (all arguments passed by keyword)::
#
#      hook(os_path=os_path, model=model, contents_manager=instance)
#
#  - path: the filesystem path to the file just written - model: the model
#  representing the file - contents_manager: this ContentsManager instance

# The function script_post_save() is used for saving a Python script (for version
# control wth Git) whenever a Jupyter notebook is saved, and is lifted from:
#
#   https://github.com/jupyter/notebook/blob/master/docs/source/extending/savehooks.rst

import io
import os
from notebook.utils import to_api_path

_script_exporter = None

def script_post_save(model, os_path, contents_manager, **kwargs):
    """convert notebooks to Python script after save with nbconvert

    replaces `ipython notebook --script`
    """
    from nbconvert.exporters.script import ScriptExporter

    if model['type'] != 'notebook':
        return

    global _script_exporter

    if _script_exporter is None:
        _script_exporter = ScriptExporter(parent=contents_manager)

    log = contents_manager.log

    base, ext = os.path.splitext(os_path)
    py_fname = base + '.py'
    script, resources = _script_exporter.from_filename(os_path)
    script_fname = base + resources.get('output_extension', '.txt')
    log.info("Saving script /%s", to_api_path(script_fname, contents_manager.root_dir))

    with io.open(script_fname, 'w', encoding='utf-8') as f:
        f.write(script)

c.FileContentsManager.post_save_hook = script_post_save
