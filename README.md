# Adding_Holiday_API
Hi Siva, here is the API!

I did my testing using Postman but here are the curl commands as well:
For adding: curl -X POST -H "Content-Type: application/json" -d '{"num1": <NUM1>, "num2": <NUM2>}' http://localhost:5000/add
For holidays: curl http://localhost:5000/holiday/<HOLIDAYNAME>

The holidays that are currently stored:
        "christmas"
        "thanksgiving"
        "newyears"
        "mlk"
        "july4"
        "veterans"
