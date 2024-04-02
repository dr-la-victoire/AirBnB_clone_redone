"""This module is the CLI for the AirBnB clone"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """This will inherit from the Cmd class"""
    prompt = "(hbnb) "

    __classes = ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]

    def do_quit(self, line):
        """This function exits the CLI"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the CLI"""
        return True

    def emptyline(self):
        """Implementing the do nothing when enter is pressed"""
        pass

    def do_create(self, line):
        """Creates a new instance of a class & prints its ID"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)

    def do_show(self, line):
        """Prints the str repr of a class based on its ID"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on class name and ID"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all str repr of a class name"""
        objs = []
        if not line:
            print("** class name missing **")
        else:
            if line not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                for values in storage.all().values():
                    if values.__class__.__name__ == line:
                        objs.append(values.__str__())
        print(objs)

    def do_update(self, line):
        """Updates an instance based on the class name and ID"""
        args = line.split(" ")
        # Getting a dictionary of all the stored instances
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
