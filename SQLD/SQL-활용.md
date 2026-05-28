---
book: SQLD
status: draft
date:
title: "SQL 활용"
category: ["SQLD"]
---

## 정규표현식

`^`는 시작, `$`는 끝.
`^[AZ].*[0-9]$` 는 대문자 알파벳으로 시작하고 숫자로 끝나는 문자열을 의미함.

Oracle에서는 `LIKE`는 단순한 와일드카드만 지원하기 때문에 복잡한 문자열 패턴 매칭이 필요한 경우에는 `REGEXP_LIKE`를 사용해야 한다.

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

## 상호 연관 서브쿼리

서브쿼리가 메인쿼리의 행 수 만큼 실행되는 쿼리.
따라서 실행 속도가 상대적으로 떨어진다.
복잡한 일반 배치 프로그램을 대체할 수 있어 조건에 맞는다면 유용하다.

## TOP-N 서브쿼리

TOP-N 서브쿼리 : INLINE VIEW의 정렬된 데이터를 ROWNUM을 이용해서 결과 행 수를 제한하거나 TOP(N) 조건을 사용하는 서브쿼리

## INLINE VIEW

INLINE VIEW : FROM 절에 사용되는 서브쿼리. SQL문에서 VIEW나 테이블처럼 사용되는 서브쿼리

## 다중행 연산자

IN, ANY, ALL : 다중행 연산자. 서브쿼리의 결과로 하나 이상의 데이터가 RETURN되는 서브쿼리

## `NTILE(ARGUMENT)`

`NTILE(ARGUMENT)` : 윈도우함수. 데이터를 `ARGUMENT` 값으로 등분한다.

`OVER()` : 윈도우함수 적용 기준을 정하는 문법

```sql
NTILE(4) OVER (ORDER BY SAL DESC)
```

- `NTILE(4)` : 데이터를 4등분 할것임 → 어떤 기준으로 등분할건데?
-  `OVER (ORDER BY SAL DESC)` : SAL을 내림차순 정렬한 데이터를
