# e.cloudmesh.shell.1 cmd5 comes with cms install
# e.cloudmesh.shell.2 folder has been uploaded to github
# e.cloudmesh.shell.3 working
from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class ChenxuCommand(PluginCOmmand):

    @command
    def do_chenxu(self, args, arguments):
        """
          ::
           Usage:
                 chenxu -f FILE
                 chenxu list
           This command does some useful things.
           Arguments:
              File     a file name
           Options:
                 -f    specify the file
        """

        print(arguments)
        if arguments.FILE:
            print("You have used file: ", arguments.FILE)
        return ""
