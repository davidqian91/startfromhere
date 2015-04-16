for $i in fn:doc("review.xml")/review/row,
    $m in fn:doc("movie.xml")/movie/row[Movie_ID=$i/Movie_ID],
    $v in fn:doc("reviewer.xml")/reviewer/row[Reviewer_ID=$i/Review_ID]
where $m/Title = 'Goodfellas' or $m/Title = 'Inception'
return <result>{distinct-values(concat('title: ', $m/Title, ', reviewer: ',$v/Reviewer_Name))}</result>