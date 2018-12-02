import wikipedia
import wolframalpha
language = "en"
wolfram_app_id = input("Enter your WolframAlpha APP ID: ")
while True:
    query = input("Query: ")

    try:
        client = wolframalpha.Client(wolfram_app_id)
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
    except:
	wikipedia.set_lang(language)
        print(wikipedia.summary(query))
