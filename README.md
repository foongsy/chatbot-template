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

## Reference
- [About Python project directory structure](https://python.plainenglish.io/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95)
