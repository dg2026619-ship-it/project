# project

# 1. 바둑판과 초기 설정
board = [["+"] * 5 for _ in range(5)]
cx, cy = 2, 2
turn = "●"

while True:
    print(f"\n현재 차례: {turn} [w,a,s,d: 이동 / 엔터: 돌놓기]")
    
    # 2. 바둑판 출력
    for r in range(5):
        row = [f"[{board[r][c]}]" if r == cy and c == cx else f" {board[r][c]} " for c in range(5)]
        print("".join(row))
        
    key = input("입력: ").strip().lower()
    
    # 3. 이동 처리
    if key == 'w': cy = max(0, cy - 1)
    elif key == 's': cy = min(4, cy + 1)
    elif key == 'a': cx = max(0, cx - 1)
    elif key == 'd': cx = min(4, cx + 1)
        
    # 4. 돌 놓기
    elif key == "":
        if board[cy][cx] == "+":
            board[cy][cx] = turn
            
            # 5. 초간단 승리 체크 (글자 이어붙여서 찾기!)
            won = False
            lines = []

            # 가로 줄들을 문자열로 합치기 (예: "+++●●")
            for r in range(5):
                lines.append("".join(board[r]))
                
            # 세로 줄들을 문자열로 합치기
            for c in range(5):
                lines.append("".join([board[r][c] for r in range(5)]))
                
            # 대각선 줄들을 문자열로 합치기 (필요한 대각선만 쏙쏙)
            lines.append("".join([board[i][i] for i in range(5)]))        # ↘ 중심 대각선
            lines.append("".join([board[i][4-i] for i in range(5)]))      # ↙ 중심 대각선
            lines.append("".join([board[i][i+1] for i in range(4)]))      # ↘ 위쪽 대각선
            lines.append("".join([board[i+1][i] for i in range(4)]))      # ↘ 아래쪽 대각선
            lines.append("".join([board[i][3-i] for i in range(4)]))      # ↙ 위쪽 대각선
            lines.append("".join([board[i+1][4-i] for i in range(4)]))    # ↙ 아래쪽 대각선

            # 만든 줄 중에 플레이어 돌이 3개 연속("●●●" 또는 "○○○")으로 들어있는지 검사!
            target = turn * 3  # "●●●" 또는 "○○○"
            for line in lines:
                if target in line:
                    won = True

            if won:
                print(f"\n🎉 {turn} 승리! 게임을 종료합니다.")
                break
                
            turn = "○" if turn == "●" else "●"
