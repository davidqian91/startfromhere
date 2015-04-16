for $movie in doc('movie.xml')/movie/row
let $avgValue := 
      avg(
      for $rating in doc("review.xml")/review/row[Movie_ID = $movie/Movie_ID]/Rating
         return $rating
      )
where $avgValue = max(
for $resultRow in doc('movie.xml')/movie/row
   let $avgInside := 
      avg(
      for $ratingInside in doc("review.xml")/review/row[Movie_ID = $resultRow/Movie_ID]/Rating
         return $ratingInside
      )
return $avgInside
)
return  <result>{distinct-values(concat('movie: ', $movie/Title, ', averageRating: ',$avgValue))}</result>