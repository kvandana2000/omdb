# Omdb api access script

This script helps you to access OMDB Movie database API and return movie rating.
Api key need to be generated from http://www.omdbapi.com/ and then should be passed as argument to this program

### Execution

Make sure that you have docker installed on your linux box in order to run the below code

```sh
$ git clone https://github.com/AnupKumar-ops/omdb.git
$ cd omdb
$ docker build -t "yourimage:tag" .
```

### Testing

```sh
docker run yourimage:tag python /app/app.py

output:
Please pass movie title and api key as arguments. For ref check below example
**********Example********
docker run mycustomimage:tag python /app/app.py avengers  api_key

```

### Sample Example

``` sh
It produces output as response code and rating of the movie as below

request success: 200
Rotten Tomatoes rating :91%
```
