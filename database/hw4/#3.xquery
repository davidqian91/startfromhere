for $year in distinct-values(doc('movie.xml')/movie/row/year-from-date(Release_Date))
   let $totalValue := 
      count(
      for $detail in doc("movie.xml")/movie/row[year-from-date(Release_Date) = $year]
         return $detail
      )
order by $year
return <result>{distinct-values(concat('year: ', $year, ', number of movies: ',$totalValue))}</result>