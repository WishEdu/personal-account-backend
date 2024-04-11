from dataclasses import fields
from backend.entities.forms import RegistrationForm


CREATE_USER_QUERY = f"""
INSERT INTO users 
({', '.join([i.name for i in fields(RegistrationForm)])})
VALUES ({', '.join(['%s' for i in range(len(fields(RegistrationForm)))])})
RETURNING id"""
