# stein-movies
Movie hosting for STEiN-Net. 

## Requirements
- Python (NOT 3.0)
- That's about it. This project is run using basic python and bottlepy. Sqlite3 is handy.

## Setup
- $hostname/config/setup to scan /movies directory for files.
- All movies must be in (or linked to) /movies/name.extension
- To add a description, or change movie genre use put request to $hostname/config/$movie
- To delete a movie send a delete request to $hostname/config/$movie
- To add a new movie not present during the initial setup send a post command to $hostname/config/movie (not title, just movie)
### Movie post/put structure
 ```
 {
      "title":"The Title",
      "desc":"Movie description",
      "filename":"Filename of the movie- MUST BE PRESENT OR ERROR 404",
      "genre":"The movie genre"
  }
  ```
