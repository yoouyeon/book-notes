---
name: book-notes-create-chapter-note
description: 책 디렉토리의 README.md 목차를 읽어 챕터에 해당하는 노트 파일을 생성
model: haiku
argument-hint: <책 디렉토리>
allowed-tools: Bash(python3 *create-notes.py*)
---

## Derived Values

- 책 디렉토리 : $ARGUMENTS[0]

## Steps

이 명령어를 실행한다: `python3 create-notes.py "$책 디렉토리"`

## Exceptions

- 책 디렉토리명이 입력되지 않은 경우 : "책 디렉토리명을 입력해주세요." 라는 메시지를 출력하고 종료한다.

## Self-Check

- 목차 섹션에 있는 챕터의 수 만큼 노트 파일이 존재하는가?
- 각 `챕터 이름`에 해당하는 노트 파일이 생성되었는가?
- 목차의 `챕터 이름` 뒤에 노트 파일 링크가 추가되었는가?

## Next Step

작업 완료 후 아래 메시지를 출력한다.

```
챕터 노트가 생성되었습니다. 각 챕터 노트 파일에 책을 읽고 공부한 내용을 기록하세요.
정리를 완료한 뒤에는 아래 명령어로 노트를 검토할 수 있습니다.

/book-notes-review $ARGUMENTS[0]/<노트 파일 이름>
```
