# Langchain + Chainlit app template for Venturenux LLM Course

## Branch 介紹

`election` branch 是以 langchainv3 為基礎，並使用 Mistral AI 的模型去建立美國總統大選聊天機械人，並演示一些基本的 prompt engineering 技考。
與 langchainv3 的主要分別

- 轉用 Mistral AI 的 LLM model
- 使用 Kaggle dataset library
- 使用 Langsmith 的 prompts 去管理 prompt

### Kaggle dataset

- [2024 US Presidential Election](https://www.kaggle.com/datasets/jpmiller/elections/data)
- `kaggle datasets download jpmiller/elections`

## 背景

為學生們提供一個 python app 的 framework

## Directory 結構

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

## 如何更新 requirements.txt

1. 傳統方法  
   `pip freeze > requirements.txt`
2. 只儲存頂層 package 的方法  
   `pipdeptree --warn silence | grep -E '^\w+' > requirements.txt`

## 基本 app 結構建議

![image](https://vbyedwxohhoyczqyvckv.supabase.co/storage/v1/object/public/buffer/service-archi.png?t=2024-06-23T10%3A36%3A33.342Z)

1. [Langsmith](https://smith.langchain.com/)
2. [Ploomber](https://ploomber.io/)
3. [Supabase](https://supabase.com/)

#### ⭐️ 關於使用 Supabase

Supabase 是近年 JS 界比較流行的 Backend-as-a-Service，直接競爭對手為 Firebase。  
Supabase 的核心服務為 Postgres 資料庫，用戶認證，檔案儲存(S3 兼容)等。  
💡 建議各位使用 Supabase 去處理用戶登入和 vector database。並以 Storage 去儲存任何檔案。  
⛔️ _Supabase 並不提供 docker deployment 的服務，關於 deployment 請看 Ploomer 部份_

- [使用 pg_vector 和 Supabase 去做 vector database 教學](https://python.langchain.com/v0.2/docs/integrations/vectorstores/supabase/)

#### ⭐️ 關於使用 Ploomer

Chainlit 本身是一個 React 的前端 UI，若要簡單地 deploy chainlit，可以使用 Ploomer，詳情請參考下面教學。

- [如何將 Chainlit deploy 到 Ploomber](https://docs.cloud.ploomber.io/en/latest/apps/chainlit.html)

## 參考

- [About Python project directory structure](https://python.plainenglish.io/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95)
