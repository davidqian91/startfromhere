let $cr := doc('movie.xml')/movie/row[contains(Genre,"Crime")]/Movie_ID
let $ar := doc('movie.xml')/movie/row[contains(Genre,"Action")]/Movie_ID
let $sc := doc('movie.xml')/movie/row[contains(Genre,"Sci-Fi")]/Movie_ID
return 
<result>
<Genre>Crime</Genre>
<Movies>{string-join($cr," ")}</Movies>
<Genre>Action</Genre>
<Movies>{string-join($ar," ")}</Movies>
<Genre>Sci</Genre>
<Movies>{string-join($sc," ")}</Movies>
</result>