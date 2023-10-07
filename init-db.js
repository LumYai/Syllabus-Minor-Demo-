db = db.getSiblingDB("test_db");

db.minor.insertMany([
	{
		"_id": "030",
		"faculty_name": "Humanities",
		"branch_name": "Vietnamese",
		"year_active": ["all_year"],
		"minor_subject": {"ปีที่หลักสูตรใช้งาน": ["ทุกชั้นปี"]}

	},
	{
		"_id": "003",
		"faculty_name": "Humanities",
		"branch_name": "German",
		"year_active": ["all_year"],
		"minor_subject": {}

	}
])

db.course.insertMany([
	{
		"_id": "030101",
		"name_course": "FUNDAMENTAL VIETNAMESE 1",
		"credit_course": "3",

	},
	{
		"_id": "030102",
		"name_course": "FUNDAMENTAL VIETNAMESE 2",
		"credit_course": "3",

	},
	{
		"_id": "030111",
		"name_course": "VIETNAMESE SOCIETY AND CULTURE",
		"credit_course": "3",

	},
	{
		"_id": "030251",
		"name_course": "VIETNAMESE FOR TOURISM",
		"credit_course": "3",

	},
	{
		"_id": "030261",
		"name_course": "VIETNAMESE FOR BUSINESS",
		"credit_course": "3",

	},
])