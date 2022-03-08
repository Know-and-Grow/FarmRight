var state_arr = new Array('ANDAMAN AND NICOBAR ISLANDS', 'ANDHRA PRADESH','ARUNACHAL PRADESH', 'ASSAM', 'BIHAR', 'CHANDIGARH','CHHATTISGARH', 'DADRA AND NAGAR HAVELI', 'GOA', 'GUJARAT','HARYANA', 'HIMACHAL PRADESH', 'JAMMU AND KASHMIR', 'JHARKHAND','KARNATAKA', 'KERALA', 'MADHYA PRADESH', 'MAHARASHTRA', 'MANIPUR','MEGHALAYA', 'MIZORAM', 'NAGALAND', 'ODISHA', 'PUDUCHERRY','PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU', 'TELANGANA','TRIPURA', 'UTTAR PRADESH','UTTARAKHAND', 'WEST BENGAL');


var s_a = new Array();
s_a[0]="";
s_a[1]=" NICOBAR | NORTH AND MIDDLE ANDAMAN | SOUTH ANDAMAN ";

s_a[2]=" ANANTAPUR | CHITTOOR | EAST GODAVARI | GUNTUR | CUDDAPAH | KRISHNA | KURNOOL | PRAKASAM | NELLORE | SRIKAKULAM | VISAKHAPATANAM | VIZIANAGARAM | WEST GODAVARI ";

s_a[3]=" ANJAW | CHANGLANG | DIBANG VALLEY | EAST KAMENG | EAST SIANG | KURUNG KUMEY | LOHIT | LONGDING | LOWER DIBANG VALLEY | LOWER SUBANSIRI | NAMSAI | PAPUM PARE | TAWANG | TIRAP | UPPER SIANG | UPPER SUBANSIRI | WEST KAMENG | WEST SIANG";

s_a[4]="BAKSA | BARPETA | BONGAIGAON | CACHAR | CHIRANG | DARRANG | DHEMAJI | DHUBRI | DIBRUGARH | DIMA HASAO | GOALPARA | GOLAGHAT | HAILAKANDI | JORHAT | KAMRUP | KAMRUP METROPOLITAN | KARBI ANGLONG | KARIMGANJ | KOKRAJHAR | LAKHIMPUR | MARIGAON | NAGAON | NALBARI | SIVASAGAR | SONITPUR | TINSUKIA | UDALGURI  ";

s_a[5]="ARARIA | ARWAL | AURANGABAD | BANKA | BEGUSARAI | BHAGALPUR | BHOJPUR | BUXAR | DARBHANGA | GAYA | GOPALGANJ | JAMUI | JEHANABAD | KAIMUR | KATIHAR | KHAGARIA | KISHANGANJ | LAKHISARAI | MADHEPURA | MADHUBANI | MUNGER | MUZAFFARPUR | NALANDA | NAWADA | PASHCHIM CHAMPARAN | PATNA | PURVI CHAMPARAN | PURNIA | ROHTAS | SAHARSA | SAMASTIPUR | SARAN | SHEIKHPURA | SHEOHAR | SITAMARHI | SIWAN | SUPAUL | VAISHALI ";

s_a[6]=" CHANDIGARH ";

s_a[7]=" BALOD | BALODA BAZAR | BALRAMPUR | BASTAR | BEMETARA | BIJAPUR | BILASPUR | DANTEWADA | DHAMTARI | DURG | GARIABAND | JANJGIR-CHAMPA | JASHPUR | KABIRDHAM | KANKER | KONDAGAON | KORBA | KORIYA | MAHASAMUND | MUNGELI | NARAYANPUR | RAIGARH | RAIPUR | RAJNANDGAON | SUKMA | SURAJPUR | SURGUJA ";

s_a[8]=" DADRA AND NAGAR HAVELI ";

s_a[9]=" NORTH GOA | SOUTH GOA";

s_a[10]=" AHMADABAD | AMRELI | ANAND | BANAS KANTHA | BHARUCH | BHAVNAGAR | DANG | DAHOD | GANDHINAGAR | JAMNAGAR | JUNAGADH | KACHCHH | KHEDA | MAHESANA | NARMADA | NAVSARI | PANCH MAHALS | PATAN | PORBANDAR | RAJKOT | SABAR KANTHA | SURAT | SURENDRANAGAR | TAPI | VADODARA | VALSAD";

s_a[11]=" AMBALA | BHIWANI | FARIDABAD | FATEHABAD | GURGAON | HISAR | JHAJJAR | JIND | KAITHAL | KARNAL | KURUKSHETRA | MAHENDRAGARH | MEWAT | PALWAL | PANCHKULA | PANIPAT | REWARI | ROHTAK | SIRSA | SONIPAT | YAMUNANAGAR ";

s_a[12]=" BILASPUR | CHAMBA | HAMIRPUR | KANGRA | KINNAUR | KULLU | LAHUL AND SPITI | MANDI | SHIMLA | SIRMAUR | SOLAN | UNA";

s_a[13]="ANANTNAG | BADGAM | BANDIPORA | BARAMULLA | DODA | GANDERBAL | JAMMU | KARGIL | KATHUA | KISHTWAR | KULGAM | KUPWARA | LEH LADAKH | POONCH | PULWAMA | RAJAURI | RAMBAN | REASI | SAMBA | SHOPIAN | SRINAGAR | UDHAMPUR";

s_a[14]="BOKARO | CHATRA | DEOGHAR | DHANBAD | DUMKA | EAST SINGHBUM | GARHWA | GIRIDIH | GODDA | GUMLA | HAZARIBAGH | JAMTARA | KHUNTI | KODERMA | LATEHAR | LOHARDAGA | PAKUR | PALAMU | RAMGARH | RANCHI | SAHEBGANJ | SARAIKELA KHARSAWAN | SIMDEGA | WEST SINGHBHUM ";

s_a[15]=" BAGALKOT | BENGALURU RURAL | BELGAUM | BELLARY | BENGALURU URBAN | BIDAR | BIJAPUR | CHAMARAJANAGAR | CHIKKABALLAPUR | CHIKMAGALUR | CHITRADURGA | DAKSHIN KANNAD | DAVANGERE | DHARWAD | GADAG | GULBARGA | HASSAN | HAVERI | KODAGU | KOLAR | KOPPAL | MANDYA | MYSORE | RAICHUR | RAMANAGARA | SHIMOGA | TUMKUR | UDUPI | UTTAR KANNAD | YADGIR";

s_a[16]=" ALAPPUZHA | ERNAKULAM | IDUKKI | KANNUR | KASARAGOD | KOLLAM | KOTTAYAM | KOZHIKODE | MALAPPURAM | PALAKKAD | PATHANAMTHITTA | THIRUVANANTHAPURAM | THRISSUR | WAYANAD";

s_a[17]="AGAR MALWA | ALIRAJPUR | ANUPPUR | ASHOKNAGAR | BALAGHAT | BARWANI | BETUL | BHIND | BHOPAL | BURHANPUR | CHHATARPUR | CHHINDWARA | DAMOH | DATIA | DEWAS | DHAR | DINDORI | GUNA | GWALIOR | HARDA | HOSHANGABAD | INDORE | JABALPUR | JHABUA | KATNI | KHANDWA | KHARGONE | MANDLA | MANDSAUR | MORENA | NARSINGHPUR | NEEMUCH | PANNA | RAISEN | RAJGARH | RATLAM | REWA | SAGAR | SATNA | SEHORE | SEONI | SHAHDOL | SHAJAPUR | SHEOPUR | SHIVPURI | SIDHI | SINGRAULI | TIKAMGARH | UJJAIN | UMARIA | VIDISHA ";

s_a[18]=" AHMEDNAGAR | AKOLA | AMRAVATI | AURANGABAD | BEED | BHANDARA | BULDHANA | CHANDRAPUR | DHULE | GADCHIROLI | GONDIA | HINGOLI | JALGAON | JALNA | KOLHAPUR | LATUR | MUMBAI | NAGPUR | NANDED | NANDURBAR | NASHIK | OSMANABAD | PALGHAR | PARBHANI | PUNE | RAIGAD | RATNAGIRI | SANGLI | SATARA | SINDHUDURG | SOLAPUR | THANE | WARDHA | WASHIM | YAVATMAL";

s_a[19]=" BISHNUPUR | CHANDEL | CHURACHANDPUR | IMPHAL EAST | IMPHAL WEST | SENAPATI | TAMENGLONG | THOUBAL | UKHRUL ";

s_a[20]=" EAST GARO HILLS | EAST JAINTIA HILLS | EAST KHASI HILLS | NORTH GARO HILLS | RI BHOI | SOUTH GARO HILLS | SOUTH WEST GARO HILLS | SOUTH WEST KHASI HILLS | WEST GARO HILLS | WEST JAINTIA HILLS | WEST KHASI HILLS";

s_a[21]=" AIZAWL | CHAMPHAI | KOLASIB | LAWNGTLAI | LUNGLEI | MAMIT | SAIHA | SERCHHIP";

s_a[22]=" DIMAPUR | KIPHIRE | KOHIMA | LONGLENG | MOKOKCHUNG | MON | PEREN | PHEK | TUENSANG | WOKHA | ZUNHEBOTO ";

s_a[23]="ANGUL | BALANGIR | BALESHWAR | BARGARH | BHADRAK | BOUDH | CUTTACK | DEOGARH | DHENKANAL | GAJAPATI | GANJAM | JAGATSINGHPUR | JAJPUR | JHARSUGUDA | KALAHANDI | KANDHAMAL | KENDRAPARA | KENDUJHAR | KHORDHA | KORAPUT | MALKANGIRI | MAYURBHANJ | NABARANGPUR | NAYAGARH | NUAPADA | PURI | RAYAGADA | SAMBALPUR | SONEPUR | SUNDARGARH ";

s_a[24]=" KARAIKAL | MAHE | PUDUCHERRY | YANAM";

s_a[25]=" AMRITSAR | BARNALA | BATHINDA | FARIDKOT | FATEHGARH SAHIB | FAZILKA | FEROZEPUR | GURDASPUR | HOSHIARPUR | JALANDHAR | KAPURTHALA | LUDHIANA | MANSA | MOGA | MUKTSAR | NAWANSHAHR | PATHANKOT | PATIALA | RUPNAGAR | S.A.S NAGAR | SANGRUR | TARN TARAN";

s_a[26]=" AJMER | ALWAR | BANSWARA | BARAN | BARMER | BHARATPUR | BHILWARA | BIKANER | BUNDI | CHITTAURGARH | CHURU | DAUSA | DHAULPUR | DUNGARPUR | GANGANAGAR | HANUMANGARH | JAIPUR | JAISALMER | JALORE | JHALAWAR | JHUNJHUNU | JODHPUR | KARAULI | KOTA | NAGAUR | PALI | PRATAPGARH | RAJSAMAND | SAWAI MADHOPUR | SIKAR | SIROHI | TONK | UDAIPUR";

s_a[27]="EAST SIKKIM | NORTH SIKKIM | SOUTH SIKKIM | WEST SIKKIM ";

s_a[28]="ARIYALUR | COIMBATORE | CUDDALORE | DHARMAPURI | DINDIGUL | ERODE | KANCHIPURAM | KANNIYAKUMARI | KARUR | KRISHNAGIRI | MADURAI | NAGAPATTINAM | NAMAKKAL | PERAMBALUR | PUDUKKOTTAI | RAMANATHAPURAM | SALEM | SIVAGANGA | THANJAVUR | THE NILGIRIS | THENI | THIRUVALLUR | THIRUVARUR | TIRUCHIRAPPALLI | TIRUNELVELI | TIRUPPUR | TIRUVANNAMALAI | THOOTHUKUDI | VELLORE | VILLUPURAM | VIRUDHUNAGAR ";

s_a[29]="ADILABAD | HYDERABAD | KARIMNAGAR | KHAMMAM | MAHBUBNAGAR | MEDAK | NALGONDA | NIZAMABAD | RANGAREDDI | WARANGAL ";

s_a[30]="DHALAI | GOMATI | KHOWAI | NORTH TRIPURA | SEPAHIJALA | SOUTH TRIPURA | UNAKOTI | WEST TRIPURA ";

s_a[31]=" AGRA | ALIGARH | ALLAHABAD | AMBEDKAR NAGAR | AMETHI | AMROHA | AURAIYA | AZAMGARH | BAGHPAT | BAHRAICH | BALLIA | BALRAMPUR | BANDA | BARABANKI | BAREILLY | BASTI | BIJNOR | BUDAUN | BULANDSHAHR | CHANDAULI | CHITRAKOOT | DEORIA | ETAH | ETAWAH | AYODHYA | FARRUKHABAD | FATEHPUR | FIROZABAD | GAUTAM BUDDHA NAGAR | GHAZIABAD | GHAZIPUR | GONDA | GORAKHPUR | HAMIRPUR | HAPUR | HARDOI | HATHRAS | JALAUN | JAUNPUR | JHANSI | KANNAUJ | KANPUR DEHAT | KANPUR NAGAR | KASGANJ | KAUSHAMBI | LAKHIMPUR KHERI | KUSHI NAGAR | LALITPUR | LUCKNOW | MAHARAJGANJ | MAHOBA | MAINPURI | MATHURA | MAU | MEERUT | MIRZAPUR | MORADABAD | MUZAFFARNAGAR | PILIBHIT | PRATAPGARH | RAE BARELI | RAMPUR | SAHARANPUR | SAMBHAL | SANT KABIR NAGAR | SANT RAVIDAS NAGAR | SHAHJAHANPUR | SHAMLI | SHRAVASTI | SIDDHARTH NAGAR | SITAPUR | SONBHADRA | SULTANPUR | UNNAO | VARANASI";

s_a[32]="ALMORA | BAGESHWAR | CHAMOLI | CHAMPAWAT | DEHRADUN | HARIDWAR | NAINITAL | PAURI GARHWAL | PITHORAGARH | RUDRA PRAYAG | TEHRI GARHWAL | UDHAM SINGH NAGAR | UTTAR KASHI ";

s_a[33]="24 PARAGANAS NORTH | 24 PARAGANAS SOUTH | BANKURA | BARDHAMAN | BIRBHUM | COOCHBEHAR | DARJEELING | DINAJPUR DAKSHIN | DINAJPUR UTTAR | HOOGHLY | HOWRAH | JALPAIGURI | MALDAH | MEDINIPUR EAST | MEDINIPUR WEST | MURSHIDABAD | NADIA | PURULIA";

function print_state(state_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(state_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select State','');
	option_str.selectedIndex = 0;
	for (var i=0; i<state_arr.length; i++) {
		option_str.options[option_str.length] = new Option(state_arr[i],state_arr[i]);
	}
}

function print_city(city_id, city_index){
	var option_str = document.getElementById(city_id);
	option_str.length=0;	// Fixed by Julian Woods
	option_str.options[0] = new Option('Select City','');
	option_str.selectedIndex = 0;
	var city_arr = s_a[city_index].split("|");
	for (var i=0; i<city_arr.length; i++) {
		option_str.options[option_str.length] = new Option(city_arr[i],city_arr[i]);
	}
}
