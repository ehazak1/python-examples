'''
The Kaprekar process.
'''

def step(x):
    '''
    One step in the Kaprekar process:
    0. take a 4-digit number
    1. sort the digits in descending order
    2. sort the digits in ascending order
    3. return descending minus ascending

        >>> step(6264)
        4176
        >>> step(4176)
        6174
        >>> step(6174)
        6174
    '''
    zero_padded = '%04d' % x
    descending = int(''.join(sorted(zero_padded, reverse=True)))
    ascending = int(''.join(sorted(zero_padded)))
    return descending - ascending


def gen_graph():
    '''
    Print a graph of the Kaprekar process for 4-digit numbers
    in the graphviz "dot" format.

        Bash:
        $ python kaprekar.py | dot -Tsvg > kaprekar.svg
    '''
    # experiment with GraphViz at http://interactive.blockdiag.com/
    # the GraphViz program can be downloaded from http://graphviz.org/
    
    graph = {}
    for i in range(10000):
        graph['%04d' % i] = '%04d' % step(i)

    non_leaves = set(graph.values())
    leaves = set(graph.keys()) - non_leaves

    groups = {}
    for leaf in leaves:
        target = graph[leaf]
        if target not in groups:
            groups[target] = set()
        groups[target].add(leaf)

    print '''
        digraph {
        graph [rankdir="LR"];
    '''
    for source in sorted(non_leaves):
        print '%s -> %s;' % (source, graph[source])

    print 'node [shape="rectangle"];'
    for target, group in groups.items():
        label = ', '.join(sorted(group)[:3])
        print '"%s ..." -> %s [label=%s];' % (label, target, len(group))
    print '}'
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    gen_graph()
