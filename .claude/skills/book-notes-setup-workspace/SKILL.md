---
name: book-notes-setup-workspace
description: 처음 읽기 시작한 책의 디렉토리를 생성하고, 하위에 목차를 기록한 README.md 파일을 생성
model: haiku
argument-hint: <책 이름> <분류>
allowed-tools: Bash(printf *), Bash(sed *), Bash(mkdir *)
---

## Derived Values

- 책 제목 : $ARGUMENTS[0]
- 책 분류 : $ARGUMENTS[1]
- 책 디렉토리 경로 : !`printf '%s' "$ARGUMENTS[0]" | sed -E 's/[[:space:]]+/-/g; s/^-+|-+$//g'`

## Steps

1. 책 디렉토리 생성
   - `mkdir -p "$책 디렉토리 경로"`
2. README.md 파일 생성
   - `echo "# $책 제목\n\n## 목차\n\n" > "$책 디렉토리 경로/README.md"`
3. 책 분류 기록
   - Root README.md 파일의 h3 섹션에 책 분류가 존재하는지 확인한다.
   - 존재하지 않는 경우, 책 분류 섹션을 추가한다.
   - 책 분류 섹션에 책 제목과 디렉토리 경로를 링크로 추가한다. (목록의 가장 뒤에 추가)
   - 예시:
     ```
     ### $책 분류
   
     - [$책 제목](./$책 디렉토리 경로) - (`🟡 읽는 중`)
     ```

## Exceptions

- 책 디렉토리가 이미 존재하는 경우 : "이미 '$책 제목' 책 디렉토리가 존재합니다." 라는 메시지를 출력하고, 책 디렉토리로 이동한다.
- 책 제목이나 분류가 입력되지 않은 경우 : "책 제목과 분류를 모두 입력해주세요." 라는 메시지를 출력하고 종료한다.

## Self-Check

- 책 디렉토리가 생성되었는가?
- 책 디렉토리 내에 README.md 파일이 생성되었는가?
- Root README.md 파일에 책 분류와 책 제목이 링크로 추가되었는가?

## Next Step

작업 완료 후 아래 메시지를 출력한다.

```
README.md에 목차를 작성한 뒤, 아래 명령어로 챕터 노트를 생성하세요:

/book-notes-create-chapter-note "$책 디렉토리 경로"
```
