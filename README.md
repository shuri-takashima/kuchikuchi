
##versions

Django	3.2  
Pillow	8.2.0  
asgiref	3.3.4  
beautifulsoup4	4.9.3  
django-axes	5.14.0  
django-bootstrap4	2.3.1  
django-cleanup	5.1.0  
django-ipware	3.0.2  
pip	21.0.1  
psycopg2-binary	2.8.6  
pytz	2021.1  
setuptools	54.2.0  
soupsieve	2.2.1  
sqlparse	0.4.1  
 ***
##機能
ログイン周りの機能（django.contrib.auth使用中)  
mp4,webmのファイルアップロード  
follow機能  
good機能  
***
##追加したい機能
*** 
###2021

***5/3 Fileuploadのcssを変更したい。（大幅変更が予想される。)***  
    modelform の fileupload のcss変更すること。  
    今現在では、cssを変更するとfileuploadのcssが変更できないため、  
    別モデルにfileuploadを持たせたモデルをForeignKeyでContentに持たせる。
    もしくは、  
    記述量が多くなるかもしれないが、ModelFormを使わずにゴリ押しの実装が必要。
    



