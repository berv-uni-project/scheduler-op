# Scheduler OP

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/384d23564c1d46e9b6d55999e0c91608)](https://app.codacy.com/app/berviantoleo/scheduler-op?utm_source=github.com&utm_medium=referral&utm_content=berv-uni-project/scheduler-op&utm_campaign=Badge_Grade_Settings)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fberv-uni-project%2Fscheduler-op.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fberv-uni-project%2Fscheduler-op?ref=badge_shield)

This is scheduler or timetabling that implements 3 algorithm. This web app using simple interface.

1. Hill Climbing

2. Simulated Annealing

3. Genetic Algorithm

## Build Status

| Docker | Django - Test |
|:------:|:-------------:|
| ![Django CI](https://github.com/berv-uni-project/scheduler-op/workflows/Django%20CI/badge.svg) | ![Docker](https://github.com/berv-uni-project/scheduler-op/workflows/Docker/badge.svg) |



## Program Demo

Link : https://scheduler-op.herokuapp.com/

This app have deployed to heroku. If have some issue, please send me an issue. :)

## Deploy

### Docker

* Create file `.env`

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_db_url
DEBUG_MODE=False
```

* Config `docker-compose.yml`

* Run: `docker-compose build && docker-compose up -d`

## Dependency

Look at [Requirements.txt](./requirements.txt).

* Django 2.1
* Python 3 or above
* dj-database-url 0.5.0
* dj-static 0.0.6
* psycopg2 2.7.6

## Developer

1. Amir - 13514017 - [Profile](https://github.com/greenword000)

2. Jeremia Jason Lasiman - 13514021 - [Profile](https://github.com/JeremiaJ)

3. Bervianto Leo Pratama - 13514047 - [Profile](https://github.com/berviantoleo)

4. Richard Welianto - 13514051 - [Profile](https://github.com/RichardWellianto)

5. M. Az-zahid Adhitya Silparensi - 13514095 - [Profile](https://github.com/Azzahid)

## LICENSE

MIT

```markdown
MIT License

Copyright (c) 2017 Bervianto Leo Pratama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fberv-uni-project%2Fscheduler-op.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fberv-uni-project%2Fscheduler-op?ref=badge_large)
