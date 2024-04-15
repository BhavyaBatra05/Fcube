let state;
var data = window.location.search;
let inp = new URLSearchParams(data);
const wlcm = document.querySelector(".aa");
let name_val = inp.get("names");
let phone_val = inp.get("phones");
let mail_val = inp.get("mails");
let address_val = inp.get("add");
const name_a = document.querySelector(".name");
const phone = document.querySelector(".phone");
const mail = document.querySelector(".mail");
const address = document.querySelector(".address");
const password = document.querySelector(".password");
wlcm.textContent = name_val;
name_a.textContent = "Name: " + name_val;
phone.textContent = "Phone no.: " + phone_val;
mail.textContent = "E-mail: " + mail_val;
address.textContent = "Address: " + address_val;
let map_srch_value;
let ind;
const states = [
  "Punjab",
  "Haryana",
  "Rajasthan",
  "Uttar Pradesh",
  "Madhya Pradesh",
  "Gujarat",
  "Maharashtra",
  "Andhra Pradesh",
  "Karnataka",
  "Kerala",
  "Tamil Nadu",
  "Tripura",
  "Assam",
  "Meghalaya",
  "Odisha",
];
const punjab_dist = [
  "Hoshiarpur",
  "Jalandhar",
  "Kapurthala",
  "Mansa",
  "Nawanshahr",
  "Sangrur",
  "Tarntaran",
];
const map_srch = document.querySelector(".a44");
const map_result = document.querySelector(".a2");
const maps = document.querySelectorAll(".a3");
const temp = document.querySelector(".temp");
const locate = document.querySelector(".loc");
const humid = document.querySelector(".humidity");
const rain = document.querySelector(".rain");
const district = document.querySelector(".district");
const district_input = document.querySelector(".dist-input");
const district_button = document.querySelector(".dist-btn");
const soil_input = document.querySelector(".soil-input");
const soil = document.querySelector(".soil");
// -------------------------------------------------------------------------------------

function disp_no() {
  maps.forEach((x) => {
    x.style.display = "none";
  });
}
const get_temp = async (state) => {
  const rough = await fetch(
    `https://api.weatherapi.com/v1/current.json?key=154148064fd54ddc87f193551241404&q=${state}`
  );
  console.log(rough);

  const final = await rough.json();
  console.log(final);
  return [
    final.current.temp_c,
    final.current.humidity,
    final.current.precip_mm,
  ];
};
function getlist() {
  if (map_srch.value !== null) {
    map_srch_value = map_srch.value;
    if (map_srch_value === "Punjab") {
      district_input.setAttribute("list", "datalistOptionspunjab");
      soil_input.setAttribute("list", "datalistOptionsoilpunjab");
    }
  }
}

// -------------------------------------------------------------------------------------

map_result.addEventListener("click", async () => {
  if (map_srch.value !== null) {
    map_srch_value = map_srch.value;
    ind = states.findIndex((x) => x == map_srch_value);
    disp_no();
    maps[ind].style.display = "inline";
    let state = states[ind];
    locate.textContent = "Location: " + states[ind];
    const tem = await get_temp(state);
    temp.textContent = "Temperature: " + tem[0] + " °C";
    humid.textContent = "Humidity: " + tem[1] + "g.kg-1 ";
    rain.textContent = "Rain: " + tem[2];
    if (state == "Punjab") {
      district.style.display = "flex";
      soil.style.display = "flex";
    }
    getlist();
  } else {
    console.log("NO DATA WAS PRESENT IN THE SEARCH INPUT!!!!");
    temp.textContent = "PLEASE SELECT STATE FIRST!!";
  }
});

// district_button.addEventListener(("click"=>{

// }))
