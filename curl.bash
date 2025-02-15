curl -X POST "http://135.125.133.105:8060/" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@E:\docker-test\ubuntu\app\tmp.zip"

curl -X POST "http://localhost:8060/" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@E:\docker-test\ubuntu\app\tmp.zip"
