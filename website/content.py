from datetime import date

class Link:
    def __init__(self, name, target, date=None):
        self.name = name
        self.target = target
        self.date = date


pages = [
    Link('Home', 'index'),
    Link('About', 'about'),
    Link('Blog', 'blog'),
]

blogs = [
    Link('Example', 'example', date(2019, 6, 1)),
    Link('Example', 'example', date(2018, 6, 1)),
    Link('Example', 'example', date(2017, 6, 1)),
    Link('Example', 'example', date(2016, 6, 1)),
    Link('Example', 'example', date(2015, 6, 1)),
    Link('Example', 'example', date(2014, 6, 1)),
    Link('Example', 'example', date(2013, 6, 1)),
    Link('Example', 'example', date(2012, 6, 1)),
    Link('Example', 'example', date(2011, 6, 1)),
    Link('Example', 'example', date(2010, 6, 1)),
    Link('Example', 'example', date(2009, 6, 1)),
    Link('Example', 'example', date(2008, 6, 1)),
    Link('Example', 'example', date(2007, 6, 1)),
    Link('Example', 'example', date(2006, 6, 1)),
    Link('Example', 'example', date(2005, 6, 1)),
    Link('Example', 'example', date(2004, 6, 1)),
    Link('Example', 'example', date(2003, 6, 1)),
    Link('Example', 'example', date(2002, 6, 1)),
    Link('Example', 'example', date(2001, 6, 1)),
    Link('Example', 'example', date(2000, 6, 1)),
    Link('Example', 'example', date(1999, 6, 1)),
    Link('Example', 'example', date(1998, 6, 1)),
    Link('Example', 'example', date(1997, 6, 1)),
    Link('Example', 'example', date(1996, 6, 1)),
    Link('Example', 'example', date(1995, 6, 1)),
    Link('Example', 'example', date(1994, 6, 1)),
    Link('Example', 'example', date(1993, 6, 1)),
    Link('Example', 'example', date(1992, 6, 1)),
    Link('Example', 'example', date(1991, 6, 1)),
    Link('Example', 'example', date(1990, 6, 1)),
    Link('Example', 'example', date(1989, 6, 1)),
    Link('Example', 'example', date(1988, 6, 1)),
    Link('Example', 'example', date(1987, 6, 1)),
    Link('Example', 'example', date(1986, 6, 1)),
    Link('Example', 'example', date(1985, 6, 1)),
    Link('Example', 'example', date(1984, 6, 1)),
    Link('Example', 'example', date(1983, 6, 1)),
    Link('Example', 'example', date(1982, 6, 1)),
    Link('Example', 'example', date(1981, 6, 1)),
    Link('Example', 'example', date(1980, 6, 1)),
    Link('Example', 'example', date(1979, 6, 1)),
    Link('Example', 'example', date(1978, 6, 1)),
    Link('Example', 'example', date(1977, 6, 1)),
    Link('Example', 'example', date(1976, 6, 1)),
    Link('Example', 'example', date(1975, 6, 1)),
    Link('Example', 'example', date(1974, 6, 1)),
    Link('Example', 'example', date(1973, 6, 1)),
    Link('Example', 'example', date(1972, 6, 1)),
    Link('Example', 'example', date(1971, 6, 1)),
    Link('Example', 'example', date(1970, 6, 1)),
    Link('Example', 'example', date(1969, 6, 1)),
    Link('Example', 'example', date(1968, 6, 1)),
]

