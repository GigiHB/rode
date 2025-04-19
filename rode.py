from requests import Session, Response
from credentials import login_url, coaches_url, headers, payload 
import json

session = Session()

def do_login(session: Session):
	response = session.post(login_url, data = payload, headers=headers)

	if response.status_code == 200:
		print("Login exitoso")
		return session
	else:
		print("error en login")
		print(response.text)
		return None

def get_coaches_info():
	logged = do_login(session)
	if logged:
		r = logged.post(coaches_url, headers = headers)
		print("Status code:", r.status_code)
		print("Respuesta:", r.text)
		if r.status_code == 200:
			coaches_data = r.json()
			coaches_list = []
			for coach in coaches_data.get("data", []):
				nombre = coach.get("emp_first_name", "N/A")
				apellido = coach.get("emp_last_name", "N/A")
				fecha_nacimiento = coach.get("emp_dob", "N/A")
				telefono = coach.get("emp_primary_phone", "N/A")
				correo = coach.get("emp_email", "N/A")

				coach_info = {
            		"nombre": nombre,
            		"apellido": apellido,
            		"Birthday": fecha_nacimiento,
            		"Cel": telefono,
            		"e-mail": correo
            	}

				coaches_list.append(coach_info)
			return coaches_list
		else:
			print("error al obtener datos")
			return None

rode_coaches = get_coaches_info()

if rode_coaches:
	with open("rode_coaches_list.json", "w", encoding="utf-8") as f:
		json.dump(rode_coaches, f, ensure_ascii=False, indent=4)
else:
	print("No se logró obtener datos")
