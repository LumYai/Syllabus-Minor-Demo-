db = db.getSiblingDB("test_db");

db.minor.insertMany([
	{
		"_id": "arr_@cmu.ac.th",
		"first_name": "Areerat",
		"last_name": "Trongratsameethong",

	},
	{
		"_id": "narin@cmu.ac.th",
		"first_name": "na",
		"last_name": "rin",

	}
])