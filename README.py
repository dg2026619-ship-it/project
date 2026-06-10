Web VPython 3.2


board = [["+"] * 5 for _ in range(5)]
cx, cy = 2, 2
turn = "●"

while True:
    print(f"\n현재 차례: {turn} [w,a,s,d: 이동 / 엔터: 돌놓기]")
    for r in range(5):
        row = [f"[{board[r][c]}]" if r == cy and c == cx else f" {board[r][c]} " for c in range(5)]
        print("".join(row))
    key = input("입력: ").strip().lower()
    if key == 'w': cy = max(0, cy - 1)
    elif key == 's': cy = min(4, cy + 1)
    elif key == 'a': cx = max(0, cx - 1)
    elif key == 'd': cx = min(4, cx + 1)
    elif key == "":
        if board[cy][cx] == "+":
            board[cy][cx] = turn
            won = False
            lines = []
            for r in range(5):
                lines.append("".join(board[r]))
            for c in range(5):
                lines.append("".join([board[r][c] for r in range(5)]))
            lines.append("".join([board[i][i] for i in range(5)]))        # ↘ 중심 대각선
            lines.append("".join([board[i][4-i] for i in range(5)]))      # ↙ 중심 대각선
            lines.append("".join([board[i][i+1] for i in range(4)]))      # ↘ 위쪽 대각선
            lines.append("".join([board[i+1][i] for i in range(4)]))      # ↘ 아래쪽 대각선
            lines.append("".join([board[i][3-i] for i in range(4)]))      # ↙ 위쪽 대각선
            lines.append("".join([board[i+1][4-i] for i in range(4)]))    # ↙ 아래쪽 대각선
            target = turn * 3  
            for line in lines:
                if target in line:
                    won = True
            if won:
                print(f"\n🎉 {turn} 승리! 게임을 종료합니다.")
                break
                
            turn = "○" if turn == "●" else "●"
            turn = "○" if turn == "●" else "●"
