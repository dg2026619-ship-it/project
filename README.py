# project

# 1. 5x5 바둑판 만들기
board = [
    ["+", "+", "+", "+", "+"],
    ["+", "+", "+", "+", "+"],
    ["+", "+", "+", "+", "+"],
    ["+", "+", "+", "+", "+"],
    ["+", "+", "+", "+", "+"]
]

# 현재 커서 위치 (2, 2) 및 시작 플레이어
cursor_x, cursor_y = 2, 2
current_player = "●"

while True:
    # 에러 나는 화면 지우기(os.system)를 빼고, 대신 구분선을 길게 그어줍니다.
    print("\n" + "="*30)
    print("🎮 [w:위] [s:아래] [a:왼쪽] [d:오른쪽] [공백없이 엔터: 돌 놓기]")
    print(f"현재 차례: {current_player}")
    print("="*30)
    
    # 2. 바둑판 출력 (내 위치는 [ ]로 표시)
    for r in range(5):
        row_str = []
        for c in range(5):
            if r == cursor_y and c == cursor_x:
                row_str.append(f"[{board[r][c]}]") # 현재 커서 위치
            else:
                row_str.append(f" {board[r][c]} ")
        print("".join(row_str))
        
    # 3. 키보드 입력 받기
    key = input("\n움직일 키 입력 후 엔터: ").strip().lower()
    
    # 4. 방향키 이동 계산
    if key == 'w' and cursor_y > 0:
        cursor_y -= 1
    elif key == 's' and cursor_y < 4:
        cursor_y += 1
    elif key == 'a' and cursor_x > 0:
        cursor_x -= 1
    elif key == 'd' and cursor_x < 4:
        cursor_x += 1
        
    # 5. 그냥 엔터만 치면 그 자리에 돌 놓기
    elif key == "":
        if board[cursor_y][cursor_x] == "+":
            board[cursor_y][cursor_x] = current_player
            # 차례 바꾸기
            current_player = "○" if current_player == "●" else "●"
        else:
            print("\n❌ 이미 돌이 있는 자리입니다!")
