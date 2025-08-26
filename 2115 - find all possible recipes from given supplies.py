class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        
        graph = {}
        in_edges = {}
        q = deque()

        for sup in supplies:
            graph[sup] = []
            in_edges[sup] = 0
            q.append(sup)
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            ingredient_list = ingredients[i]

            for ingredient in ingredient_list:
                in_edges[recipe] = in_edges.get(recipe, 0) + 1
                graph.setdefault(ingredient, []).append(recipe)
                
        
        result = []

        while q:
            el = q.popleft()
            for neighbor in graph.get(el, []):
                in_edges[neighbor] -= 1
                if in_edges[neighbor] == 0:
                    result.append(neighbor)
                    q.append(neighbor)
        return result