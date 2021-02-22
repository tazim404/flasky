import click
import os
import sys
import subprocess


def current_dir():
    '''It return the current working directory'''
    current_working_directory = os.getcwd()
    return current_working_directory


def create_file(filename_or_filepath, content):
    with open(filename_or_filepath, 'w') as file:
        file.write(content)


@click.command()
@click.argument('application_name')
def cli(application_name):
    current_working_directory = current_dir()
    click.echo("🤖Creating the Flask App🤖")
    try:
        os.mkdir(os.path.join(current_working_directory, application_name))
    except (FileExistsError, Exception):
        sys.exit('Project Already Exists Please Select Another Name 👩‍🏭')
    # Changing the dir to application dir
    os.chdir(os.path.join(current_working_directory, application_name))
    click.echo("Creating the virtual environment📑")
    subprocess.run(['virtualenv', 'venv'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    click.echo("Vitualenv created📩")
    # Making an app directory
    os.mkdir('app')
    # At this point the cwd is
    cwd_at_this_point = current_dir()
    os.chdir(os.path.join(cwd_at_this_point, 'app'))
    # Here is the main game
    # We need to make bunch of folders and file
    # TODO: Step 1->Create a templates Directory
    # TODO: Step 2->Create a static Directory
    # TODO: Step 1->Then create css/js/img directory in static
    click.echo("Creating Templates🗃️")
    os.mkdir('./templates')
    create_file('./templates/index.html', 'Hello world')
    click.echo("Creating Static Folders📁")
    os.mkdir('./static')
    os.mkdir('./static/css')
    os.mkdir('./static/js')
    os.mkdir('./static/img')
    create_file('./__init__.py', "print('hello world')")
    create_file('./routes.py', "print('This is routes file')")
    click.echo("\n")
    click.echo(" SuccessFully Created Project 👍")
