(:#1:)
let $time := (doc("movie.xml")/movie/row/Runtime)
let $m_id := (doc("movie.xml")/movie/row/Movie_ID)
for $t at $pos in $time
where $t = max($time)
return <id> {distinct-values($m_id[$pos])}</id>