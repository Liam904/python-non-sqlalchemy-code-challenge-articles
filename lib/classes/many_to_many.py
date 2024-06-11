from collections import Counter

class Article:
    all = []

    def __init__(self, author, magazine, title: str):
        assert len(title) > 0
        self.author = author
        self.magazine = magazine
        self.__title = title
        author.add_author(self)
        magazine.add_article(self)
        Article.all.append(self)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value


class Author:
    def __init__(self, name: str):
        assert len(name) > 0 and len(name) < 50
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 0 < len(value) < 50:
            raise ValueError("Name must be between 1 and 49 characters")
        self.__name = value

    def add_author(self, article):
        self.__articles.append(article)

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(set(article.magazine for article in self.__articles))

    def add_article(self, magazine, title):
        ##Aggregate methods
        return Article(self, magazine, title)

    def topic_areas(self):
        topics =  list(set(article.magazine.category for article in self.__articles))
        return topics if topics else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__articles = []
        self.__contributors = set()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self.__name = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self.__category = value

    def add_article(self, article):
        self.__articles.append(article)
        self.__contributors.add(article.author)

    def articles(self):
        return self.__articles

    def contributors(self):
        return list(self.__contributors)

    def article_titles(self):
        titles = [article.title for article in self.__articles]
        return titles if titles else None

    def contributing_authors(self):
        count = Counter(article.author for article in self.__articles)
        contributors = [author for author, count in count.items() if count > 2]
        return contributors if contributors else None
    
  