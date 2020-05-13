# -*- coding: utf-8 -*-

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Check the group's immediate visible users
    
    users_in_group = group.get_users()
    if user in users_in_group:
        return True
    else:
        # Recurse through the group's groups and check if user exists in any
        groups_in_group = group.get_groups()
        for item in groups_in_group:
            if is_user_in_group(user, item):
                return True
    return False


parent = Group("parent")

parent_user1="parent_user1"

parent.add_user(parent_user1)

child1 = Group("child1")

child2 = Group("child2")

sub_child1 = Group("subchild1")
sub_child2 = Group("subchild2")


sub_child_user = "sub_child_user"
sub_child1.add_user(sub_child_user)

child1.add_group(sub_child1)

child2.add_group(sub_child2)

parent.add_group(child1)

#checking for the sub child in the parent group
print(is_user_in_group(sub_child_user,parent)) # returns True


#checking for the parent user in the child1 group
print(is_user_in_group(parent_user1,child1)) # returns False


#checking for the sub child1 user in the child2 group
print(is_user_in_group(sub_child_user,child2)) # returns False


#


