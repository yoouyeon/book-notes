---
name: book-notes-commit
description: stage된 변경사항에 해당하는 커밋 메시지를 생성하여 커밋
model: sonnet
allowed-tools: Bash(git status), Bash(git -C * status), Bash(git diff *), Bash(git -C * diff *)
---

## Steps

1. `git status` 명령어를 실행하여 stage된 변경사항이 있는지 확인한다.
2. stage된 변경사항이 있는 경우 `git diff --cached` 명령어를 실행하여 stage된 변경사항의 내용을 확인한다.
3. 변경사항의 내용과 Commit Message Rules을 바탕으로 커밋 메시지를 생성한다. 커밋 메시지 예시는 [example.md](example.md) 파일을 참고한다.
4. 커밋한다.
  - Co-Author를 명시하지 않는다.

## Commit Message Rules

```text
<type>(<scope>): <한국어 설명>
```

허용하는 type과 해당하는 scope는 다음과 같다.

- `book`: 책 등록, 목차, 책 README 변경, 책 상태 변경. scope는 책 디렉토리 이름.
- `note`: 책 디렉토리 하위 노트 본문 추가 또는 수정. scope는 책 디렉토리 이름.
- `skill`: Claude book-notes 스킬 변경. scope은 스킬 이름.
- `repo`: 저장소 설정, 정리, 전역 문서 변경. scope는 생략

커밋 메시지 예시는 [example.md](example.md) 파일을 참고한다.

## Exceptions

- stage된 변경사항이 없는 경우 : "커밋할 변경사항이 없습니다." 라는 메시지를 출력하고 종료한다.

## Self-Check

- 커밋 메시지가 Commit Message Rules을 준수하는가?
- 커밋 메시지가 변경사항의 내용을 정확하게 설명하는가?
- 커밋 메시지가 명확하고 간결한가?
- 커밋 메시지가 영어 대신 한국어로 작성되었는가?
- co-author가 명시되어 있지 않은가?
