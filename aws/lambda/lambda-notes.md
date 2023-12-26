# Running lambda
1. from python runtime env
```bash
python lambda_template.py
```

2. using aws lambda docker
```bash
docker run -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 \
  --entrypoint /aws-lambda/aws-lambda-rie \
  docker-image:test \
    /usr/local/bin/python -m awslambdaric app.handler
```
3. aws lambda withe nodemon for dynamic reload
```bash
npx nodemon -w ./ -s SIGINT -x "docker run -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 \
  --entrypoint /aws-lambda/aws-lambda-rie \
  docker-image:test \
    /usr/local/bin/python -m awslambdaric app.handler"
```

### Run
```bash
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
```