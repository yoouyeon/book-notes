---
book: SQLD
status: draft
date:
title: "SQL 활용"
category: ["SQLD"]
---

## 서브쿼리

### Scala Subquery

Scala Subquery (스칼라 서브쿼리) : 행마다 서브쿼리를 실행해서 하나의 값을 얻어낸다. 최종적으로 컬럼 하나를 반환함.

### SELECT 절에서 사용되는 스칼라 서브쿼리

```sql
SELECT <어쩌고> (SELECT LOC
FROM DEPARTMENT D
WHERE D.DEPT_ID=E.DEPT_ID)
```

`()` 안이 바로 스칼라 서브쿼리
DEPARTMENT 테이블의 모든 행에서 해당 구문이 실행되는 것. 그리고 하나의 값을 반환한다. 없으면 NULL을 반환한다.

### 상호 연관 서브쿼리

서브쿼리가 메인쿼리의 행 수 만큼 실행되는 쿼리.
따라서 실행 속도가 상대적으로 떨어진다.
복잡한 일반 배치 프로그램을 대체할 수 있어 조건에 맞는다면 유용하다.

### INLINE VIEW

INLINE VIEW : FROM 절에 사용되는 서브쿼리. SQL문에서 VIEW나 테이블처럼 사용되는 서브쿼리

### 다중행 연산자

IN, ANY, ALL : 다중행 연산자. 서브쿼리의 결과로 하나 이상의 데이터가 RETURN되는 서브쿼리

## 그룹 함수

### `CUBE`

`CUBE` : 그룹함수

제시된 칼럼에 대해서 결합 가능한 모든 집계를 계산한다.

일반 `GROUP BY` : `GROUP BY DEPTNO, JOB`

```
DEPTNO | JOB      | COUNT(*)
-------+----------+---------
10     | CLERK    | 1
10     | MANAGER  | 1
20     | CLERK    | 2
20     | ANALYST  | 2
```

`CUBE(DEPTNO, JOB)`은 아래 네 가지를 전부 만든다.

```sql
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
GROUP BY JOB
GROUP BY ()
```

```
DEPTNO | JOB      | COUNT(*)
-------+----------+---------
10     | CLERK    | 1      -- 부서+직무별
10     | MANAGER  | 1      -- 부서+직무별
20     | CLERK    | 2      -- 부서+직무별
20     | ANALYST  | 2      -- 부서+직무별

10     | NULL     | 2      -- 부서별 소계
20     | NULL     | 4      -- 부서별 소계

NULL   | CLERK    | 3      -- 직무별 소계
NULL   | MANAGER  | 1      -- 직무별 소계
NULL   | ANALYST  | 2      -- 직무별 소계

NULL   | NULL     | 6      -- 전체 합계
```

### `GROUP BY GROUPING SETS (...)`

`GROUP BY GROUPING SETS (...)`는 내가 원하는 집계 기준들을 직접 골라서 나열하는 문법

```sql
GROUP BY GROUPING SETS (
  DEPTNO,
  JOB,
  (DEPTNO, JOB),
  ()
);
```

아래 4개의 `GROUP BY`를 한 번에 실행하는 것과 같다

```sql
GROUP BY DEPTNO
GROUP BY JOB
GROUP BY DEPTNO, JOB
전체 집계
```

### `GROUP BY ROLLUP( … )`

`GROUP BY ROLLUP( … )` 은 계층적인 소계와 총계를 구하는 문법

`GROUP BY ROLLUP(DEPTNO, JOB)` 은 아래 집계를 한번에 구하는 것과 같다.

```sql
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
전체 집계
```

중요한 것은 왼쪽에서 오른쪽으로 단계적으로 접는다는 것. 그래서 인자 순서에 따라서 결과가 다르다.

`ROLLUP(DEPTNO, JOB)` 이면

- (DEPTNO, JOB)
- (DEPTNO)
- ()

`ROLLUP(JOB, DEPTNO)` 이면

- (JOB, DEPTNO)
- (JOB)
- ()

## 윈도우 함수

### `RANK`

`RANK` : 순위를 구하는 윈도우 함수

### `NTILE(ARGUMENT)`

`NTILE(ARGUMENT)` : 윈도우함수. 데이터를 `ARGUMENT` 값으로 등분한다.

`OVER()` : 윈도우함수 적용 기준을 정하는 문법

```sql
NTILE(4) OVER (ORDER BY SAL DESC)
```

- `NTILE(4)` : 데이터를 4등분 할것임 → 어떤 기준으로 등분할건데?
-  `OVER (ORDER BY SAL DESC)` : SAL을 내림차순 정렬한 데이터를

## Top N 쿼리

### `ROWNUM`

`ROWNUM`은 1부터 시작한다.
`ROWNUM 1` 이란 첫번째 행을 의미하는 것.

### TOP-N 서브쿼리

TOP-N 서브쿼리 : INLINE VIEW의 정렬된 데이터를 ROWNUM을 이용해서 결과 행 수를 제한하거나 TOP(N) 조건을 사용하는 서브쿼리

## 계층형 질의와 셀프 조인

### `PRIOR`

`PRIOR`

- `WHERE` 절과 함께 쓸 수 없다.
- `PRIOR` 가 **하위 계층(자식 컬럼)**에 붙으면 **순방향 전개**
- `PRIOR` 가 **상위 계층(부모 컬럼)**에 붙으면 **역방향 전개**

## 정규 표현식

### 정규표현식

`^`는 시작, `$`는 끝.
`^[AZ].*[0-9]$` 는 대문자 알파벳으로 시작하고 숫자로 끝나는 문자열을 의미함.

Oracle에서는 `LIKE`는 단순한 와일드카드만 지원하기 때문에 복잡한 문자열 패턴 매칭이 필요한 경우에는 `REGEXP_LIKE`를 사용해야 한다.
