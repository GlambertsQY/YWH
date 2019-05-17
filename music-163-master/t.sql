use test;
create table comments (
	MUSIC_ID varchar(10) primary key,
    COMMENTS varchar(100),
    DETAILS varchar(100),
    foreign key(MUSIC_ID) references musics(MUSIC_ID)
);
create table musics(
	MUSIC_ID varchar(10) primary key, 
    MUSIC_NAME varchar(100), 
    ALBUM_ID varchar(100),
    foreign key(ALBUM_ID) references albums(ALBUM_ID)
);
create table albums(
	ALBUM_ID varchar(10),
    ARTIST_ID varchar(10),
    primary key(ALBUM_ID),
    foreign key(ARTIST_ID) references artists(ARTIST_ID)
);
create table artists(
	ARTIST_ID varchar(10) primary key, 
    ARTIST_NAME varchar(100)
);
use test;
delete from artists;
delete from artists where ARTIST_ID like "6%";
drop table comments;
drop table musics;
drop table albums;

select * from artists;