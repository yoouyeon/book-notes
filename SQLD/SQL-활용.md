---
book: SQLD
status: draft
date:
title: "SQL 활용"
category: ["SQLD"]
---

## 서브 쿼리

**스칼라 서브쿼리(Scalar Subquery)** : 행마다 서브쿼리를 실행해서 하나의 값을 얻어낸다. 최종적으로 컬럼 하나를 반환하며, 값이 없으면 NULL을 반환한다.

```sql
SELECT <컬럼>, (SELECT LOC
                FROM DEPARTMENT D
                WHERE D.DEPT_ID = E.DEPT_ID)
FROM ...
```

**상호 연관 서브쿼리** : 서브쿼리가 메인쿼리의 행 수만큼 실행되는 쿼리. 실행 속도가 상대적으로 떨어지지만, 복잡한 일반 배치 프로그램을 대체할 수 있다.

**INLINE VIEW** : FROM 절에 사용되는 서브쿼리. SQL문에서 VIEW나 테이블처럼 사용된다.

**ORDER BY 절의 서브쿼리** : 서브쿼리는 ORDER BY 절에서 사용할 수 있다.

**다중행 연산자** : `IN`, `ANY`, `ALL`. 서브쿼리의 결과로 하나 이상의 데이터가 반환되는 경우에 사용한다.

```sql
deptno <> ANY (SELECT deptno FROM Emp)
-- Emp의 부서번호 목록 중 하나라도 내 deptno와 다른 값이 있으면 TRUE
```

## 집합 연산자

**집합 연산자** : 두 개 이상의 테이블에서 조인을 하지 않고 관련된 데이터를 조회할 때 사용한다.

- `UNION ALL`
- `UNION`
- `EXCEPT`

**`UNION` vs `UNION ALL`** : `UNION`은 내부적으로 SORT가 발생하기 때문에 성능 측면에서는 `UNION ALL`이 우수하다.

## 그룹 함수

**`CUBE`** : 제시된 컬럼에 대해 결합 가능한 모든 집계를 계산한다. `CUBE(DEPTNO, JOB)`은 아래 네 가지를 전부 계산한다.

```sql
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
GROUP BY JOB
GROUP BY ()        -- 전체 합계
```

**`GROUPING SETS(...)`** : 원하는 집계 기준들을 직접 지정해서 나열하는 문법.

```sql
GROUP BY GROUPING SETS (DEPTNO, JOB, (DEPTNO, JOB), ())
```

- `GROUPING SETS(A, B)` → `GROUP BY A` + `GROUP BY B`
- `GROUPING SETS((A, B), A)` → `GROUP BY A, B` + `GROUP BY A`

**`ROLLUP(...)`** : 계층적인 소계와 총계를 구하는 문법. 왼쪽에서 오른쪽으로 단계적으로 접기 때문에 인자 순서에 따라 결과가 다르다. `ROLLUP(DEPTNO, JOB)`은 아래를 한 번에 구한다.

```sql
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
-- 전체 집계
```

## 윈도우 함수

**`PARTITION BY`** : 특정 컬럼 값을 기준으로 계산 범위를 나누는 문법. `GROUP BY`처럼 행을 줄이지 않고 원래 행을 유지한 채로 그룹별 집계를 계산한다. `PARTITION BY` 절이 없으면 전체 행을 대상으로 계산한다.

**`WINDOWING` 절** : `OVER(...)` 안에서 윈도우 함수의 계산 대상 행 범위를 정한다. `WINDOWING` 절을 사용하려면 `ORDER BY`가 있어야 한다.

- **`UNBOUNDED PRECEDING`** : 맨 처음 행부터.
- **`CURRENT ROW`** : 현재 행까지.

**`RANK()`** : 순위를 구하는 윈도우 함수. 동일한 값이 있으면 동일한 순위를 부여하고 다음 순위를 건너뛴다. `ROW_NUMBER()`는 동일한 값이 있어도 고유한 순위를 부여한다.

**`LAG(컬럼, 오프셋, 디폴트)`** : 현재 행 기준 이전 행의 값을 가져온다. 오프셋 기본값은 1, 디폴트 기본값은 NULL이다.

**`LEAD(컬럼, 오프셋, 디폴트)`** : 현재 행 기준 다음 행의 값을 가져온다. 오프셋 기본값은 1, 디폴트 기본값은 NULL이다.

**`NTILE(N)`** : 전체 데이터를 N개의 그룹으로 균등하게 나누고 각 행에 그룹 번호를 부여한다.

```sql
NTILE(4) OVER (ORDER BY SAL DESC)
-- SAL 내림차순으로 정렬한 데이터를 4등분
```

## TOP N 쿼리

**`ROWNUM`** : SELECT 문에서 행이 인출될 때 순서대로 부여되는 일련번호. 1부터 시작한다. 조건으로 사용하려면 인라인 뷰 안에서 정렬 후 바깥에서 `ROWNUM`을 필터링해야 한다.

**TOP-N 서브쿼리** : INLINE VIEW의 정렬된 데이터를 `ROWNUM`으로 결과 행 수를 제한하는 서브쿼리.

**상위 N개 추출 방법**

1. 인라인 뷰로 정렬한 가상 테이블을 만든다 : `FROM (SELECT * FROM EMP ORDER BY SALARY DESC)`.
2. `WHERE ROWNUM <= N`으로 상위 N개를 추출한다.

## 계층형 질의와 셀프 조인

**`PRIOR`**

- `WHERE` 절과 함께 쓸 수 없다.
- `PRIOR`가 자식 컬럼에 붙으면 순방향 전개.
- `PRIOR`가 부모 컬럼에 붙으면 역방향 전개.

**`CONNECT_BY_ISLEAF`** : Oracle 계층형 쿼리에서 현재 행이 리프 노드인지 여부를 나타내는 가상 컬럼. 1이면 리프 노드, 0이면 리프 노드가 아니다.

## PIVOT 절과 UNPIVOT 절

**`UNPIVOT`** : 열을 행으로 전환하는 연산.

## 정규 표현식

**정규 표현식 기본 문자**

- **`^`** : 문자열의 시작.
- **`$`** : 문자열의 끝.

`^[AZ].*[0-9]$` : 대문자 알파벳으로 시작하고 숫자로 끝나는 문자열

**`REGEXP_LIKE`** : `LIKE`는 단순한 와일드카드만 지원하므로, 복잡한 문자열 패턴 매칭이 필요한 경우 `LIKE` 대신 사용한다.
