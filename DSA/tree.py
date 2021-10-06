class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self,item):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if item == 'name':
            print(prefix + self.data.split(" ",1)[0])
        elif item == 'designation':
            print(prefix + self.data.split(" ",1)[1])
        elif item == 'both':
            print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(item)

def build_management_tree():
    root = TreeNode("Nilpul (CEO)")

    Infa = TreeNode("vishwa (Infrastructure Head)")
    Infa.add_child(TreeNode("Dhaval (Cloud Manager)"))
    Infa.add_child(TreeNode("Abhijit (App Manager)"))

    CTO = TreeNode("Chinmay (CTO)")
    CTO.add_child(Infa)
    CTO.add_child(TreeNode("Aamir (Application Head)"))

    HR = TreeNode("Gels (HR HEAD)")
    HR.add_child(TreeNode("Peter (Recruitment Manager)"))
    HR.add_child(TreeNode("Waqas (Policy Manager)"))

    Infa = TreeNode("vishwa (Infrastructure Head)")
    Infa.add_child(TreeNode("Dhaval (Cloud Manager)"))
    Infa.add_child(TreeNode("Abhijit (App Manager)"))

    root.add_child(CTO)
    root.add_child(HR)
    return root


if __name__ == '__main__':
    #root_node = TreeNode(None)
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")