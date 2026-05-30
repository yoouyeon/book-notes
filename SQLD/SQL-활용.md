---
book: SQLD
status: completed
date: 2026-05-31T03:36:02+09:00
title: "SQL 활용"
category: ["SQLD"]
---

## 서브 쿼리

**서브쿼리 주의사항**

- 서브쿼리는 괄호로 감싸야 한다.
- 서브쿼리 내부에서는 `ORDER BY`를 사용할 수 없다. 단, `ORDER BY` 절 안에서 서브쿼리를 사용하는 것은 가능하다.
- 단일 행 비교 연산자는 서브쿼리의 결과가 반드시 1건 이하여야 사용할 수 있다.
- 다중 행 비교 연산자는 서브쿼리의 결과 건수와 관계없이 사용할 수 있다.
- 메인쿼리의 결과가 서브쿼리에 제공될 수도, 서브쿼리의 결과가 메인쿼리에 제공될 수도 있어 실행 순서는 상황에 따라 달라진다.

**반환 형태에 따른 서브쿼리 분류**

- **단일 행 서브쿼리** : 결과가 1건 이하. 단일 행 비교 연산자(`=`, `<`, `<=`, `>`, `>=`, `<>`)와 함께 사용한다.
- **다중 행 서브쿼리** : 결과가 여러 건. 다중 행 비교 연산자(`IN`, `ALL`, `ANY`, `SOME`, `EXISTS`)와 함께 사용한다.
- **단일 칼럼 서브쿼리** : 결과가 1개의 칼럼.
- **다중 칼럼 서브쿼리** : 결과가 여러 칼럼. 메인쿼리의 조건절에서 여러 칼럼을 동시에 비교할 수 있으며, 서브쿼리와 메인쿼리에서 비교하는 칼럼의 개수와 위치가 동일해야 한다. SQL Server에서는 지원하지 않는다.

```sql
deptno <> ANY (SELECT deptno FROM Emp)
-- Emp의 부서번호 목록 중 하나라도 내 deptno와 다른 값이 있으면 TRUE
```

**스칼라 서브쿼리(Scalar Subquery)** : 행마다 서브쿼리를 실행해서 하나의 값을 얻어낸다. 최종적으로 컬럼 하나를 반환하며, 값이 없으면 NULL을 반환한다.

```sql
SELECT <컬럼>, (SELECT LOC
                FROM DEPARTMENT D
                WHERE D.DEPT_ID = E.DEPT_ID)
FROM ...
```

**비연관 서브쿼리** : 메인쿼리의 칼럼을 포함하지 않는 서브쿼리. 주로 메인쿼리에 값을 제공하기 위한 목적으로 사용된다.

**상호 연관 서브쿼리(연관 서브쿼리)** : 서브쿼리가 메인쿼리의 칼럼을 포함하는 형태로, 메인쿼리의 행 수만큼 실행된다. 실행 속도가 상대적으로 떨어지지만, 복잡한 일반 배치 프로그램을 대체할 수 있다.

**INLINE VIEW** : FROM 절에 사용되는 서브쿼리. 실행 시에 동적으로 생성된 테이블처럼 사용할 수 있다.

**뷰(VIEW) 사용의 장점**

- **독립성** : 테이블 구조가 변경되더라도 뷰를 사용하는 응용 프로그램은 변경하지 않아도 된다.
- **편리성** : 복잡한 질의를 뷰로 생성해서 관련 질의를 단순하게 작성할 수 있다.
- **보안성** : 민감한 정보를 제외한 뷰를 생성하여 사용자에게 제공할 수 있다.

## 집합 연산자

**집합 연산자** : 두 개 이상의 SQL문의 결과를 조인 없이 결합할 때 사용한다.

- **`UNION`** : 합집합. 중복된 행은 하나로 합쳐 출력한다. 내부적으로 SORT가 발생하므로 성능 측면에서는 `UNION ALL`이 우수하다.
- **`UNION ALL`** : 합집합. 중복된 행도 그대로 출력한다. 각 SQL문의 결과가 상호 배타적일 때 `UNION`과 결과가 동일하다.
- **`INTERSECT`** : 교집합. 중복된 행은 하나로 합쳐 출력한다.
- **`EXCEPT`** : 차집합. 앞의 SQL문 결과에서 뒤의 SQL문 결과를 뺀다. 중복된 행은 하나로 합쳐 출력한다. Oracle에서는 `MINUS`를 사용한다.

**집합 연산자 사용 시 주의사항**

- `ORDER BY`는 최종 결과를 정렬하며, 가장 마지막 줄에 한 번만 사용할 수 있다.
- 위에 정의된 연산자가 먼저 수행된다.

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

**`ROLLUP(...)`** : 계층적인 소계와 총계를 구하는 문법. 왼쪽에서 오른쪽으로 단계적으로 접기 때문에 인자 순서에 따라 결과가 다르다. `ROLLUP(DEPTNO, JOB)`은 아래를 한 번에 구한다. `CUBE`와 인자가 1개일 때는 결과가 동일하지만, 인자가 2개 이상이면 결과가 달라질 수 있다.

```sql
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
-- 전체 집계
```

**GROUP BY 표현식별 집계 조합**

| 문법 | 출력되는 집계 조합 |
|---|---|
| `GROUPING SETS (grade, (job, grade))` | `(grade)`, `(job, grade)` |
| `ROLLUP (grade, job)` | `(grade, job)`, `(grade)`, `()` |
| `grade, ROLLUP (job)` | `(grade, job)`, `(grade)` |
| `grade, CUBE (job)` | `(grade, job)`, `(grade)` |

## 윈도우 함수

**`PARTITION BY`** : 특정 컬럼 값을 기준으로 계산 범위를 나누는 문법. `GROUP BY`는 여러 행을 하나의 집계 행으로 합치지만, `PARTITION BY`는 행을 줄이지 않고 원래 행을 유지한 채로 그룹별 집계를 계산한다. `PARTITION BY` 절이 없으면 전체 행을 대상으로 계산하며, 윈도우 함수의 적용 범위는 Partition을 넘을 수 없다.

**`WINDOWING` 절** : `OVER(...)` 안에서 윈도우 함수의 계산 대상 행 범위를 정한다. `WINDOWING` 절을 사용하려면 `ORDER BY`가 있어야 한다.

- **`UNBOUNDED PRECEDING`** : 맨 처음 행부터.
- **`CURRENT ROW`** : 현재 행까지.

**`RANK()`** : 동일한 값이 있으면 같은 순위를 부여하고 다음 순위를 건너뛴다. `ROW_NUMBER()`는 동일한 값이 있어도 고유한 순위를 부여한다.

**`DENSE_RANK()`** : 동일한 값이 있으면 같은 순위를 부여하고 다음 순위를 건너뛰지 않는다. SAL 100, 200, 200, 300일 때 RANK는 1, 2, 2, 4 (3을 건너뜀), DENSE_RANK는 1, 2, 2, 3 (건너뜀 없음).

**`PERCENT_RANK()`** : 순위를 0부터 1 사이의 값으로 표현한다.

**`CUME_DIST()`** : 현재 값 이하인 행이 전체에서 차지하는 누적 비율을 반환한다. SAL = 200일 때, 200 이하인 행이 5개 중 3개이므로 3 / 5 = 0.60.

**순위 함수 비교 예제**

```sql
SELECT ENAME, SAL,
       PERCENT_RANK() OVER (ORDER BY SAL) AS PERCENT_RANK,
       DENSE_RANK()   OVER (ORDER BY SAL) AS DENSE_RANK,
       CUME_DIST()    OVER (ORDER BY SAL) AS CUME_DIST,
       RANK()         OVER (ORDER BY SAL) AS RANK,
       RATIO_TO_REPORT(SAL) OVER ()       AS RATIO,
       NTILE(3)       OVER (ORDER BY SAL) AS NTILE
FROM EMP;
```

| ENAME | SAL | PERCENT_RANK | DENSE_RANK | CUME_DIST | RANK | RATIO | NTILE |
|---|---|---|---|---|---|---|---|
| A | 100 | 0.00 | 1 | 0.20 | 1 | 0.08 | 1 |
| B | 200 | 0.25 | 2 | 0.60 | 2 | 0.15 | 1 |
| C | 200 | 0.25 | 2 | 0.60 | 2 | 0.15 | 2 |
| D | 300 | 0.75 | 3 | 0.80 | 4 | 0.23 | 2 |
| E | 500 | 1.00 | 4 | 1.00 | 5 | 0.38 | 3 |

**`LAG(컬럼, 오프셋, 디폴트)`** : 현재 행 기준 이전 행의 값을 가져온다. 오프셋 기본값은 1, 디폴트 기본값은 NULL이다. SQL Server에서는 지원하지 않는다.

**`LEAD(컬럼, 오프셋, 디폴트)`** : 현재 행 기준 다음 행의 값을 가져온다. 오프셋 기본값은 1, 디폴트 기본값은 NULL이다.

**`NTILE(N)`** : 전체 데이터를 N개의 그룹으로 균등하게 나누고 각 행에 그룹 번호를 부여한다. 값의 크기가 아닌 행을 그룹으로 나누는 함수이므로 동일한 값의 행도 서로 다른 그룹에 들어갈 수 있다.

```sql
NTILE(4) OVER (ORDER BY SAL DESC)
-- SAL 내림차순으로 정렬한 데이터를 4등분
```

**`RATIO_TO_REPORT(컬럼) OVER (...)`** : Oracle 윈도우 함수. 전체 합계 또는 그룹별 합계에서 현재 행의 값이 차지하는 비율을 계산한다.

```sql
RATIO_TO_REPORT(컬럼) OVER (PARTITION BY 그룹기준)
```

## TOP N 쿼리

**`ROWNUM`** : SELECT 문에서 행이 인출될 때 순서대로 부여되는 일련번호. 1부터 시작한다. 조건으로 사용하려면 인라인 뷰 안에서 정렬 후 바깥에서 `ROWNUM`을 필터링해야 한다.

**TOP-N 서브쿼리** : INLINE VIEW의 정렬된 데이터를 `ROWNUM`으로 결과 행 수를 제한하는 서브쿼리.

**상위 N개 추출 방법**

1. 인라인 뷰로 정렬한 가상 테이블을 만든다 : `FROM (SELECT * FROM EMP ORDER BY SALARY DESC)`.
2. `WHERE ROWNUM <= N`으로 상위 N개를 추출한다.

**`TOP(N) WITH TIES`** : SQL Server에서 사용하는 문법. 동일한 값이 있는 경우 N개를 초과하더라도 함께 출력한다.

## 계층형 질의와 셀프 조인

**셀프 조인** : 동일 테이블을 FROM 절에 두 번 이상 사용하는 조인. 테이블과 칼럼 이름이 모두 동일하기 때문에 반드시 테이블 ALIAS를 사용해야 한다.

```sql
SELECT A.칼럼명, B.칼럼명
FROM 테이블 A, 테이블 B
WHERE A.칼럼명 = B.칼럼명;
```

**`CONNECT BY`** : 한 테이블 안에서 부모-자식 관계를 반복해서 따라가는 Oracle 계층형 질의 문법.

```sql
SELECT 컬럼, LEVEL
FROM 테이블
START WITH 최상위_조건
CONNECT BY PRIOR 기본키 = 부모키;
```

- **`START WITH`** : 계층 탐색의 시작점 조건.
- **`CONNECT BY`** : 부모와 자식을 연결하는 규칙.
- **`PRIOR`** : `CONNECT BY` 절에서 이전 단계 행의 칼럼임을 표시한다. `PRIOR PK = FK`는 부모에서 자식으로 내려가는 순방향 전개, `PRIOR FK = PK`는 자식에서 부모로 올라가는 역방향 전개를 한다.

**`ORDER SIBLINGS BY`** : 전체 결과를 재정렬하지 않고, 같은 부모를 가진 자식들끼리만 정렬한다.

```sql
ORDER SIBLINGS BY 컬럼 ASC
ORDER SIBLINGS BY 컬럼 DESC
```

**가상 칼럼**

- **`LEVEL`** : 계층의 깊이. 루트 노드는 1.
- **`CONNECT_BY_ISLEAF`** : 현재 행이 리프 노드이면 1, 아니면 0.

## PIVOT 절과 UNPIVOT 절

**`UNPIVOT`** : 열을 행으로 전환하는 연산.

## 정규 표현식

**정규 표현식 기본 문자**

- **`^`** : 문자열의 시작.
- **`$`** : 문자열의 끝.

**`^[A-Z].*[0-9]$`** : 대문자 알파벳으로 시작하고 숫자로 끝나는 문자열.

**`REGEXP_LIKE`** : `LIKE`는 단순한 와일드카드만 지원하므로, 복잡한 문자열 패턴 매칭이 필요한 경우 `LIKE` 대신 사용한다.
