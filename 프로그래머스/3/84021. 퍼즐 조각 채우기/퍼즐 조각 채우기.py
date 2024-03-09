def solution(game_board, table):
    answer = -1
    n = len(table)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]    
    
    board_shards = []
    table_shards = []
    
    #find table shard
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                #bfs
                shard = [(0, 0)]
                table[i][j] = 0
                q = [(i, j)]
                while q:
                    cy, cx = q.pop(0)
                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if table[ny][nx] == 1:
                            q.append((ny, nx))
                            shard.append((ny-i, nx-j))
                            table[ny][nx] = 0
                table_shards.append(shard)
    #find board shard
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                #bfs
                shard = [(0, 0)]
                game_board[i][j] = 1
                q = [(i, j)]
                while q:
                    cy, cx = q.pop(0)
                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if game_board[ny][nx] == 0:
                            q.append((ny, nx))
                            shard.append((ny-i, nx-j))
                            game_board[ny][nx] = 1
                board_shards.append(shard)
                
    table_shards.sort(key=lambda x: len(x))
    board_shards.sort()
    while table_shards:
        cur_table_shard = table_shards.pop()
        rotated_shard = []
        rotate_result = []
        
        mx = max(cur_table_shard, key=lambda x:x[1])[1]
        my = max(cur_table_shard, key=lambda x:x[0])[0]
        #rotation
        for c in range(4):
            rr = []
            if c == 0:
                for y, x in cur_table_shard:
                    temp = (x, max(mx, my) -y-1)
                    rr.append(temp)
            else:
                for y, x in rotated_shard[-1]:
                    temp = (x, max(mx, my) -y-1)
                    rr.append(temp)
                    
            rotated_shard.append(rr)
            print(rr)
        
        for shard in rotated_shard:
            shard.sort(key = lambda x : (x[0], x[1]))
            y, x = 0, 0
            for s in range(len(shard)):
                if s == 0:
                    y, x = -1 * shard[s][0], -1 * shard[s][1]
                    shard[s] = (0, 0)
                    continue 
                shard[s] = (shard[s][0]+y, shard[s][1]+x)
            rotate_result.append(shard)
        rotate_result.sort()
        
        for b in board_shards:
            if sorted(b) in rotate_result:
                print("OK", sorted(b))
                board_shards.remove(b) 
                answer += len(b)
                break
        print()
    return answer+1