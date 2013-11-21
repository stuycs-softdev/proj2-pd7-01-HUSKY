proj2-pd7-01-HUSKY
==================
Nancy, Hanson, Isabella, CBass

Project Idea: Chess conversion. 
	      Find API with chess records and convert from new notation to old notation.
We need:
   API - Wiki - Bios - 
   Search Bar - Bootstrap
   Screenscraping chess games to convert from current notation to old notation.
   Rules -screenscrape/api
   
Dividing by Features:

1) Design
2) API usage
API info is at http://en.wikipedia.org/w/api.php
3) Screenscrape
We take Wikipedia articles pertaining to chess, and convert instances of algebraic notation into descriptive notation.
4) Conversion
Because the state of the board will not necessarily be obvious, we will attempt to guess which instances of notation in the preceding part of the article precede the move being currently parsed, but this may fail. To account for this eventuality, we will make available the option of literal translation, which still entails displaying a descriptive-notation-flavored version of the original notation, but with the implicit details not filled in.