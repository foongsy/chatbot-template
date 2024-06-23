# Langchain + Chainlit app template for Venturenux LLM Course

## 背景
為學生們提供一個python app的framework

## Directory結構 
```
.git/
_projectname_/          # 按項目名稱更改，建議將功能寫成module並置於此, 毋須__init__.py
data/                   # 可將raw或pre-process過的data此directory。（已被加入gitignore, 將不會被commit）
test/                   # Unit Testing
tool/                   # 其他
.gitignore              # 不被
Dockerfile              # 強烈建議使用Docker去將服務打包
README.md               # 本檔案
main.py                 # Google Cloud Run要求__main__置於main.py內
requirements.txt
```

## 如何更新requirements.txt
1. 傳統方法  
`pip freeze > requirements.txt` 
2. 只儲存頂層package的方法  
`pipdeptree --warn silence | grep -E '^\w+' > requirements.txt`

## 基本app結構建議
![image](https://vbyedwxohhoyczqyvckv.supabase.co/storage/v1/object/public/buffer/service-archi.png?t=2024-06-23T10%3A36%3A33.342Z)  

1. [Langsmith](https://smith.langchain.com/)
2. [Ploomber](https://ploomber.io/)
3. [Supabase](https://supabase.com/)

#### ⭐️ 關於使用Supabase
Supabase是近年JS界比較流行的Backend-as-a-Service，直接競爭對手為Firebase。  
Supabase的核心服務為Postgres資料庫，用戶認證，檔案儲存(S3兼容)等。  
💡 建議各位使用Supabase去處理用戶登入和vector database。並以Storage去儲存任何檔案。  
⛔️ *Supabase並不提供docker deployment的服務，關於deployment請看Ploomer部份*

* [使用pg_vector和Supabase去做vector database教學](https://python.langchain.com/v0.2/docs/integrations/vectorstores/supabase/)

#### ⭐️ 關於使用Ploomer
Chainlit本身是一個React的前端UI，若要簡單地deploy chainlit，可以使用Ploomer，詳情請參考下面教學。
* [如何將Chainlit deploy到Ploomber](https://docs.cloud.ploomber.io/en/latest/apps/chainlit.html)

## 參考
- [About Python project directory structure](https://python.plainenglish.io/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95)
