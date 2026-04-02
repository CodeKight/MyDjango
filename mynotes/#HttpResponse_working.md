

# NOTE:----------------------------------------------------------------------------  

# how HttpResponse work 

HttpResponse(content='', content_type=None, status=200, reason=None, charset=None)

🔑 Explanation
    - content → main data (string, HTML, JSON, etc.)
    - content_type → MIME type (e.g., "text/html", "application/json")
    - status → HTTP status code (e.g., 200, 404)
    - reason → optional status message
    - charset → encoding (e.g., "utf-8")

🧠 Important Point
    - You can pass up to 5 parameters (as shown),
    - but in practice, most people use 1–3 arguments.

✅ Example
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Hello", content_type="text/plain", status=200)


## you cannot pass two variable in the HttpResponse

HttpResponse(var1, var2)   # ❌ This is NOT for two content values

## concatinate them or pass them as a string 

1. Using string concatenation

HttpResponse(var1 + var2)

2. Using f-string (best)

HttpResponse(f"{var1} {var2}")

✅ HttpResponse accepts:

    String
    HTML (which is just a string)
    Bytes


👉 You can send JSON using HttpResponse, but only after converting it to a string.

    import json
    from django.http import HttpResponse

    def view(request):
        data = {"name": "John"}
        return HttpResponse(json.dumps(data), content_type="application/json")

✔ This works because:

    - json.dumps() → converts dict → string
    - Then HttpResponse sends that string

✅ So your understanding (refined)

    - HttpResponse → accepts string/HTML/bytes
    - JSON is allowed only after converting to string

    from django.http import JsonResponse
    return JsonResponse({"name": "John"})

👉 It automatically:

    Converts dict → JSON string
    Sets correct content_type

🧠 Final Rule (remember this)
    HttpResponse → raw content (string/HTML)
    JsonResponse → Python dict → JSON



## how does a 'GET' function work: 

🔥 Timeline (real understanding)

- User visits page → GET
- Django runs last line → renders HTML
- User fills form + clicks submit
- Browser sends POST request
- Django runs POST block
- Data is processed

## what is in the 'request' parameter ? 
👉 request = a box full of data sent by the browser

Inside the box:

- method (GET/POST)
- form data
- URL data
- headers


# levels of django: 
🧠 The Two Levels

✅ 1. Django-level change (Python side)

👉 Happens in your models.py

    default=
    validation
    form handling
    logic before saving

✔ No migration needed
✔ Runs when you call:

Todo.objects.create(...)

👉 Example:
priority = models.TextField(default="not important")

- Django fills this before sending to DB


✅ 2. Database-level change (DB schema)

👉 Happens in actual table structure (SQLite)

    Adding/removing columns
    Changing column type
    Constraints

✔ Requires migration
makemigrations
migrate
