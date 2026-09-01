class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        grid = classroom
        sr = sc = -1
        litter_bit = {}
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == 'S':
                    sr, sc = i, j
                elif c == 'L':
                    litter_bit[(i, j)] = len(litter_bit)
        total = len(litter_bit)
        overfull = (1 << total) - 1
        if total == 0:
            return 0
        done = [[[bytearray(1 << total) for _ in range(energy + 1)] for _ in range(n)] for _ in range(m)]
        done[sr][sc][energy][0] = 1
        box = deque([(sr, sc, energy, 0)])
        moves = 0
        disha = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while box:
            for _ in range(len(box)):
                r, c, leftover, total_lit = box.popleft()
                if total_lit == overfull:
                    return moves
                if leftover == 0:
                    continue
                for dr, dc in disha:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == 'X':
                        continue
                    ne = energy if grid[nr][nc] == 'R' else leftover - 1
                    now_lit = total_lit
                    if (nr, nc) in litter_bit:
                        now_lit |= (1 << litter_bit[(nr, nc)])
                    if not done[nr][nc][ne][now_lit]:
                        done[nr][nc][ne][now_lit] = 1
                        box.append((nr, nc, ne, now_lit))
            moves += 1
        return -1 
        