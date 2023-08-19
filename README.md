# Hammer

API для Авторизации и Инвайт-кодов

Этот API предоставляет функционал для авторизации по номеру телефона и управления инвайт-кодами.

Эндпоинт: /authorize/
Метод: POST
Описание: Этот эндпоинт позволяет отправить запрос на авторизацию пользователя по номеру телефона.
Параметры запроса:
json

{
  "phone_number": "string"
}
Успешный ответ:
json

{
  "message": "Verification code sent successfully"
}
Ошибка:
json

{
  "phone_number": ["This field is required."]
}

Эндпоинт: /verify_code/
Метод: POST
Описание: Этот эндпоинт позволяет подтвердить код верификации после получения.

Параметры запроса:
json

{
  "phone_number": "string",
  "verification_code": "string"
}
Успешный ответ:
json

{
  "message": "Verification successful"
}
Ошибка:
json

{
  "phone_number": ["This field is required."],
  "verification_code": ["This field is required."]
}

Эндпоинт: /activate_invite_code/{phone_number}/
Метод: POST
Описание: Этот эндпоинт позволяет активировать инвайт-код для указанного номера телефона.

Параметры запроса:
json

{
  "invite_code": "string"
}
Успешный ответ:
json

{
  "message": "Invite code activated successfully"
}
Ошибка:
json

{
  "invite_code": ["This field is required."]
}

Эндпоинт: /user_profile/{phone_number}/
Метод: GET
Описание: Этот эндпоинт позволяет получить профиль пользователя по номеру телефона.

Успешный ответ:
json

{
  "phone_number": "string",
  "verification_code": "string",
  "invite_code": "string",
  "activated_invite": "string"
}
Ошибка:
json

{
  "detail": "Not found."
}

Эндпоинт: /users_with_invite/{phone_number}/
Метод: GET
Описание: Этот эндпоинт позволяет получить список пользователей, которые ввели инвайт-код текущего пользователя.

Успешный ответ:
json

[
  {
    "phone_number": "string"
  }
]
Ошибка:
json

{
  "detail": "Not found."
}