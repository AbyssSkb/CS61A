def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not branches(tree)


def is_tree(tree):
    if not isinstance(tree, list) or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])
result = label(min(branches(max([t1, t2], key=label)), key=label))
print(result)
