from typing import List
from functools import lru_cache


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1

        @lru_cache(maxsize=None)
        def all_paths_to_target(current_node):
            if current_node == target:
                return [[target]]

            results = []
            for next_node in graph[current_node]:
                for path in all_paths_to_target(next_node):
                    results.append([current_node] + path)

            return results
        return all_paths_to_target(0)
