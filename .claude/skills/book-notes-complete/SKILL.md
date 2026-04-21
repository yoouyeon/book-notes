---
name: book-notes-complete
description: 책 디렉토리의 모든 챕터 노트 status를 확인하고, 모두 completed이면 루트 README.md에 완독 표시를 추가
model: haiku
argument-hint: <책 디렉토리>
allowed-tools: Bash(python3 *check-complete.py*)
---

## Derived Values

- 책 디렉토리 : $ARGUMENTS[0]

## Steps

1. 이 명령어를 실행한다: `python3 check-complete.py "$책 디렉토리"`
2. 실행 결과가 `true`인 경우:
   - 루트 `README.md`에서 해당 책 항목의 `🟡 읽는 중`을 `🟢 완독`으로 변경한다.
   - "모든 챕터 노트가 완료되었습니다. 루트 README.md에 완독 표시를 추가했습니다." 메시지를 출력한다.
3. 실행 결과가 `false`인 경우:
   - 완료되지 않은 챕터 목록을 출력하고 종료한다.

## Exceptions

- 책 디렉토리명이 입력되지 않은 경우 : "책 디렉토리명을 입력해주세요." 라는 메시지를 출력하고 종료한다.
