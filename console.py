#!/usr/bin/python3
'''the entry point of the command interpreter'''


from shlex import split

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State

from models import storage

import cmd
'''cmd model'''


class HBNBCommand(cmd.Cmd):
    '''the class of the command interpreter'''

    prompt = "(hbnb) "

    def emptyline(self):
        '''to skip the empty line'''
        pass

    def parse(self, strr):
        '''a function to parse the line and return a list of the arguments'''
        argv = strr.split()
        arg = list()
        s = ""
        i = 0
        for j in argv:
            if j[0] == '"' and j[len(j) - 1] == '"':
                arg.append(j)
            elif j[len(j) - 1] == '"':
                i = 0
                s += j
                s += " "
                arg.append(s)
                s = ""
            elif j[0] == '"':
                i += 1
                s += j
            else:
                if i == 0:
                    arg.append(j)
                else:
                    s += " "
                    s += j
        return arg

    def checkClass(self, obj):
        '''a function to check if the obj's type is or is not in this list
            obj => the object
            Return: True if the obj's type exist, False if not
        '''
        classList = [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]
        for i in classList:
            if obj == i:
                return True
        return False

    def default(self, line):
        '''set the defult when it doesn't recognaize the command'''

        default = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "count": self.do_count
                }
        try:
            argv = line.split(".")
            argv += argv[1].split("(")
            argv += argv[3].split(")")
            command = "{} {}".format(argv[0], argv[4])
            c = command.split(", ", 1)
            if len(c) == 2 and c[1][0] == "{":
                cmd = "{} ".format(c[0])
                c = eval(c[1])
                for i in c:
                    cmd += " {}".format(i)
                    cmd += " {}".format(str(c[i]))
                for i in default:
                    if i == argv[2]:
                        return default[i](cmd)
            else:
                cmd = ""
                c = command.split(",")
                for i in c:
                    cmd += i + " "
                for i in default:
                    if i == argv[2]:
                        return default[i](cmd)
        except (IndexError, AttributeError):
            pass
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program
        '''
        print("")
        return True

    def do_create(self, obj):
        '''Usage: create a new <class>
        Create command to creates a new instance and print the id
        '''
        argv = self.parse(obj)
        if len(argv) == 0:
            print("** class name missing **")
        elif self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")

        new_ins = eval(argv[0])()
        if len(argv) > 1:
            for i in range(1, len(argv)):
                # Arguments parsed for key and value
                key = argv[i][:argv[i].find('=')]
                value = argv[i][argv[i].find('=') + 1:]

                value = value.replace('\"', '')
                value = value.replace('_', ' ')
                try:
                    new_instance.__dict__[key] = eval(value)
                except Exception as e:
                    pass

        new_ins.save()
        print(new_ins.id)

    def do_show(self, arg):
        '''Usage: print the <class> <id>
        Show command to prints the string representation of an instance
        based on the class name and id
        '''
        argv = self.parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
        elif self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            o = 0
            store = storage.all()
            s = "{}.{}".format(argv[0], argv[1])
            for i in store:
                if i == s:
                    o = 1
                    print(store[s])
            if o == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''Usage: deletes an instance of a <class>
        Destroy deletes an instance based on the class name and id
        '''
        argv = self.parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
        elif self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            o = 0
            store = storage.all()
            s = "{}.{}".format(argv[0], argv[1])
            for i in store:
                if i == s:
                    o = 1
            if o == 0:
                print("** no instance found **")
            else:
                del store[s]
                storage.save()

    def do_all(self, obj):
        '''Usage: print all string representation of the <class>
        All prints all string representation of all instances of a class
        '''
        lis = list()
        argv = self.parse(obj)
        if len(argv) != 0:
            if self.checkClass(argv[0]) is not True:
                print("** class doesn't exist **")
            else:
                for i in storage.all(eval(argv[0])).values():
                    if argv[0] == i.__class__.__name__:
                        lis.append(i.__str__())
        else:
            for i in storage.all().values():
                    lis.append(i.__str__())

        print(lis)
    def do_update(self, strr):
        '''Usage: updates the instance of the <class> based on <id>
        Update updates an instance based on the class name and id
        '''

        argv = self.parse(strr)
        store = storage.all()
        if len(argv) == 0:
            print("** class name missing **")
            return False
        elif self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")
            return False
        elif len(argv) < 2:
            print("** instance id missing **")
            return False
        else:
            o = 0
            s = "{}.{}".format(argv[0], argv[1])
            for i in store:
                if i == s:
                    o = 1
            if o == 0:
                print("** no instance found **")
                return False
            if len(argv) < 3:
                print("** attribute name missing **")
                return False
            elif len(argv) < 4:
                print("** value missing **")
                return False
            elif len(argv) > 4:
                att = 2
                val = 3
                obj = store[s]
                while val < len(argv):
                    obj.__dict__[argv[att]] = argv[val]
                    val += 1
                    att += 1
            else:
                obj = store[s]
                obj.__dict__[argv[2]] = argv[3]
        storage.save()

    def do_count(self, line):
        '''Usage: Count counts the instances of a <class>
        retrieve the number of instances of a class
        '''
        store = storage.all()
        s = 0
        argv = self.parse(line)
        if len(argv) != 0:
            for i in store:
                m = i.split(".")
                if argv[0] == m[0]:
                    s += 1
            print(s)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
