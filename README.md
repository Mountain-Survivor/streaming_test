# streaming_test

## 목적

스트리밍 출력과 일괄 출력의 첫 결과 도착 시간 및 전체 완료 시간을 비교하기 위해 만든 프로젝트이다.

## 실행 방법

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install fastapi uvicorn
uvicorn main:app --reload --port 8002
```

Codespaces의 PORTS 탭에서 8002 포트를 브라우저로 연다.

## 실험 결과

- `async def` 안에서 `time.sleep(5)`를 실행하면 이벤트 루프가 막혀 스트리밍 요청도 지연된다.
- `await asyncio.sleep(5)`는 대기 중 제어권을 돌려주므로 다른 요청이 진행될 수 있다.
- `await asyncio.to_thread(batch_model)`은 동기 함수를 별도 스레드에서 실행해 이벤트 루프의 막힘을 피한다.

| 일괄 응답 구현 | 스트리밍 첫 데이터 | 스트리밍 완료 | 일괄 응답 완료 |
|---|---:|---:|---:|
| `async def` + `time.sleep()` | 6.20초 | 10.21초 | 5.20초 |
| `await asyncio.sleep()` | 1.38초 | 5.39초 | 5.28초 |
| `await asyncio.to_thread()` | 1.48초 | 5.49초 | 5.47초 |

시간은 Codespaces 환경에서 각 방식을 한 번씩 측정한 값이며, 네트워크 상태에 따라 달라질 수 있다.
