USE DB_Henkflix;

START TRANSACTION;

-- ----------------------------------------------------------------
-- Testdata

--
-- Test data: subscription
--

INSERT INTO `subscription` (`subscription_id`, `subscription_price`, `video_quality`) VALUES
(1, 7.99, 'SD'),
(2, 10.99, 'HD'),
(3, 13.99, 'UHD');

--
-- Test data: account
--

INSERT INTO `account` (`account_id`, `email`, `username`, `password`, `payment_method`, `blocked`, `subscription_id`) VALUES
(1, 'john.doe@example.com', 'john_doe', 'hashed_password', 'credit_card', NULL, 1),
(2, 'jane.smith@example.com', 'jane_smith', 'hashed_password', 'paypal', NULL, 2),
(3, 'alice.jones@example.com', 'alice_jones', 'hashed_password', 'debit_card', NULL, 1),
(4, 'bob.white@example.com', 'bob_white', 'hashed_password', 'credit_card', 1, 3),
(5, 'mary.green@example.com', 'mary_green', 'hashed_password', 'paypal', NULL, 2),
(6, 'sam.brown@example.com', 'sam_brown', 'hashed_password', 'debit_card', NULL, 1),
(7, 'emily.wilson@example.com', 'emily_wilson', 'hashed_password', 'credit_card', NULL, 3),
(8, 'charlie.rogers@example.com', 'charlie_rogers', 'hashed_password', 'paypal', NULL, 1),
(9, 'olivia.hall@example.com', 'olivia_hall', 'hashed_password', 'debit_card', 1, 2),
(10, 'david.lee@example.com', 'david_lee', 'hashed_password', 'credit_card', NULL, 3),
(11, 'sophie.collins@example.com', 'sophie_collins', 'hashed_password', 'paypal', NULL, 2),
(12, 'max.miller@example.com', 'max_miller', 'hashed_password', 'debit_card', NULL, 1);

--
-- Test data: profile
--

INSERT INTO `profile` (`profile_id`, `profile_image`, `profile_child`, `language`, `account_id`) VALUES
(1, '/path/to/image', 0, 'DUTCH', 1),
(2, '/path/to/image', 0, 'DUTCH', 1),
(3, NULL, NULL, 'DUTCH', 2),
(4, NULL, NULL, 'ENGLISH', 2),
(5, NULL, NULL, 'ENGLISH', 3),
(6, NULL, NULL, 'GERMAN', 2),
(7, NULL, 1, 'GERMAN', 4),
(8, NULL, NULL, 'DUTCH', 5),
(9, NULL, 1, 'DUTCH', 6),
(10, NULL, NULL, 'DUTCH', 8),
(11, NULL, NULL, 'DUTCH', 8),
(12, NULL, 1, 'ENGLISH', 7),
(13, NULL, NULL, 'DUTCH', 8),
(14, NULL, NULL, 'DUTCH', 9),
(15, NULL, NULL, 'DUTCH', 10),
(16, NULL, NULL, 'ENGLISH', 12),
(17, NULL, NULL, 'ENGLISH', 11),
(18, NULL, NULL, 'GERMAN', 12),
(19, NULL, 1, 'GERMAN', 7),
(20, NULL, NULL, 'DUTCH', 5),
(21, NULL, 1, 'DUTCH', 6),
(22, NULL, NULL, 'DUTCH', 5),
(23, NULL, NULL, 'DUTCH', 10),
(24, NULL, 1, 'ENGLISH', 4);

--
-- Test data: agepreference
--

INSERT INTO `agepreference` (`agepreference_id`, `profile_id`, `agerestriction`) VALUES
(1, 1, 'SIX_YEARS'),
(2, 1, 'TWELVE_YEARS'),
(3, 2, 'SIX_YEARS'),
(4, 2, 'SIXTEEN_YEARS');

--
-- Test data: genrespreference
--

INSERT INTO `genrespreference` (`genrepreference_id`, `profile_id`, `genre`) VALUES
(1, 1, 'ACTION'),
(2, 1, 'FANTASY'),
(3, 2, 'ACTION'),
(4, 2, 'SCIFI');

--
-- Test data: indicationpreference
--

INSERT INTO `indicationpreference` (`indicationpreference_id`, `profile_id`, `indication`) VALUES
(1, 1, 'VIOLENCE'),
(2, 1, 'PROFANITY_USAGE'),
(3, 2, 'VIOLENCE'),
(4, 2, 'FEAR');

--
-- Test data: movie
--

INSERT INTO `movie` (`movie_id`, `title`, `movie_duration`, `age_restriction`) VALUES
(1, 'The Shawshank Redemption', 142, 'SIXTEEN_YEARS'),
(2, 'The Godfather', 175, 'ALL_AGES'),
(3, 'Pulp Fiction', 154, 'ALL_AGES'),
(4, 'The Dark Knight', 152, 'SIXTEEN_YEARS'),
(5, 'Schindlers List', 195, 'SIXTEEN_YEARS'),
(6, 'Inception', 148, 'SIXTEEN_YEARS'),
(7, 'Fight Club', 139, 'SIXTEEN_YEARS'),
(8, 'Forrest Gump', 142, 'ALL_AGES'),
(9, 'The Matrix', 136, 'SIX_YEARS'),
(10, 'The Silence of the Lambs', 118, 'TWELVE_YEARS'),
(11, 'The Green Mile', 189, 'SIXTEEN_YEARS'),
(12, 'The Godfather: Part II', 202, 'TWELVE_YEARS'),
(13, 'unavailable movie', 150, 'SIX_YEARS');

--
-- Test data: serie
--

INSERT INTO `serie` (`serie_id`, `serie_name`, `age_restriction`) VALUES
(1, 'Stranger Things', 'SIXTEEN_YEARS'),
(2, 'The Crown', 'SIXTEEN_YEARS'),
(3, 'Breaking Bad', 'SIXTEEN_YEARS'),
(4, 'Friends', 'ALL_AGES'),
(5, 'Black Mirror', 'SIXTEEN_YEARS'),
(6, 'The Mandalorian', 'TWELVE_YEARS'),
(7, 'Money Heist', 'SIXTEEN_YEARS'),
(8, 'Narcos', 'SIXTEEN_YEARS'),
(9, 'The Witcher', 'SIXTEEN_YEARS'),
(10, 'Peaky Blinders', 'ALL_AGES'),
(11, 'The Office', 'ALL_AGES'),
(12, 'Game of Thrones', 'SIXTEEN_YEARS'),
(13, 'unavailable series', 'SIX_YEARS');

--
-- Test data: genres
--

INSERT INTO `genres` (`genres_id`, `genre`, `movie_id`, `serie_id`) VALUES
(1, 'ACTION', 1, NULL),
(2, 'ADVENTURE', 1, NULL),
(3, 'SCIFI', 1, NULL),
(4, 'DRAMA', 1, NULL),
(5, 'COMEDY', 1, NULL),
(6, 'THRILLER', 1, NULL),
(7, 'HORROR', 1, NULL),
(8, 'ROMANCE', 1, NULL),
(9, 'FANTASY', 1, NULL),
(10, 'MYSTERY', 1, NULL),
(11, 'ANIMATION', 1, NULL),
(12, 'DOCUMENTARY', 1, NULL),
(13, 'ACTION', 2, NULL),
(14, 'ADVENTURE', 2, NULL),
(15, 'SCIFI', 2, NULL),
(16, 'DRAMA', 2, NULL),
(17, 'COMEDY', 2, NULL),
(18, 'THRILLER', 2, NULL),
(19, 'HORROR', 2, NULL),
(20, 'ROMANCE', 2, NULL),
(21, 'FANTASY', 2, NULL),
(22, 'MYSTERY', 2, NULL),
(23, 'ANIMATION', 2, NULL),
(24, 'DOCUMENTARY', 2, NULL),
(25, 'ACTION', NULL, 1),
(26, 'ADVENTURE', NULL, 1),
(27, 'SCIFI', NULL, 1),
(28, 'DRAMA', NULL, 1),
(29, 'COMEDY', NULL, 1),
(30, 'THRILLER', NULL, 1),
(31, 'HORROR', NULL, 1),
(32, 'ROMANCE', NULL, 1),
(33, 'FANTASY', NULL, 1),
(34, 'MYSTERY', NULL, 1),
(35, 'ANIMATION', NULL, 1),
(36, 'DOCUMENTARY', NULL, 1),
(37, 'ACTION', NULL, 2),
(38, 'ADVENTURE', NULL, 2),
(39, 'SCIFI', NULL, 2),
(40, 'DRAMA', NULL, 2),
(41, 'COMEDY', NULL, 2),
(42, 'THRILLER', NULL, 2),
(43, 'HORROR', NULL, 2),
(44, 'ROMANCE', NULL, 2),
(45, 'FANTASY', NULL, 2),
(46, 'MYSTERY', NULL, 2),
(47, 'ANIMATION', NULL, 2),
(48, 'DOCUMENTARY', NULL, 2);

--
-- Test data: episode
--

INSERT INTO `episode` (`episode_id`, `title`, `episode_duration`, `serie_id`) VALUES
(1, 'The Beginning', 45, 1),
(2, 'Secrets Unveiled', 42, 1),
(3, 'Into the Abyss', 40, 1),
(4, 'Hidden Truths', 38, 1),
(5, 'Fallen Heroes', 41, 1),
(6, 'Deception', 37, 1),
(7, 'Betrayal', 44, 1),
(8, 'Rising Tensions', 39, 1),
(9, 'The Reckoning', 43, 1),
(10, 'Final Stand', 36, 1),
(11, 'Epiphany', 40, 1),
(12, 'Closure', 42, 1),
(13, 'New Horizons', 50, 2),
(14, 'Lost and Found', 48, 2),
(15, 'Dawn of Destiny', 52, 2),
(16, 'Echoes of the Past', 45, 2),
(17, 'Fading Light', 47, 2),
(18, 'Shattered Dreams', 49, 2),
(19, 'Whispers in the Wind', 46, 2),
(20, 'Crimson Skies', 51, 2),
(21, 'Dystopian Realms', 50, 2),
(22, 'The Final Chapter', 53, 2),
(23, 'Fragments of Reality', 48, 2),
(24, 'Redemption', 50, 2),
(25, 'Beginnings', 35, 3),
(26, 'Lost Memories', 32, 3),
(27, 'Echoing Voices', 38, 3),
(28, 'Forgotten Tales', 40, 3),
(29, 'Veil of Shadows', 36, 3),
(30, 'Whispers in the Dark', 37, 3),
(31, 'Fading Echoes', 39, 3),
(32, 'Twisted Fate', 34, 3),
(33, 'Shattered Illusions', 33, 3),
(34, 'Fractured Reality', 36, 3),
(35, 'Spectral Visions', 35, 3),
(36, 'Eternal Twilight', 31, 3);

--
-- Test data: watchlist
--

INSERT INTO `watchlist` (`watchlist_id`, `movie_id`, `serie_id`, `profile_id`) VALUES
(1, 1, NULL, 1),
(2, NULL, 1, 1);

--
-- Test data: subtitle
--

INSERT INTO `subtitle` (`subtitle_id`, `language`, `subtitle_location`, `movie_id`, `episode_id`) VALUES
(1, 'ENGLISH', '/path/to/subtitles/movie1_eng.srt', 1, NULL),
(2, 'DUTCH', '/path/to/subtitles/movie1_nl.srt', 1, NULL),
(3, 'FRENCH', '/path/to/subtitles/movie1_fr.srt', 1, NULL),
(4, 'SPANISH', '/path/to/subtitles/movie1_es.srt', 1, NULL),
(5, 'GERMAN', '/path/to/subtitles/movie1_de.srt', 1, NULL),
(6, 'ITALIAN', '/path/to/subtitles/movie1_it.srt', 1, NULL),
(7, 'JAPANESE', '/path/to/subtitles/movie1_jp.srt', 1, NULL),
(8, 'CHINESE', '/path/to/subtitles/movie1_cn.srt', 1, NULL),
(9, 'RUSSIAN', '/path/to/subtitles/movie1_ru.srt', 1, NULL),
(10, 'PORTUGUESE', '/path/to/subtitles/movie1_pt.srt', 1, NULL),
(11, 'ARABIC', '/path/to/subtitles/movie1_ar.srt', 1, NULL),
(12, 'KOREAN', '/path/to/subtitles/movie1_kr.srt', 1, NULL),
(13, 'ENGLISH', '/path/to/subtitles/movie2_eng.srt', 2, NULL),
(14, 'DUTCH', '/path/to/subtitles/movie2_nl.srt', 2, NULL),
(15, 'FRENCH', '/path/to/subtitles/movie2_fr.srt', 2, NULL),
(16, 'SPANISH', '/path/to/subtitles/movie2_es.srt', 2, NULL),
(17, 'GERMAN', '/path/to/subtitles/movie2_de.srt', 2, NULL),
(18, 'ITALIAN', '/path/to/subtitles/movie2_it.srt', 2, NULL),
(19, 'JAPANESE', '/path/to/subtitles/movie2_jp.srt', 2, NULL),
(20, 'CHINESE', '/path/to/subtitles/movie2_cn.srt', 2, NULL),
(21, 'RUSSIAN', '/path/to/subtitles/movie2_ru.srt', 2, NULL),
(22, 'PORTUGUESE', '/path/to/subtitles/movie2_pt.srt', 2, NULL),
(23, 'ARABIC', '/path/to/subtitles/movie2_ar.srt', 2, NULL),
(24, 'KOREAN', '/path/to/subtitles/movie2_kr.srt', 2, NULL),
(25, 'ENGLISH', '/path/to/subtitles/episode1_eng.srt', NULL, 1),
(26, 'DUTCH', '/path/to/subtitles/episode1_nl.srt', NULL, 1),
(27, 'FRENCH', '/path/to/subtitles/episode1_fr.srt', NULL, 1),
(28, 'SPANISH', '/path/to/subtitles/episode1_es.srt', NULL, 1),
(29, 'GERMAN', '/path/to/subtitles/episode1_de.srt', NULL, 1),
(30, 'ITALIAN', '/path/to/subtitles/episode1_it.srt', NULL, 1),
(31, 'JAPANESE', '/path/to/subtitles/episode1_jp.srt', NULL, 1),
(32, 'CHINESE', '/path/to/subtitles/episode1_cn.srt', NULL, 1),
(33, 'RUSSIAN', '/path/to/subtitles/episode1_ru.srt', NULL, 1),
(34, 'PORTUGUESE', '/path/to/subtitles/episode1_pt.srt', NULL, 1),
(35, 'ARABIC', '/path/to/subtitles/episode1_ar.srt', NULL, 1),
(36, 'KOREAN', '/path/to/subtitles/episode1_kr.srt', NULL, 1),
(37, 'ENGLISH', '/path/to/subtitles/episode13_eng.srt', NULL, 13),
(38, 'DUTCH', '/path/to/subtitles/episode13_nl.srt', NULL, 13),
(39, 'FRENCH', '/path/to/subtitles/episode13_fr.srt', NULL, 13),
(40, 'SPANISH', '/path/to/subtitles/episode13_es.srt', NULL, 13),
(41, 'GERMAN', '/path/to/subtitles/episode13_de.srt', NULL, 13),
(42, 'ITALIAN', '/path/to/subtitles/episode13_it.srt', NULL, 13),
(43, 'JAPANESE', '/path/to/subtitles/episode13_jp.srt', NULL, 13),
(44, 'CHINESE', '/path/to/subtitles/episode13_cn.srt', NULL, 13),
(45, 'RUSSIAN', '/path/to/subtitles/episode13_ru.srt', NULL, 13),
(46, 'PORTUGUESE', '/path/to/subtitles/episode13_pt.srt', NULL, 13),
(47, 'ARABIC', '/path/to/subtitles/episode13_ar.srt', NULL, 13),
(48, 'KOREAN', '/path/to/subtitles/episode13_kr.srt', NULL, 13);

COMMIT;
