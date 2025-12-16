const Papa = require("papaparse");
const fs = require("fs");
const dataStream = fs.readFileSync("beer.csv", { encoding: "utf-8" });
const fsExtra = require("fs-extra");

// Function to generate Google Maps link from coordinates
function getGoogleMapsLink(lat, lng) {
  return `https://www.google.com/maps/search/?api=1&query=${lat},${lng}`;
}

// Function to generate Kakao Maps link from coordinates
function getKakaoMapsLink(lat, lng) {
  return `https://map.kakao.com/link/map/${lat},${lng}`;
}

// Function to check if coordinates are valid
function hasValidCoordinates(y, x) {
  return y && x;
}

try {
  const results = Papa.parse(dataStream, { header: true });

  fsExtra.emptyDirSync("./data/");
  console.log("✂️ 데이터 분할중 (Splitting data)... ");

  const breweries = results.data;
  let validCount = 0;
  
  for (let brewery of breweries) {
    let { sidoNm } = brewery;
    // Skip entries without a valid region name
    if (!sidoNm || sidoNm.trim() === '') continue;
    
    validCount++;
    let sidoNmPath = `./data/${sidoNm}.md`;
    let data = `#### [${brewery.name}](${brewery.naverUrl}) \n`;
    data += ` - Address (주소): ${brewery.address}\n`;
    data += `- Type (종류): ${brewery.beerType}\n`;
    data += ` - Features (특징): ${brewery.desc}\n`;
    
    // Add map links
    if (hasValidCoordinates(brewery.y, brewery.x)) {
      data += `- Maps (지도):\n`;
      data += `  - [Naver Map (네이버 지도)](${brewery.naverUrl})\n`;
      data += `  - [Google Maps (구글 지도)](${getGoogleMapsLink(brewery.y, brewery.x)})\n`;
      data += `  - [Kakao Map (카카오맵)](${getKakaoMapsLink(brewery.y, brewery.x)})\n`;
    }
    
    if (brewery.homepage != "") {
      data += `- [Homepage (홈페이지)](${brewery.homepage})\n`;
    }

    fs.appendFileSync(sidoNmPath, data);
  }

  console.log("👍 데이터 분할 완료! (Data splitting complete!)");
  console.log("총 (Total) " + validCount + " 개의 데이터를 분할했습니다. (data entries split)");
} catch (e) {
  console.log("❌ 데이터 분할 실패! (Data splitting failed!)");
  console.log(e);
}
