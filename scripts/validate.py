"""beer.csv 형식 검사. 문제가 있으면 목록을 출력하고 종료 코드 1을 낸다.

    python scripts/validate.py
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent

HEADER = ["sidoNm", "name", "address", "beerType", "desc", "naverUrl", "homepage", "x", "y"]
TYPES = {"탭룸", "브루펍", "바틀샵", "기타"}
# 시도명 → 주소 첫 단어로 허용하는 값
SIDO = {
    "강원": {"강원"}, "경기": {"경기"}, "경상": {"경북", "경남"}, "광주": {"광주"},
    "대구": {"대구"}, "대전": {"대전"}, "부산": {"부산"}, "서울": {"서울"},
    "세종": {"세종"}, "울산": {"울산"}, "인천": {"인천"}, "전라": {"전북", "전남"},
    "제주": {"제주"}, "충청": {"충북", "충남"},
}
NAVER = re.compile(r"https://map\.naver\.com/v5/entry/place/\d+|https?://naver\.me/\w+")


def main():
    with open(ROOT / "beer.csv", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows = list(reader)

    errs = []
    if header != HEADER:
        errs.append(f"헤더가 다름: {header}")

    for i, r in enumerate(rows, start=2):  # 1행은 헤더
        tag = f"{i}행 {r['name']!r}"
        for k, v in r.items():
            if v != v.strip():
                errs.append(f"{tag}: {k} 앞뒤 공백")
        if r["sidoNm"] not in SIDO:
            errs.append(f"{tag}: 알 수 없는 시도 {r['sidoNm']!r}")
        elif r["address"].split()[:1] and r["address"].split()[0] not in SIDO[r["sidoNm"]]:
            errs.append(f"{tag}: 시도({r['sidoNm']})와 주소({r['address'].split()[0]}) 불일치")
        if r["beerType"] not in TYPES:
            errs.append(f"{tag}: 종류 {r['beerType']!r}는 {sorted(TYPES)} 중 하나여야 함")
        if r["naverUrl"] and not NAVER.fullmatch(r["naverUrl"]):
            errs.append(f"{tag}: 네이버 지도 URL 형식 {r['naverUrl']!r}")
        try:
            x, y = float(r["x"]), float(r["y"])
            if not (124 < x < 132 and 33 < y < 39):
                errs.append(f"{tag}: 좌표가 한국 범위 밖이거나 x(경도)·y(위도)가 바뀜 ({x}, {y})")
        except ValueError:
            errs.append(f"{tag}: 좌표가 숫자가 아님")

    for key in ("name", "naverUrl"):
        c = Counter(r[key] for r in rows if r[key])
        errs += [f"중복 {key}: {v!r} ({n}건)" for v, n in c.items() if n > 1]

    warn = [f"{i}행 {r['name']!r}: 네이버 지도 URL 없음" for i, r in enumerate(rows, 2) if not r["naverUrl"]]

    for w in warn:
        print("경고:", w)
    for e in errs:
        print("오류:", e)
    print(f"{len(rows)}곳 검사, 오류 {len(errs)}건, 경고 {len(warn)}건")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
