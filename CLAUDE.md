# Book notes 레포지토리 맥락

## 개요

책을 읽고 공부한 내용을 정리하는 개인 학습 프로젝트

## 디렉토리 구조

```
book-notes/
├── README.md
├── CLAUDE.md
├── 책 이름/
│   ├── README.md
│   ├── 챕터 제목.md
│   └── ...
```

## 공부 흐름

1. `book-notes-setup-workspace` skill : 책 이름과 분류를 입력받아 책 디렉토리를 생성하고 하위에 README.md 파일을 생성
2. `book-notes-create-chapter-note` skill : 책 디렉토리의 README.md 파일의 목차를 읽어 챕터 제목에 해당하는 노트 파일을 생성
3. 사용자가 책을 읽고 공부한 내용을 노트 파일에 기록
4. `book-notes-review` skill : 정리한 노트를 읽고 오타를 수정하고 사실과 다른 내용을 확인하여 사용자에게 제안 (내용 수정은 사용자가 직접 수행)
5. `book-notes-complete` skill : 책 디렉토리의 모든 노트 파일의 status를 확인하고, 완료한 경우 루트 README.md 파일에 완료 표시를 추가

## 유틸리티 스킬

- `book-notes-commit` : stage된 변경사항에 해당하는 커밋 메시지를 생성하여 커밋

## 상태 관리

- 책 상태 : 루트 README.md 파일에서 `🟡 읽는 중`, `🟢 완독`으로 상태 표시
- 노트 상태 : 각 노트 파일 frontmatter의 `status` 필드에서 `draft`, `reviewed`, `completed`로 상태 표시
