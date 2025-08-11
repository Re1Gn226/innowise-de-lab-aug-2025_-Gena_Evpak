**PART 1: Для данной работы выбран сценарий: Сервис потоковой передачи музыки.** 
Эта система будет управлять артистами, альбомами, песнями, пользователями и пользовательскими плейлистами.

**PART 2: Проектирование Базы Данных и Документация**
**Идентификация Сущностей и Атрибутов:**
1. Артисты (Performers)
2. Альбомы (Albums)
3. Песни (Songs)
4. Пользователи (Users)
5. Плейлисты (Playlists)
6. Связь песен и плейлистов (PlaylistSongs)

**Проектирование Таблиц:**
1. Table Name: Performers
   **Description:** Хранит информацию об исполнителях
   **Atributes:**
   1. PerformerID: INTEGER, PK, NOT NULL, UNIQUE
   2. Name: VARCHAR(100), NOT NULL
   **Constraints**:
   1. PK_Performers: PRIMARY KEY (PerformerID)
   2. UQ_Performer: UNIQUE
2. Table Name: Albums
   **Descriprion**: Содержит информацию об альбомах
   **Atributes:**:
   1. AlbumID: INTEGER, PK, NOT NULL, UNIQUE
   2. Album_title: VARCHAR(255), NOT NULL
   3. PerformerID: INTEGER, FK (REFERENCES Performers), NOT NULL
   **Constraints**:
   1. PK_Albums: PRIMARY KEY (AlbumID)
   2. FK_Albums_Performers: FOREIGN KEY (PerformerID) REFERENCES Perfomers(PerformerID)
3. Table Name: Songs
   **Description:** Хранит информацию о песнях
   **Atributes:**
   1. SongID: INTEGER, PK, NOT NULL, UNIQUE
   2. Song_title: VARCHAR(255), NOT NULL
   3. PerformerID: INTEGER, FK (References Performers), NOT NULL
   4. Duration: INTEGER, NOT NULL
   **Constraints**:
   1. PK_Songs: PRIMARY KEY (SongsID)
   2. FK_Songs_Performers: FOREIGN KEY (PerformerID) REFERENCES Performers (PerformerID)
   3. CHK_Duration: CHECK (Duration) > 0
4. Table Name: Users
   **Description:** Хранит информацию о пользователях
   **Atributes:**
   1. UserID: INTEGER, PK, NOT NULL, UNIQUE
   2. Name: VARCHAR (100), NOT NULL
   3. Email: VARCHAR (255), UNIQUE
   4. Country: VARCHAR (100)
   5. BirthDate: DATE
   **Constraints**:
   1. PK_Users: PRIMARY KEY (UserID)
   2. UQ_Email: UNIQUE (Email)
5. Table Name: Playlists
   **Description:** Хранит информацию о пользовательских плейлистах
   **Atributes:**
   1. PlaylistID: INTEGER, PK, NOT NULL, UNIQUE
   2. Playlist_title: VARCHAR (255), NOT NULL
   3. UserID: INTEGER, FK (References Users), NOT NULL
   4. IsPublic: BOOLEAN, DEFAULT False
   **Constraints**:
   5. PK_Playlists: PRIMARY KEY (PlaylistID)
   6. FK_Playlists_Users: FOREIGN KEY (UserID) REFERENCES Songs (UserID)
6. Table Name: PlaylistsSongs
   **Description:** Связывает плейлисты и песни
   **Atributes:**
   1. **PlaylistSongID**: INTEGER, PK, NOT NULL, UNIQUE  
   2. **PlaylistID**: INTEGER, FK (REFERENCES Playlists), NOT NULL  
   3. **SongID**: INTEGER, FK (REFERENCES Songs), NOT NULL
   **Constraints**:
   4. PK_PlaylistSongs: PRIMARY KEY (PlaylistSongID)
   5. FK_PlaylistSongs_Playlists: FOREIGN KEY (PlaylistID) REFERENCES Playlists (PlaylistID)
   6. FK_PlaylistSongs_Songs: FOREIGN KEY (SongID) REFERENCES Songs (SongID)
   
**Взаимосвязи:**
1. Performers и Albums (Один-ко-Многим): Один исполнитель может выпустить множество альбомов, но каждый альбом принадлежит только одному исполнителю.
   Albums.PerformerID является внешним ключом, ссылающимся на Performers.PerformerID.
2. Performers и Songs (Один-ко-Многим): Один исполнитель может записать множество песен, но каждая песня связана с одним исполнителем.
   Songs.PerformerID является внешним ключом, ссылающимся на Performers.PerformerID.
3. Users и Playlists (Один-ко-Многим): Один пользователь может создать множество плейлистов, но каждый плейлист принадлежит только одному пользователю.
   Playlists.UserID является внешним ключом, ссылающимся на Users.UserID.
4. Playlists и Songs (Многие-ко-Многим через PlaylistSongs): Один плейлист может содержать множество песен, и одна песня может входить в множество плейлистов.
PlaylistSongs.PlaylistID является внешним ключом, ссылающимся на Playlists.PlaylistID.
PlaylistSongs.SongID является внешним ключом, ссылающимся на Songs.SongID.
 