def format_string(new_value, path, node, action: str, result: list, old_value=None):
    path += node
    f_string = ''
    strange_means = ['false', 'true', 'none', 'null', '[complex value]']
    if isinstance(new_value, dict):
        new_value = '[complex value]'
    if isinstance(old_value, dict):
        old_value = '[complex value]'
    if new_value not in strange_means:
        new_value = f'\'{new_value}\''
    if old_value not in strange_means:
        old_value = f'\'{old_value}\''
    if action == 'delete':
        f_string = f'Property \'{path}\' was removed\n'
    elif action == 'add':
        f_string = f'Property \'{path}\' was added with value {new_value}\n'
    elif action == 'update':
        f_string = f'Property \'{path}\' was updated. From {old_value} to {new_value}\n'
    result.extend(f_string)
    return result


def status_node(list_of_node, node, status):
    count, result = 0, 'status'
    for point in list_of_node:
        if point == node:
            count += 1
    if count == 1 and status == '+':
        result = 'add'
    elif count == 2 and status == '-':
        result = 'update'
    elif count == 1 and status == ' ':
        result = 'not change'
    elif count == 1 and status == '-':
        result = 'delete'
    return result


def separate_status_of_name(list_of_node):
    formate_node = []
    for point in list_of_node:
        point = point[0:len(point) - 1]
        formate_node.append(point)
    return formate_node


def status_key(diction: dict, result, path='', depth=1):
    keys = list(diction.keys())
    formate_keys_name = separate_status_of_name(keys)
    for node in keys:
        status = str(node)[-1]
        node_for_check = node[0:len(str(node)) - 1]
        what_hapend = status_node(formate_keys_name, node_for_check, status)
        if isinstance(diction[node], dict) and status == ' ':
            path += str(node_for_check) + '.'
            depth += 1
            status_key(diction[node], result, path, depth)
            depth -= 1
            if depth == 1:
                path = ''
        elif what_hapend == 'add':
            format_string(diction[node], path, node_for_check, what_hapend, result)
        elif what_hapend == 'update':
            old_value = diction[node_for_check + "-"]
            new_value = diction[node_for_check + "+"]
            format_string(new_value, path, node_for_check, what_hapend, result, old_value)
        elif what_hapend == 'delete':
            format_string(diction[node], path, node_for_check, what_hapend, result)
    return result
