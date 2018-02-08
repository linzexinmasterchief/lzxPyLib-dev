# this tree.py is used for constructing a tree data structure, the tree will be made by node
# this is the definition of a single node class
class node():
    
    # each node will have three attributes: ancestor, children, name and value
    # the ancestor is set to self by default in __init__, there will be only one ancestor for one node, 
    #   this will be reset while the current node is set to be a child of another node
    ancestor = None
    # the children list contains all the child nodes of this node, set to empty by default
    children = []
    # name is the identifier of this node, !!!THERE MUST NOT BE TWO NODES WITH SAME NAME IN ONE LIST!!!
    name = ""
    # value is the value carried by this node
    value = ""
    
    # the initialization should initialize all the attributes using set functions
    def __init__(self, name = "", value = "empty", child = None, children = [], ancestor = None):
        # initialize ancestor
        try:
            self.set_ancestor(ancestor)
        except:
            # if no ancestor is asigned or any error occured, set ancestor to self
            self.ancestor = self
        
        # initialize children list
        try:
            self.set_children(child, children)
        except:
            # if no children list is asigned or any error occured, set children list to empty
            self.children = []

        # initialize name
        # handle no errors since name is critical for identify and not replicatable
        self.set_name(name)

        # initialize value
        try:
            self.set_value(value)
        except:
            self.value = "empty"

    # all the getters and setters are below this comment
    def set_name(self, name = ""):
        # first check if the name is a string, then check if the name is empty or not
        if type(name) != type(""):
            # the name must be a string, since using numbers as identifier is easy to be replicated
            raise TypeError("name must be string!")
        elif name == "":
            # obviously that the name should not be left empty
            raise ValueError("name must not be empty!")
        else:
            # if everything is normal, pass the inputed name value to self.name attribute
            self.name = name

    # TODU: make get_name function
    def get_name(self):
        return self.name

    def set_value(self, value = "empty"):
        # check if the value is a string
        if type(value) != type(""):
            # TODU: find a way to allow the value attribute to contain all types of value
            # the value is currently set to only be string, but not forever
            raise TypeError("value must be string!")
        else:
            self.value = value

    # TODU: make get_value function
    def get_value(self):
        return self.value
    
    def set_children(self, child = None, children = []):
        # !!!BE CAREFUL WHEN USING THIS FUNCTION!!! the input value will overide the existing value
        # this function allow the user to either input only one child or a list of child
        # the most important part is that the child must be a node
        # if the children list input is empty, check the child input
        if children != []:
            # iterate through the children list
            for node in children:
                # check if every child in the children list is a node
                if not isinstance(self, type(node)):
                    # if not, throw an error
                    raise TypeError("there is one or more items that is not a node")
            self.children = children
        elif child != None:
            # check if the child is a node
            if not isinstance(self, type(child)):
                # if not, throw an error
                raise TypeError("there is one or more items that is not a node")
            else:
                # !!!BE CAREFUL HERE!!!
                # since the self.children is a list, directly asign child to children will cause
                #  the list to became a single node, which is dangerouse because a single node
                #  don't have the ability to contain multiple nodes
                self.children = [child]
        else:
            # if both child and children are empty, throw an error
            raise ValueError("can't find input node!")

    def add_children(self, child = None, children = []):
        # this function allow the user to either input only one child or a list of child
        # the input value will be append to the children list after checking
        # the most important part is that the child must be a node
        # if the children list input is empty, check the child input
        if children != []:
            # iterate through the children list
            for node in children:
                # if the node is not an node :P raise an error
                if not isinstance(self, type(node)):
                    raise TypeError("there is one or more items that is not a node")
                # append input nodes to children list
                self.children.append(node)
        elif child != None:
            # check if the child is a node, if not, raise an error
            if not isinstance(self, type(child)):
                raise TypeError("there is one or more items that is not a node")
            else:
                # append input node to children list
                self.children.append(child)
        else:
            # if both child and children are empty, throw an error
            raise ValueError("can't find input node!")

    def get_children(self):
        return self.children

    # TODU: define set_ancestor and get_ancestor functions
    def set_ancestor(self, ancestor = None):
        if ancestor == None:
            self.ancestor = self
        else:
            self.ancestor = ancestor

    def get_ancestor(self):
        return self.ancestor

#=========test area=========#
# node1 = node()
# ch_node = node()
# ad_node = node()
# node1.set_children(ch_node)
# node1.add_children(ad_node)
# print(node1.get_children())