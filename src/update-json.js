const Papa = require("papaparse");
const fs = require("fs");

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
  const dataStream = fs.readFileSync("beer.csv", { encoding: "utf-8" });
  const results = Papa.parse(dataStream, { header: true });
  
  console.log("📝 Updating JSON with map links...");
  
  const breweries = results.data
    .filter(brewery => brewery.sidoNm !== undefined && brewery.sidoNm !== "")
    .map(brewery => ({
      sidoNm: brewery.sidoNm,
      name: brewery.name,
      naverUrl: brewery.naverUrl,
      googleMapsUrl: hasValidCoordinates(brewery.y, brewery.x) ? getGoogleMapsLink(brewery.y, brewery.x) : "",
      kakaoMapsUrl: hasValidCoordinates(brewery.y, brewery.x) ? getKakaoMapsLink(brewery.y, brewery.x) : "",
      address: brewery.address,
      beerType: brewery.beerType,
      desc: brewery.desc || null,
      homepage: brewery.homepage,
      x: brewery.x,
      y: brewery.y
    }));
  
  fs.writeFileSync("beer.json", JSON.stringify(breweries, null, 2), { encoding: "utf-8" });
  
  console.log("✅ JSON file updated successfully!");
  console.log(`Total entries: ${breweries.length}`);
} catch (e) {
  console.log("❌ JSON update failed!");
  console.log(e);
}
