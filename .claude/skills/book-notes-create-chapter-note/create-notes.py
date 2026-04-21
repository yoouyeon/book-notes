#!/usr/bin/env python3

import re
import sys
from pathlib import Path


def convert_filename(name):
    # 영숫자와 한글만 남기고 나머지는 하이픈으로 치환, 앞뒤 하이픈 제거
    filename = re.sub(r"[^a-zA-Z0-9가-힣]+", "-", name)
    return filename.strip("-")


def create_note(filepath, template_path, book_title, chapter_name):
    # 템플릿의 플레이스홀더를 실제 값으로 치환하여 노트 파일 생성
    template = template_path.read_text(encoding="utf-8")
    content = template.replace("$책 제목", book_title).replace(
        "$챕터 이름", chapter_name
    )
    filepath.write_text(content, encoding="utf-8")


def add_link_to_readme(readme_path, chapter_name, filename):
    content = readme_path.read_text(encoding="utf-8")

    # 이미 링크가 추가된 경우 스킵
    if f"({filename}.md)" in content:
        return

    # "- 챕터명" → "- [챕터명](./파일명.md)" 로 교체
    new_content = re.sub(
        r"^- " + re.escape(chapter_name) + r"$",
        f"- [{chapter_name}](./{filename}.md)",
        content,
        flags=re.MULTILINE,
    )
    readme_path.write_text(new_content, encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        print("책 디렉토리명을 입력해주세요.")
        sys.exit(1)

    book_dir = Path(sys.argv[1])
    readme_path = book_dir / "README.md"
    skill_dir = Path(__file__).parent
    template_path = skill_dir / "template.md"

    if not readme_path.exists():
        print(f"오류: '{readme_path}' 파일을 찾을 수 없습니다.")
        sys.exit(1)

    content = readme_path.read_text(encoding="utf-8")

    # README.md h1에서 책 제목 추출
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    book_title = title_match.group(1).strip() if title_match else ""

    # 목차에서 챕터 이름 추출: "- 챕터명" 형식만 처리 (이미 링크된 항목 제외)
    chapters = [
        m
        for m in re.findall(r"^- (.+)$", content, re.MULTILINE)
        if not m.startswith("[")
    ]

    for chapter in chapters:
        filename = convert_filename(chapter)
        filepath = book_dir / f"{filename}.md"

        if filepath.exists():
            print(f"Already exists: {filepath}")
        else:
            create_note(filepath, template_path, book_title, chapter)
            print(f"Created: {filepath}")

        add_link_to_readme(readme_path, chapter, filename)

    print("Done.")


if __name__ == "__main__":
    main()
