# How to Contribute (기여방법)

- Check if the beer place is already in the list before adding.  
  (추가하기 전에 목록에 있는 맥주집인지 체크합니다.)
- Places like "Grandma Yeokjeon Beer" (traditional Korean pubs) cannot be added.  
  Only places that sell **craft beer** should be selected.  
  (역전할머니맥주와 같은 포차집은 추가할 수 없습니다. 반드시, **수제 맥주**를 판매 하는 곳을 기준으로 선정하여야합니다.)

- If there are multiple branches, please attach the branch name to the name. (ex: Art Monster **Gangnam Branch** / 아트몬스터 **강남점**)  
  (여러 분점이 있는 경우, 이름에 지점 명칭을 붙여주세요. (ex : 아트몬스터 **강남점**))

- Please add data in the following format to the last line of the `beer.csv` file.  
  (`beer.csv` 파일의 마지막 줄에 아래와 같은 규격으로 데이터를 추가해주세요.)

```
[시도명],[가게명],[도로명주소],[맥주집 종류],[설명],[네이버지도url],[홈페이지],[경도],[위도],[상태],[확인일]
[Region],[Store Name],[Street Address],[Beer Place Type],[Description],[Naver Map URL],[Homepage],[Longitude],[Latitude],[Status],[Last Verified]
```

- Status is one of 영업 (open), 폐업 (closed), 미확인 (unverified). Do not delete closed places; mark them 폐업.  
  (상태는 영업, 폐업, 미확인 중 하나입니다. 폐업한 곳은 지우지 말고 폐업으로 표시해주세요.)
- Last Verified is the date you checked the place yourself, in YYYY-MM-DD. Leave it empty if you have not checked.  
  (확인일은 직접 영업 여부를 확인한 날짜를 YYYY-MM-DD로 적습니다. 확인하지 않았으면 비워둡니다.)

## Input Format (입력 양식)

- Beer places are divided into the following categories:  
  (맥주집 종류는 크게 곳으로 나뉩니다.)
  - **Tap Room (탭룸)**: A place that sells beer without brewing it  
    (**탭룸** : 맥주를 양조하지 않고, 맥주를 판매하는곳)
  - **Brewpub (브루펍)**: A place with a beer brewing facility in the store  
    (Includes cases where the brewery is separate but the pub sells the beer)  
    (**브루펍** : 매장에 맥주를 양조하는 공장이 있는 곳 (양조장은 별개로 있고, 해당 펍에서 맥주를 판매하는 경우는 브루펍에 포함))
  - **Bottle Shop (바틀샵)**: A place that sells beer in bottles  
    (**바틀샵** : 맥주를 병으로 판매하는 곳)
  - **Other (기타)**: Places that don't fall into the above categories (e.g., workshops)  
    (**기타** : 위 범주에 들어가지 않는 곳 (공방 등))
- Please briefly write the characteristics of the store in the features section!  
  (Currently, there are many empty spots in features due to initial data entry)  
  (특징은 그 매장의 특징을 간단하게 적어주세요! (현재 초도데이터 입력으로 특징에 빈곳이 많습니다))

- For the homepage, please link to Instagram if possible, as most information is posted there.  
  (홈페이지는 보통 인스타그램에 많은 정보가 올라오므로, 가능하면 인스타그램의 링크를 걸어주세요.)

---

## Build (빌드)

After editing `beer.csv`, run the following with Python 3.9+ (no packages needed):  
(`beer.csv`를 고친 뒤 Python 3.9 이상으로 아래 명령을 실행해주세요. 따로 설치할 패키지는 없습니다.)

```bash
python scripts/validate.py   # Check the CSV format (CSV 형식 검사)
python scripts/build.py      # Regenerate beer.json and data/*.md (beer.json, data/*.md 재생성)
```

`beer.json` and `data/*.md` are generated files. Edit only `beer.csv`.  
(`beer.json`과 `data/*.md`는 생성 파일입니다. `beer.csv`만 고쳐주세요.)

Types must be one of 탭룸, 브루펍, 바틀샵, 기타.  
(종류는 탭룸, 브루펍, 바틀샵, 기타 중 하나여야 합니다.)

Thank you for contributing.  
(기여해주셔서 감사합니다.)
