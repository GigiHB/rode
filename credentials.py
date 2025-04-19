login_url = "https://api.ezfit.io/index.php/embed/api/login"
coaches_url = "https://api.ezfit.io/index.php/embed/api/employee/show"

headers = {
	'Referer': login_url,
	"Accept": "application/json",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

payload = {
	'email': 'mariagrosval@gmail.com',
	'branch_id': 488,
	'password': 'GISYLU4EVER',
	'gym_id': 247
}