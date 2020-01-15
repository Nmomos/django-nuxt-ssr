# django-nuxt-ssr
Django + Vue.js + Nuxt.js でSSRアプリを作る
![title](https://github.com/mila411/django-nuxt-ssr/blob/master/title.png)

[Django + Vue.js + Nuxt.js でSSRアプリを作る](hhttps://nmomos.com/tips/2020/01/16/django-vue-nuxt-ssr/ "Django + Vue.js + Nuxt.js でSSRアプリを作る")

# 実行方法
## 1. リポジトリのクローン
```bash
https://github.com/mila411/django-nuxt-ssr.git
```
***
## 2. バックエンド実行
### 2-1. パッケージのインストール
```bash
cd server
pip install -r requirements.txt
```
### 2-2. マイグレート
```bash
python manage.py migrate
```
### 2-3. 開発サーバ起動
```bash
python manage.py runserver
```
***
## 3. フロントエンド実行

### 3-1. セットアップ
```bash
npm install
```
### 3-2. 実行
```basu
npm run dev
```
