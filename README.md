# Adding_Holiday_API
Hi Siva, here is the API!

I did my testing using Postman but here are the curl commands as well:

For adding: curl -X POST -H "Content-Type: application/json" -d '{"num1": <NUM1>, "num2": <NUM2>}' http://localhost:5000/add

For holidays: curl http://localhost:5000/holiday/<HOLIDAYNAME>

I was unsure of how to structure the input for the addition. I did it this way because it seemed to make it easier to catch the error if a string is put in. However, if a string is used without quotes it gets a JSON error.
{
        "num1": 100,
        "num2": 3
}

The holidays that are currently stored:
        "christmas"
        "thanksgiving"
        "newyears"
        "mlk"
        "july4"
        "veterans"
