[![codecov](https://codecov.io/gh/namantam1/tempfiler/branch/main/graph/badge.svg?token=I9T16R1WYJ)](https://codecov.io/gh/namantam1/tempfiler)
[![Django CI](https://github.com/namantam1/tempfiler/actions/workflows/django.yml/badge.svg)](https://github.com/namantam1/tempfiler/actions/workflows/django.yml)

# Tempfiler

This is simple teampory file storage where you can store your file upto 30 days.


## Usage

POST https://namantam1.pythonanywhere.com/upload/ 

Body -
`{
"expire_on": "2020-06-05T00:00",
"myfile": "path/to/file.png"
}
`

Response - 
`
{
    "id": 3,
    "timestamp": "2021-06-28T15:50:08.569322+05:30",
    "expire_on": "2021-06-28T15:55:00+05:30",
    "myfile": "http://namantam1.pythonanywhere.com/media/84ee4e1938.png"
}
`

The uploaded file while be deleted after expire on time.

### To delete file immediatetly

DELETE https://namantam1.pythonanywhere.com/get_delete/[id]/ 

