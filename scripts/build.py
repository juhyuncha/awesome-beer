"""beer.csv에서 beer.json과 data/<시도>.md를 만든다.

beer.json에는 모든 가게를 넣고, data/*.md에는 폐업한 곳을 뺀다.
표준 라이브러리만 쓰므로 Python 3.9 이상이면 바로 돌아간다.

    python scripts/build.py              # 저장소 루트에 생성
    python scripts/build.py --out <dir>  # 다른 폴더에 생성(비교용)
"""
import argparse
import csv
import json
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent


def google(lat, lng):
    return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"


def kakao(lat, lng):
    return f"https://map.kakao.com/link/map/{lat},{lng}"


def load(csv_path):
    with open(csv_path, encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f) if (r.get("sidoNm") or "").strip()]


def to_md(r):
    s = f"#### [{r['name']}]({r['naverUrl']}) \n"
    s += f" - Address (주소): {r['address']}\n"
    s += f"- Type (종류): {r['beerType']}\n"
    s += f" - Features (특징): {r['desc']}\n"
    s += f"- Status (상태): {r['status']}"
    s += f" (확인일 {r['last_verified']})\n" if r["last_verified"] else "\n"
    if r["y"] and r["x"]:
        s += "- Maps (지도):\n"
        s += f"  - [Naver Map (네이버 지도)]({r['naverUrl']})\n"
        s += f"  - [Google Maps (구글 지도)]({google(r['y'], r['x'])})\n"
        s += f"  - [Kakao Map (카카오맵)]({kakao(r['y'], r['x'])})\n"
    if r["homepage"] != "":
        s += f"- [Homepage (홈페이지)]({r['homepage']})\n"
    return s


def to_json(r):
    has = bool(r["y"] and r["x"])
    return {
        "sidoNm": r["sidoNm"],
        "name": r["name"],
        "naverUrl": r["naverUrl"],
        "googleMapsUrl": google(r["y"], r["x"]) if has else "",
        "kakaoMapsUrl": kakao(r["y"], r["x"]) if has else "",
        "address": r["address"],
        "beerType": r["beerType"],
        "desc": r["desc"] or None,
        "homepage": r["homepage"],
        "x": r["x"],
        "y": r["y"],
        "status": r["status"],
        "lastVerified": r["last_verified"] or None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=ROOT / "beer.csv", type=Path)
    ap.add_argument("--out", default=ROOT, type=Path)
    a = ap.parse_args()

    rows = load(a.csv)
    data_dir = a.out / "data"
    if data_dir.exists():
        shutil.rmtree(data_dir)
    data_dir.mkdir(parents=True)

    by_sido = {}
    for r in rows:
        if r["status"] == "폐업":
            continue
        by_sido.setdefault(r["sidoNm"], []).append(to_md(r))
    for sido, parts in by_sido.items():
        (data_dir / f"{sido}.md").write_text("".join(parts), encoding="utf-8", newline="")

    (a.out / "beer.json").write_text(
        json.dumps([to_json(r) for r in rows], ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="",
    )
    shown = sum(len(v) for v in by_sido.values())
    print(f"{len(rows)}곳(md에는 폐업 제외 {shown}곳), 시도 {len(by_sido)}개 파일 생성")


if __name__ == "__main__":
    main()
