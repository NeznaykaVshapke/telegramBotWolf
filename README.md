# telegramBotWolf
Невероятный, потрясающий криптоБот!
Для запуска свой токен необходимо ввести в поле token в файле main.
Функционал: 
поддерживаемые криптовалюты: "bitcoin", "ethereum", "dogecoin", поддерживаемые валюты: "usd", "eur", "rub"
Что можно делать с ботом?
1) Как только откроете бота -- напишите "start", Вам будет предложено пройти небольшую регистрацию. После чего Вы должны будете подтвердить свои данные (бот ответит, отталкиваясь от вашего возраста).
2) Если написать в бота название криптовалюты, он выведет её текущий курс в долларах.
3) Из более инересного -- конвертер валют -- напишите "konverter", Вам будет предложено выбрать криптовалюту, валюту и значение
4) Изюминка бота -- уведомления, вы можете написать nCripto и настроить уведомления так, чтобы они пришли, когда валюта превысит какое-то, установленное Вами пороговое значение. Эти уведомления будут приходить регулярно через промежуток времени, который Вы зададите. Отключаются уведомления -- "stop nCripto"
5) Кроме уведомлений на криптовалюты, Вы можете настроить и обычные уведомления. Для этого напишите "notice", введите текст уведомления и время через сколько надо его прислать. 
Такими образом, реализовано два вида уведомлений
6) Так же есть деловые заметки для самых деловых физтехов. Для этого напишите "notes". Вызывая функцию заново, Вы можете дополнять заметку. Если Вы не хотите дополнять заметку, а просто посмотреть -- напишите "get notes". тобы очистить заметку, напишите -- "stop notes".
7) Конечно же, в боте есть кнопка "help"
Каждое вводимое Вами слово обрабатывается. Если Вы введете слово неправильно, то Вам будет вынесено предупреждение и Вам предложат написать заново. Если просится числовое значение, ввод букв недопустим. Обращаю Ваше внимание, значения, вводимые в бота могут быть дробными, но время должно быть целым (это --число минут). 
Однако, чтобы проверяющему не приходилось долго ждать, он может ввести "0.1" -- это исключение из правила о целом числе минут.


