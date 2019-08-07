#!/usr/bin/env python
from sys import argv

import graphviz
import neutron_lib.api.definitions as nlibs


def main():
    exts = []
    for nlib in nlibs._ALL_API_DEFINITIONS:
        exts.append((nlib.ALIAS, nlib.REQUIRED_EXTENSIONS))
    dot = graphviz.Digraph('neutron-extensions-requirements', format='svg')
    for ext in exts:
        if ext[1]:
            dot.node(ext[0])
            for e in ext[1]:
                dot.edge(ext[0], e)

    if len(argv) > 1:
        dot.render(argv[1])
    else:
        dot.render(view=True)


if __name__ == '__main__':
    main()
