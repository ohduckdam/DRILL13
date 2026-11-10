# Drill #13 - 아이템 모드

pico2d 게임 프레임워크(LEC15)에 아이템 모드를 추가한 과제.

## 실행

    cd LEC15_Game_Framework
    python main.py

## 조작

| 모드 | 키 | 동작 |
|---|---|---|
| title | Space | 게임 시작 |
| play | ← / → | 이동 |
| play | Space | 공 던지기 (잠들어 있으면 깨우기) |
| play | P | 아이템 모드 열기 |
| play | ESC | 타이틀로 |
| item | 0 | 공 없음 |
| item | 1 | 작은 공 (기본) |
| item | 2 | 큰 공 |
| item | ← / → / Space | 아이템 창이 떠 있어도 이동·발사 가능 |
| item | ESC / P | 선택 없이 닫기 |

아이템 모드에서도 게임은 멈추지 않고 계속 진행되며, 화면 위에 선택 창이 표시된다.
