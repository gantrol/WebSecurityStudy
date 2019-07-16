import base64

jwt_string = u"""
{
  "alg": "None"
}
{
  "iat": 1564109140,
  "admin": "true",
  "user": "Tom"
}
"""
jwt_byte = base64.b64encode(bytes(jwt_string, "ascii"))
print(jwt_byte)

# ew0KICAiYWxnIjogIk5vbmUiDQp9.ew0KICAiaWF0IjogMTU2NDEwOTE0MCwNCiAgImFkbWluIjogImZhbHNlIiwNCiAgInVzZXIiOiAiVG9tIg0KfQ==