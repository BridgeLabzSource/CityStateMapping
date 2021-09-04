indian_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat",
                 "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam",
                 "Pimpri-Chinchwad", "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Ranchi",
                 "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar", "Varanasi", "Srinagar",
                 "Aurangabad", "Dhanbad", "Gurgaon", "Amritsar", "Navi Mumbai", "Allahabad", "Howrah", "Gwalior",
                 "Jabalpur", "Coimbatore", "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota", "Salem", "Chandigarh",
                 "Guwahati", "Solapur", "Hubli–Dharwad", "Mysore", "Tiruchirappalli", "Bareilly", "Aligarh", "Tiruppur",
                 "Moradabad", "Jalandhar", "Bhubaneswar", "Warangal", "Mira-Bhayandar", "Jalgaon", "Guntur",
                 "Thiruvananthapuram", "Bhiwandi", "Saharanpur", "Gorakhpur", "Bikaner", "Amravati", "Noida",
                 "Jamshedpur", "Bhilai", "Cuttack", "Firozabad", "Kochi", "Nellore", "Bhavnagar", "Dehradun",
                 "Durgapur", "Asansol", "Rourkela", "Nanded", "Kolhapur", "Ajmer", "Akola", "Gulbarga", "Jamnagar",
                 "Ujjain", "Loni", "Siliguri", "Jhansi", "Ulhasnagar", "Jammu", "Sangli-Miraj & Kupwad", "Mangalore",
                 "Erode", "Belgaum", "Kurnool", "Ambattur", "Rajahmundry", "Tirunelveli", "Malegaon", "Gaya",
                 "Tirupati", "Udaipur", "Kakinada", "Davanagere", "Kozhikode", "Maheshtala", "Rajpur Sonarpur",
                 "Bokaro", "South Dumdum", "Bellary", "Patiala", "Gopalpur", "Agartala", "Bhagalpur", "Muzaffarnagar",
                 "Bhatpara", "Panihati", "Latur", "Dhule", "Rohtak", "Sagar", "Korba", "Bhilwara", "Berhampur",
                 "Muzaffarpur", "Ahmednagar", "Mathura", "Kollam", "Avadi", "Kadapa", "Anantapuram", "Kamarhati",
                 "Bilaspur", "Sambalpur", "Shahjahanpur", "Satara", "Bijapur", "Rampur", "Shimoga", "Chandrapur",
                 "Junagadh", "Thrissur", "Alwar", "Bardhaman", "Kulti", "Nizamabad", "Parbhani", "Tumkur", "Khammam",
                 "Uzhavarkarai", "Bihar Sharif", "Panipat", "Darbhanga", "Bally", "Aizawl", "Dewas", "Ichalkaranji",
                 "Karnal", "Bathinda", "Jalna", "Eluru", "Barasat", "Kirari Suleman Nagar", "Purnia", "Satna", "Mau",
                 "Sonipat", "Farrukhabad", "Durg", "Imphal", "Ratlam", "Hapur", "Arrah", "Anantapur", "Karimnagar",
                 "Etawah", "Ambarnath", "North Dumdum", "Bharatpur", "Begusarai", "New Delhi", "Gandhidham",
                 "Baranagar", "Tiruvottiyur", "Pondicherry", "Sikar", "Thoothukudi", "Rewa", "Mirzapur", "Raichur",
                 "Pali", "Ramagundam", "Silchar", "Haridwar", "Vijayanagaram", "Tenali", "Nagercoil", "Sri Ganganagar",
                 "Karawal Nagar", "Mango", "Thanjavur", "Bulandshahr", "Uluberia", "Katni", "Sambhal", "Singrauli",
                 "Nadiad", "Secunderabad", "Naihati", "Yamunanagar", "Bidhannagar", "Pallavaram", "Bidar", "Munger",
                 "Panchkula", "Burhanpur", "Kharagpur", "Dindigul", "Gandhinagar", "Hospet", "Nangloi Jat", "Malda",
                 "Ongole", "Deoghar", "Chapra", "Puri", "Haldia", "Khandwa", "Nandyal", "Morena", "Amroha", "Anand",
                 "Bhind", "Bhalswa Jahangir Pur", "Madhyamgram", "Bhiwani", "Berhampore", "Ambala", "Morbi", "Fatehpur",
                 "Raebareli", "Khora, Ghaziabad", "Chittoor", "Bhusawal", "Orai", "Bahraich", "Phusro", "Vellore",
                 "Mehsana", "Raiganj", "Sirsa", "Danapur", "Serampore", "Sultan Pur Majra", "Guna", "Jaunpur", "Panvel",
                 "Shivpuri", "Surendranagar Dudhrej", "Unnao", "Chinsurah", "Alappuzha", "Kottayam", "Machilipatnam",
                 "Shimla", "Adoni", "Udupi", "Katihar", "Proddatur", "Mahbubnagar", "Saharsa", "Dibrugarh", "Jorhat",
                 "Hazaribagh", "Hindupur", "Nagaon", "Hajipur", "Sasaram", "Giridih", "Bhimavaram", "Port Blair",
                 "Kumbakonam", "Bongaigaon", "Dehri", "Madanapalle", "Siwan", "Bettiah", "Ramgarh", "Tinsukia",
                 "Guntakal", "Srikakulam", "Motihari", "Dharmavaram", "Medininagar", "Gudivada", "Phagwara",
                 "Pudukkottai", "Hosur", "Narasaraopet", "Suryapet", "Miryalaguda", "Tadipatri", "Karaikudi",
                 "Kishanganj", "Jamalpur", "Ballia", "Kavali", "Tadepalligudem", "Amaravati", "Buxar", "Tezpur",
                 "Jehanabad", "Aurangabad", "Gangtok", "Vasco Da Gama", "Praygraj", "Bombay", "Madras"]


def get_cities_name():
    return indian_cities