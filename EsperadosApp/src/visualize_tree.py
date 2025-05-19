import os
from graphviz import Digraph

def print_tree(node, parser, graph, parent_id=None, node_id=0):
    label = parser.ruleNames[node.getRuleIndex()] if hasattr(node, "getRuleIndex") else str(node)
    cur_id = str(node_id)
    graph.node(cur_id, label)

    if parent_id is not None:
        graph.edge(parent_id, cur_id)

    if hasattr(node, 'children'):
        child_id = node_id + 1
        for child in node.children:
            child_id = print_tree(child, parser, graph, cur_id, child_id)
        return child_id
    else:
        return node_id + 1

def visualize_tree(tree, parser, file_path: str):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    
    output_dir = os.path.join(os.path.dirname(file_path), "..", "Examples")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, base_name + '_ast')

    dot = Digraph(comment='Esperados AST')
    dot.attr('node', shape='box', style='filled', color='lightblue2', fontname='Arial')
    print_tree(tree, parser, dot)
    dot.render(filename=output_file, format='png', cleanup=True, view=True)