---
book: SQLD
status: draft
date:
title: "SQL 활용"
category: ["SQLD"]
---

## `RANK`

`RANK` : 순위를 구하는 윈도우 함수

## `PRIOR`

`PRIOR`

- `WHERE` 절과 함께 쓸 수 없다.
- `PRIOR` 가 **하위 계층(자식 컬럼)**에 붙으면 **순방향 전개**
- `PRIOR` 가 **상위 계층(부모 컬럼)**에 붙으면 **역방향 전개**

## `ROWNUM`

`ROWNUM`은 1부터 시작한다.
`ROWNUM 1` 이란 첫번째 행을 의미하는 것.

## Scala Subquery

Scala Subquery (스칼라 서브쿼리) : 행마다 서브쿼리를 실행해서 하나의 값을 얻어낸다. 최종적으로 컬럼 하나를 반환함.

## SELECT 절에서 사용되는 스칼라 서브쿼리

```sql
SELECT <어쩌고> (SELECT LOC
FROM DEPARTMENT D
WHERE D.DEPT_ID=E.DEPT_ID)
```

`()` 안이 바로 스칼라 서브쿼리
DEPARTMENT 테이블의 모든 행에서 해당 구문이 실행되는 것. 그리고 하나의 값을 반환한다. 없으면 NULL을 반환한다.

## `NTILE(ARGUMENT)`

`NTILE(ARGUMENT)` : 윈도우함수. 데이터를 `ARGUMENT` 값으로 등분한다.

`OVER()` : 윈도우함수 적용 기준을 정하는 문법

```sql
NTILE(4) OVER (ORDER BY SAL DESC)
```

- `NTILE(4)` : 데이터를 4등분 할것임 → 어떤 기준으로 등분할건데?
-  `OVER (ORDER BY SAL DESC)` : SAL을 내림차순 정렬한 데이터를
