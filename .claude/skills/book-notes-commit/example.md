# Commit message examples

## book: 새로운 책 등록

Input:
- `git status` 결과: `new file: 면접을-위한-CS-전공지식-노트/README.md`
- README.md 내용: 책 제목과 목차만 있고 노트 파일 없음

Output:
```
book(면접을-위한-CS-전공지식-노트): 책 읽기 시작
```

## book: 목차 수정

Input:
- `git diff --cached` 결과: `면접을-위한-CS-전공지식-노트/README.md`의 목차 항목 변경

Output:
```
book(면접을-위한-CS-전공지식-노트): 목차 수정
```

## book: 완독

Input:
- `git diff --cached` 결과: 루트 `README.md`에서 책 상태가 `🟡 읽는 중` → `🟢 완독`으로 변경

Output:
```
book(코어-자바스크립트): 완독
```

## note: 챕터 노트 추가 (1개)

Input:
- `git status` 결과: `new file: 면접을-위한-CS-전공지식-노트/1-1-디자인-패턴.md`

Output:
```
note(면접을-위한-CS-전공지식-노트): 1-1 디자인 패턴 노트 추가
```

## note: 챕터 노트 추가 (여러 개)

Input:
- `git status` 결과:
  ```
  new file: 면접을-위한-CS-전공지식-노트/1-1-디자인-패턴.md
  new file: 면접을-위한-CS-전공지식-노트/1-2-프로그래밍-패러다임.md
  new file: 면접을-위한-CS-전공지식-노트/3-2-메모리.md
  ```

Output:
```
note(면접을-위한-CS-전공지식-노트): 1-1, 1-2, 3-2 챕터 노트 추가
```

## note: 노트 내용 수정

Input:
- `git diff --cached` 결과: `면접을-위한-CS-전공지식-노트/1-1-디자인-패턴.md` 본문 수정

Output:
```
note(면접을-위한-CS-전공지식-노트): 1-1 디자인 패턴 노트 수정
```

## skill: 스킬 파일 변경

Input:
- `git diff --cached` 결과: `.claude/skills/book-notes-commit/SKILL.md` 수정

Output:
```
skill(book-notes-commit): 커밋 메시지 규칙 수정
```

## skill: 새 스킬 추가

Input:
- `git status` 결과: `new file: .claude/skills/book-notes-review/SKILL.md`

Output:
```
skill(book-notes-review): 스킬 추가
```

## repo: 저장소 설정 변경

Input:
- `git status` 결과: `new file: .gitignore`, `modified: README.md`

Output:
```
repo: .gitignore 추가와 README 수정
```
