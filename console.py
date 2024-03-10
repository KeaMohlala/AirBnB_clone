#!/usr/bin/python3
"""Module for the console."""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            else:
                new_instance = models.classes[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(class_name, args[1])
                objects = models.storage.all()
                print(objects.get(key, "** no instance found **"))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(class_name, args[1])
                objects = models.storage.all()
                if key in objects:
                    del objects[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = shlex.split(arg)
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            else:
                filtered_objs = [str(obj) for obj in objects.values()
                                 if obj.__class__.__name__ == class_name]
                print(filtered_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(class_name, args[1])
                objects = models.storage.all()
                if key not in objects:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj = objects[key]
                    attr_name = args[2]
                    attr_value = args[3]
                    setattr(obj, attr_name, attr_value)
                    obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
