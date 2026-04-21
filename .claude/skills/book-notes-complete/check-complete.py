#!/usr/bin/env python3

import re
import sys
from pathlib import Path


def parse_frontmatter_status(filepath):
    # 파일의 frontmatter에서 status 값을 추출. frontmatter가 없거나 status가 없으면 None 반환.
    content = filepath.read_text(encoding="utf-8")

    # frontmatter는 파일 첫 줄이 "---"로 시작하고 다음 "---"로 닫혀야 함
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    frontmatter = match.group(1)

    # "status: <value>" 형식으로 추출
    status_match = re.search(r"^status:\s*(.+)$", frontmatter, re.MULTILINE)
    if not status_match:
        return None

    return status_match.group(1).strip()


def check_complete(book_dir):
    # 책 디렉토리 내 README.md를 제외한 모든 .md 파일의 status를 확인.
    # 모두 'completed'이면 True, 하나라도 아니면 False 반환.
    # 파일 목록과 각 상태도 함께 출력.

    md_files = [f for f in sorted(Path(book_dir).glob("*.md")) if f.name != "README.md"]

    if not md_files:
        print("노트 파일이 없습니다.")
        return False

    all_completed = True
    for filepath in md_files:
        status = parse_frontmatter_status(filepath)
        marker = "✓" if status == "completed" else "✗"
        print(f"  {marker} {filepath.name}: {status or '(status 없음)'}")
        if status != "completed":
            all_completed = False

    return all_completed


def main():
    if len(sys.argv) < 2:
        print("책 디렉토리명을 입력해주세요.")
        sys.exit(1)

    book_dir = Path(sys.argv[1])

    if not book_dir.exists():
        print(f"오류: '{book_dir}' 디렉토리를 찾을 수 없습니다.")
        sys.exit(1)

    print(f"[ {book_dir} ] 챕터 완료 상태 확인")
    result = check_complete(book_dir)
    print()
    print("true" if result else "false")


if __name__ == "__main__":
    main()
