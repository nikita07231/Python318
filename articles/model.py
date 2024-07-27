import pickle
import os.path


class Article:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.director})"


class ArticleModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.articles = self.load_data()

    def __str__(self):
        return f"{self.articles}"

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название": article.title,
            'режиссёра': article.director,
            'год выпуска': article.year,
            'длительность': article.duration
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.articles, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

