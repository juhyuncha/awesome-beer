# 기록 (결정·외부 반영)

## 2026-11-11
- **외부 반영:** GitHub에 `juhyuncha/awesome-beer` 포크 생성(공개, `resten1497/awesome-beer`에서). 근거: 사용자 답 "포크해서 정리 시작"
- **결정:** mahi97 포크(2025-12, 9커밋: 좌표 20건 위경도 교정, 영문 병기, 구글·카카오 지도 링크, `update-json.js`)를 fast-forward로 받아 기반으로 삼았다. 좌표 작업을 반복하지 않고 기여 이력을 남기기 위해서다.
- **결정:** 빌드를 Node(`src/*.js`, papaparse)에서 표준 라이브러리만 쓰는 Python(`scripts/build.py`)으로 옮기고 Node 스크립트와 `package.json`을 지웠다. 이 PC에 Node가 없고, 같은 출력을 내는 스크립트를 두 벌 두면 어긋나기 때문이다. 옮기기 전 CSV로 Python 빌드를 돌려 `beer.json`과 `data/*.md` 13개가 기존 파일과 바이트 단위로 같음을 확인했다.
- **데이터 정리**(224곳 → 223곳, `validate.py` 오류 56건 → 0건, 경고 1건):
  - 필드 앞뒤 공백 제거(주소 29건 등)
  - 주소 시도 표기 통일: 서울특별시·부산광역시·전라북도 → 서울·부산·전북. "맥" 주소에 빠진 "전주시"를 넣었다
  - 종류 정리: 공방 2곳과 한우돌곱창(" 곱창집")을 기타로 바꿨다
  - 위클리비어: 주소가 충남 천안이라 시도를 경기에서 충청으로 옮겼다
  - 화수브루어리 경주점 중복 삭제: 홈페이지만 다른 두 행 중 인스타그램 행을 남겼다(CONTRIBUTING이 인스타그램 권장)
  - 같은 이름의 다른 지점 4곳에 지점명을 붙였다
  - 플레이그라운드 네이버 URL 끝의 `?`를 지웠다
- **정정:** mahi97 변경을 받으려고 `upstream`·`mahi97` 원격을 추가했다가 지웠다. 개인 git 규칙이 juhyuncha 저장소 외의 원격 추가를 금지한다.
- **결정:** 이 저장소는 개인 git 규칙("juhyuncha 계정의 private 저장소만 쓴다")의 예외로 공개 상태를 유지한다. 공개 저장소의 포크는 GitHub에서 비공개로 바꿀 수 없고, 남과 공유하는 목록이라 공개가 맞다. 근거: 사용자 답 "3개로 커밋하고 이 저장소만 공개 예외로 둔다."
- **외부 반영:** `cleanup/data-2026` 브랜치(커밋 ae9309a, d61cf41, 0192fba 포함, master보다 12커밋 앞섬)를 origin에 push했다. master는 그대로다. 근거: 사용자 답 "push"
- **외부 반영:** 포크 안에서 PR [juhyuncha/awesome-beer#1](https://github.com/juhyuncha/awesome-beer/pull/1)(`cleanup/data-2026` → `master`)을 만들었다. 원본 저장소에는 보내지 않았다. 근거: 사용자 답 "PR 만들기"
- **외부 반영:** PR #1을 merge commit 방식으로 master에 병합했다(병합 커밋 9c75d4d, mahi97 커밋 이력 보존). 근거: 사용자 답 "병합"
- **외부 반영:** 기록 커밋 34162d0을 master에 push했다. 근거: 사용자 답 "push"(이 줄은 다음 커밋에 함께 올린다)
- **결정(2단계):** `beer.csv` 끝에 `status`(영업/폐업/미확인), `last_verified`(YYYY-MM-DD, 빈 값 허용) 열을 추가했다. 기존 223곳은 `미확인`, 몰티스 브루펍만 `폐업`. `beer.json`에는 `status`, `lastVerified`(빈 값은 `null`) 필드로 넣는다. `validate.py`는 허용값, 날짜 형식, 미래 날짜를 검사한다.
- **결정:** 몰티스 브루펍 설명의 "10/02 영업종료"를 지웠다. 근거: 사용자 답 "문구 지우기 (Recommended)"
- **결정:** 폐업한 곳은 `data/*.md`에서 빼고 `beer.json`에는 남긴다. 근거: 사용자 답 "md에서 빼기 (Recommended)"
- **정정:** `CONTRIBUTING.md` 입력 양식의 열 순서가 실제 CSV 헤더와 달랐다(주소·네이버 URL, 경도·위도 순서). 새 열을 넣으면서 실제 순서로 고쳤다.
- **결정:** 2단계 변경을 `feature/status-field` 브랜치에 커밋 두 개(필드 추가, 기록)로 나눠 커밋했다. push·PR은 하지 않았다. 근거: 사용자 답 "작업 트리 변경 사항을 적절한 메시지와 함께 커밋하세요."
- **외부 반영:** `feature/status-field` 브랜치(커밋 67d23aa, 3c6db87)를 origin에 push했다. master는 그대로다. 근거: 사용자 답 "push"(이 줄은 다음 커밋에 함께 올린다)
- **외부 반영:** 포크 안에서 PR [juhyuncha/awesome-beer#2](https://github.com/juhyuncha/awesome-beer/pull/2)(`feature/status-field` → `master`)를 만들었다. 원본 저장소에는 보내지 않았다. 근거: 사용자 답 "PR 만들기"
- **외부 반영:** PR #2를 merge commit 방식으로 master에 병합했다(병합 커밋 a1ea667). 근거: 사용자 답 "병합"
