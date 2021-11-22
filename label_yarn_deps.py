import json, copy
import anytree
from anytree import Node, RenderTree
import semantic_version

## first run yarn list --json in project
YARN_LIST_JSON_FILE = 'yarn_deps.json'
data = None

with open(YARN_LIST_JSON_FILE, 'r') as input:
    data = json.load(input)


## convert from list of dependencies to dict

dependency_list = data['data']['trees']

root=Node('root')
deps_root = Node('deps',root)
peer_root = Node('peer deps',root)
dev_root = Node('dev deps',root)
unknown_root = Node('unclassified deps',root)


top_deps = {
    "react": {'version':"^17.0.2"},
    "react-dom":{'version':"^17.0.2"},
    "react-redux": {'version':"^7.2.6"},
    "redux": {'version':"^4.1.2"},
    "web-vitals": {'version':"^2.1.2"}
}

top_dev_deps = {
    "@storybook/addon-actions": {'version':  "^6.3.0"},
    "@storybook/addon-essentials": {'version': "^6.3.0"},
    "@storybook/addon-links": {'version': "^6.3.0"},
    "@storybook/addon-storyshots": {'version': "^6.3.12"},
    "@storybook/node-logger": {'version': "^6.3.0"},
    "@storybook/preset-create-react-app": {'version': "^3.1.7"},
    "@storybook/react": {'version': "^6.3.0"},
    "@storybook/testing-react": {'version': "^0.0.17"},
    "@testing-library/jest-dom": {'version': "^5.11.4"},
    "@testing-library/react": {'version': "^11.1.0"},
    "@testing-library/user-event": {'version': "^12.1.10"},
    "chromatic": {'version': "^6.0.6"},
    "react-scripts": {'version': "4.0.3"},
    "react-test-renderer": {'version': "^17.0.2"}
}

"foo".startswith('foo')

def package_string_to_node(s):
    """
    'ps1@1.8.0' --> Node('ps1',version='1.8.0')
    '@testing-library/react@11.1.0' --> Node('@testing-library/react', version='11.1.0')
    """

    temp = s.split('@')
    version = temp[-1]
    name = '@'.join(temp[:-1])
    return Node(name, version=version)

def add_child(parent, child):

    if len(parent.children) == 0:
        parent.children = child
    else:
        kids = list(parent.children).append(child)
        parent.children=kids
    

def classify_node(trees, dependency_lists):
    """ 

    @param dependency_lists:    ie [{'package1': {'version': 'xxx}}, ]
    @param trees:               list of anytree root nodes"""

    pass

for dep in dependency_list:
    key = dep['name']
    tmp = key.split('@')[:-1]  # last '@' should be for version number
    version = key.split('@')[-1]
    name = '@'.join(tmp)
    child_nodes = [package_string_to_node(i['name']) for i in dependency_list[0]['children'] if dependency_list[0].get('children')]
    n = Node(name, version=version, children=child_nodes)
    

    # remember could be in more then one root/tree
    if name in top_deps:
        pass
        ## and semver match
        
    
    if name in top_dev_deps:
        pass

    ## search existing root nodes
    candidates = anytree.search.findall(root, filter_=lambda node: node.name==name)

    if not candidates:
        pass
        add_child(unknown_root, n)
    else:
    ## need to do the semver match thingy

    ## discard any candidates that already have children populated
    ## n.parent = remaining candidates, excpet you have to do a copy or whatever because
    ## this doesnot support mult-parents
