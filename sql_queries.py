# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id BIGSERIAL PRIMARY KEY, 
    start_time TIMESTAMP, 
    user_id BIGINT, 
    level VARCHAR(30), 
    song_id VARCHAR(100), 
    artist_id VARCHAR(100), 
    session_id BIGINT, 
    location VARCHAR(200), 
    user_agent VARCHAR(250)

);
""")


user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY, 
    first_name VARCHAR(50), 
    last_name VARCHAR(50), 
    gender CHAR(1), 
    level varchar(30)

);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR(100) PRIMARY KEY,
    title  VARCHAR(150), 
    artist_id VARCHAR(100), 
    year INTEGER, 
    duration FLOAT(10),
    constraint year check (year >= 0)

);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(100) PRIMARY KEY, 
    name VARCHAR(100), 
    location VARCHAR(100), 
    latitude FLOAT(8), 
    longitude FLOAT(8)

);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY, 
    hour INTEGER, 
    day INTEGER, 
    week INTEGER,
    month INTEGER, 
    year INTEGER,
    weekdaY INTEGER

);
""")

# INSERT RECORDS

# (my comment): adding additional on conflict for primary keys
# UPSERT statements

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(songplay_id) DO NOTHING;
""")


user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, songs.artist_id FROM songs 
JOIN artists ON songs.artist_id = artists.artist_id
WHERE songs.title = %s
AND artists.name = %s
AND songs.duration = %s
;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]