---
book: SQLD
status: draft
date:
title: "데이터 모델과 SQL"
category: ["SQLD"]
---

## 정규화

### 3차 정규화

식별자를 제외한 일반 속성간 종속을 제거한다.

### 반정규화

테이블 반정규화, 칼럼 반정규화는 데이터 무결성에 영향을 미친다.

관계의 반정규화 기법 중 중복 관계 추가는 데이터 무결성을 깨뜨릴 위험을 갖지 않으면서도 데이터 처리의 성능을 향상시킬 수 있다.

관계의 반정규화가 유용한 경우 ⇒ 데이터 모델 전체가 관계로 연결되어 있고, 관계가 서로 먼 친척 간에 조인 관계가 빈번하게 되어 성능저하가 예상되는 경우

## 모델이 표현하는 트랜잭션의 이해

### 트랜잭션의 특성 : ACID

- A
- C
- Isolation (고립성) : 여러 트랜잭션이 서로 영향받지 않고 독립적으로 실행되어야 한다.
- D

## Null 속성의 이해

### `NULL`

`NULL`과 `NULL`은 비교할 수 없다.
`NULL=NULL`은 `UNKNOWN`을 반환한다.

`NULL`인지 확인하려면 `IS NULL`, `NULL`이 아닌지 확인하려면 `IS NOT NULL` 을 써야 한다.

WHERE 절은 TRUE인 것만 반환한다.
따라서 `WHERE NULL=NULL` 은 그냥 빈 값. 아무 행도 나오지 않는다.

NULL에 뭔가를 연산해도 그 결과는 NULL이다.

```sql
-- 이 SELECT 문은 모두
SELECT NULL * 2
SELECT NULL * 3
SELECT NULL * NULL
SELECT NULL + 100

SELECT NULL -- 이거랑 같음 SELECT NULL은 NULL을 반환한다.
```

### SQL Server와 Oracle의 `NULL` 인덱스 저장

SQL Server는 null 값을 인덱스 맨 앞에 저장한다.
Oracle은 맨 뒤에 저장한다.

SQL Server는 인덱스 구성 칼럼이 모두 null인 레코드도 인덱스에 저장한다.
Oracle에서 인덱스 구성 칼럼 중 하나라도 null이 아닌 레코드만 인덱스에 저장한다.
