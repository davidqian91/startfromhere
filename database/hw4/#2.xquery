(:#2:)

let $rows := (doc("movie.xml")/movie/row)
for $row in $rows
where $row/Writer = 'Christopher Nolan'
and $row/Director = 'Christopher Nolan'
order by $row/Release_Date
return <result> {distinct-values(concat('Movie_ID:',$row/Movie_ID,', Release_Date:',$row/Release_Date)) }</result>
