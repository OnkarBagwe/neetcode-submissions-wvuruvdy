class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org = image[sr][sc]
        if org == color:
            return image

        ROWS = len(image)
        COLS = len(image[0])

        q = deque([(sr,sc)])

        image[sr][sc] = color

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while q:
            r,c = q.popleft()

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if nr in range(ROWS) and nc in range(COLS) and image[nr][nc] == org:
                    image[nr][nc] = color
                    q.append((nr,nc))

        return image