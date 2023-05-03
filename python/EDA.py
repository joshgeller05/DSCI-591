import duckdb
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# create a connection to a file called 'database.db'
try:
    con = duckdb.connect('database.db')
    rated_podcasts = con.sql("select * from podcasts where average_rating >= 0").df()
    total = 0
    for (colname,colval) in rated_podcasts.iteritems():
        if colname == "ratings_count":
            for x in colval:
                if  "K" not in x:
                    total += int(x)
                else:
                    formatted = float(x[0:x.find('K')])
                    total += (1000 * formatted)
    print(f'Total Number of Rated Podcasts: {int(rated_podcasts.shape[0]):,}')
    print(f'Total Number of Podcast Ratings: {int(total):,}')
except duckdb.CatalogException as e:
    print("Can't find database, download from teams and place in python/ directory")