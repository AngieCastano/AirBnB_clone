#!/usr/bin/python3
"""AirBnB console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Console of AirBnB"""
    prompt = '(hbnb) '
    classes = ["BaseModel", "Amenity", "City", "Place", "Review",
               "State", "User"]

    def do_quit(self, args):
        """Quit command, exits the program """
        exit()

    def do_EOF(self, args):
        """End of file, exits the program"""
        exit()

    def emptyline(self):
        """Adds a new line when press Enter key"""
        pass

    def do_create(self, args):
        """Creates a Base model instance and saves it to  the JSON file"""
        if len(args.split()) == 0:
            print("** class name missing **")
        else:
            if args.split()[0] in HBNBCommand.classes:
                instance = globals()[args]()
                instance.save()
                print(str(instance.id))
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        storage.reload()
        if len(args.split()) == 0:
            print("** class name missing **")
        elif len(args.split()) == 1:
            if args.split()[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            try:
                print(storage.all()[args.split()[0] + "." + args.split()[1]])
                storage.reload()
            except(KeyError):
                print("** no instance found **")

    def do_destroy(self, args):
        """Destroys an instance"""
        storage.reload()
        if len(args.split()) == 0:
            print("** class name missing **")
        elif len(args.split()) == 1:
            if args.split()[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            try:
                del storage.all()[args.split()[0] + "." + args.split()[1]]
                storage.save()
            except(KeyError):
                print("** no instance found **")

    def do_all(self, args):
        """Brings all objects stored"""
        storage.reload()
        inst = []
        if len(args.split()) == 0:
            for key, value in storage.all().items():
                inst.append(str(value))
            print(inst)
        elif args.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                inst.append(str(value))
            print(inst)

    def do_update(self, args):
        """updates an object considering its id"""
        if len(args.split()) == 0:
            print("** class name missing **")
        elif len(args.split()) == 1:
            print("** instance id missing **")
        elif len(args.split()) == 2:
            print("** attribute name missing **")
        elif len(args.split()) == 3:
            print("** value missing **")
        else:
            if args.split()[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                try:
                    setattr(storage.all()
                            [args.split()[0] + "." +
                             args.split()[1]], args.split()[2],
                            args.split()[3])
                    storage.save()
                except(KeyError):
                    print("** no instance found **")

    def do_pcount(self, args):
        """Class.all()"""
        i = 0
        for key, value in storage.all().items():
            if key.split(".")[0] == args.split()[0]:
                i += 1
        print(i)

    def do_pall(self, args):
        print("[", end="")
        for key, value in storage.all().items():
            if key.split(".")[0] == args.split()[0]:
                print(value, end="")
        print("]")

    def do_pshow(self, args):
        """Shows a instance by its user and by its id"""
        try:
            print(storage.all()[args.split()[0] + "." + args.split()[1]])
            storage.reload()
        except(KeyError):
            print("** no instance found **")

    def do_pdestroy(self, args):
        """Destroys an instance by it is and its class"""
        storage.reload()
        try:
            del storage.all()[args.split()[0] + "." + args.split()[1]]
            storage.save()
        except(KeyError):
            print("** no instance found **")

    def do_pupdate(self, args):
        """updates an object considering its id"""
        if len(args.split()) == 0:
            print("** class name missing **")
        elif len(args.split()) == 1:
            print("** instance id missing **")
        elif len(args.split()) == 2:
            print("** attribute name missing **")
        elif len(args.split()) == 3:
            print("** value missing **")
        else:
            if args.split()[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                try:
                    setattr(storage.all()
                            [args.split()[0] + "." +
                             args.split()[1]], args.split()[2],
                            args.split()[3])
                    storage.save()
                except(KeyError):
                    print("** no instance found **")

    def do_pupdate(self, args):
        """updates an object considering its id"""
        try:
            setattr(storage.all()[args.split()[0].replace("\"", "") +
                                  "." + args.split()[1].replace("\"", "")
                                  .replace(",", "")],
                    args.split()[2].replace(",", "").replace("\"", ""),
                    args.split()[3].replace(",", ""))
            storage.save()
        except(KeyError):
            print("** no instance found **")

    def precmd(self, line):
        """Modifies the line from the command"""
        if len(line.split(".")) > 1:
            first = line.split(".")[1].split("(")[0]
            second = line.split(".")[0]
            third = line.split(".")[1].split("(")[1] .replace(")", "")
            return "p{} {} {}".format(first, second, third)
        else:
            return line
if __name__ == '__main__':
    storage = FileStorage()
    storage.reload()
    HBNBCommand().cmdloop()
