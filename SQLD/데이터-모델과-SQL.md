---
book: SQLD
status: draft
date:
title: "데이터 모델과 SQL"
category: ["SQLD"]
---

## 트랜잭션의 특성 : ACID

- A
- C
- Isolation (고립성) : 여러 트랜잭션이 서로 영향받지 않고 독립적으로 실행되어야 한다.
- D

## 3차 정규화

식별자를 제외한 일반 속성간 종속을 제거한다.

## `NULL`

`NULL`과 `NULL`은 비교할 수 없다.
`NULL=NULL`은 `UNKNOWN`을 반환한다.

`NULL`인지 확인하려면 `IS NULL`, `NULL`이 아닌지 확인하려면 `IS NOT NULL` 을 써야 한다.

WHERE 절은 TRUE인 것만 반환한다.
따라서 `WHERE NULL=NULL` 은 그냥 빈 값. 아무 행도 나오지 않는다.
