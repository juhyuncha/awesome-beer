# awesome-beer 에이전트 규칙

국내 수제맥주 가게 목록. 목표·범위·용어는 [docs/overview.md](docs/overview.md), 단계·상태·미결은 [docs/plan.md](docs/plan.md), 결정과 외부 반영 기록은 [docs/log.md](docs/log.md)에 둔다.

- 원본 데이터는 `beer.csv` 하나다. `beer.json`, `data/*.md`는 손으로 고치지 않고 `python scripts/build.py`로 만든다.
- `beer.csv`를 고치면 `python scripts/validate.py`(오류 0건)와 `python scripts/build.py`를 차례로 돌린 뒤 커밋한다.
- CSV는 UTF-8, 모든 필드 큰따옴표, CRLF 줄바꿈이다. 이 저장소는 `core.autocrlf=false`로 쓴다.
- 가게 정보(영업 여부, 영업시간 등)는 네이버·카카오 지도를 자동 수집하지 않는다(이용약관). 확인은 사람이 하고 `docs/plan.md`에 진행을 남긴다.
- 이 저장소는 공개 저장소다(개인 git 규칙의 private 원칙 예외, [docs/log.md](docs/log.md) 2026-11-11). 개인 정보·인증 정보가 들어가지 않게 한다.
- 원격은 `origin`(juhyuncha/awesome-beer) 하나만 둔다. 원본 `resten1497/awesome-beer`와 `mahi97/awesome-beer`는 필요할 때 URL로 직접 fetch하고 원격으로 등록하지 않는다. 그 저장소들에 PR·이슈를 사용자 확인 없이 만들지 않는다.
- push, PR, GitHub 설정 변경 같은 외부 반영은 하기 전에 확인받고, 한 뒤에는 바로 `docs/log.md`에 적는다.
