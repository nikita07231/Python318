def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserUnterface:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действие со статьями:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определённого фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия:")
        # print("=" * 50)
        return user_answer

    @add_title("Добавление  фильма")
    def add_user_article(self):
        dict_article = {
            "название": None,
            'режиссёра': None,
            'год выпуска': None,
            'длительность': None
        }
        # print(" Создание статьи ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} фильма: ")
        # print("=" * 50)
        return dict_article

    @add_title("Список статей")
    def show_all_articles(self, articles):
        # print(" Список статей ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        # print("=" * 50)

    @add_title("Ввод названия статьи")
    def get_user_article(self):
        user_article = input("Введите название фильма: ")
        return user_article

    @add_title("Просмотр фильма")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} статьи - {article[key]}")

    @add_title("Сообщение об ошибки")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_article(self, article):
        print(f"Фильм {article} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")