# We notice that the problem can be restated as a graph problem. We want to find a path on the complete directed graph on vertices 0 through 9 such that all sequences in the keylogs appear as (non-consecutive) subpaths.
# This can be done manually by drawing the additional required edges at each step, and removing any edges :math:`(a,b)` if the rest of the path goes through :math:`a` and later through :math:`b`.
