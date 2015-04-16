(for $movie in doc('movie.xml')/movie/row
return if (contains($movie/Genre,"Crime"))
then <result>Genre:Crime, Movie_ID:{$movie/Movie_ID/text()}</result>
else ())
union
(for $movie in doc('movie.xml')/movie/row
return if (contains($movie/Genre,"Action"))
then <result>Genre:Action, Movie_ID:{$movie/Movie_ID/text()}</result>
else ())
union
(for $movie in doc('movie.xml')/movie/row
return if (contains($movie/Genre,"Sci-Fi"))
then <result>Genre:Sci-Fi, Movie_ID:{$movie/Movie_ID/text()}</result>
else ())