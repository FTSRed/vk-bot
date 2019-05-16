import vk_api
import time
import random
 
token = "твой токен"
 
vk = vk_api.VkApi(token="вставь свой токе группы сюда!")
 
vk._auth_token()
 
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "что ты умеешь?":
                vk.method("messages.send", {"peer_id": id, "message": "Мало чего(", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "саня":
                vk.method("messages.send", {"peer_id": id, "message": "Хуй соси!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "пока":
                vk.method("messages.send", {"peer_id": id, "message": "Пока! Возвращайся ещё!", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Этой команды я пока что не знаю, но может скоро узнаю!", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
