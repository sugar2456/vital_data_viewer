# リポジトリについて

ウェアラブルデバイス（fitbit）のデータを収集、参照するシステムになります。

fitbit web APIを利用してデバイスのデータを収集し、アプリケーションデバイスに保存します。

## 機能

### 認証機能
firebaseによる認証を実装
web/mobile両方で対応できるようにする

### fitbit user登録画面
fitbit userを登録する画面

### fitbit user一覧画面
fitbit userを一覧参照する画面  
検索できるようにする

### fitbit user削除画面
fitbit userを削除する画面

### fitbit user トークン保存機能
fitbit userによるトークンを保存する機能  
userの生体情報を取得する際に  
トークンを利用して取得する  

### vaital_data蓄積機能
クライアントから生体情報の取得のリクエストがあった場合、  
Fitbit Web APIを代理にリクエストし、情報をDBに蓄積する。  
クライアントに生体情報を返す  

以下の情報を登録する
- sleep
- Blood Oxygen Saturation (SpO2)
- Temperature
- Activity Intraday by Interval
- Breathing Rate Intraday by Interval
- Heart Rate Intraday by Interval


### vaital_data表示機能
過去の生体情報を表示する機能  
アプリケーションサーバに生体情報が保存されていない場合、  
itbit Web APIを代理にリクエストし、情報をDBに蓄積、  
クライアントに表示する。

以下の情報を登録する
- sleep
- Blood Oxygen Saturation (SpO2)
- Temperature
- Activity Intraday by Interval
- Breathing Rate Intraday by Interval
- Heart Rate Intraday by Interval

### ユーザ参照画面
### ユーザ編集画面

## システム構成

webサーバ: nginx  
frontendサーバ： nextjs  
backendサーバ： fast API  
dbサーバ： mysql  

## Fitbit Web APIについて

ユーザーからのリクエストを受け取ったとき、  
まずデータベース（MySQL）をチェックします。

リクエストに対応するデータがデータベースに存在し、  
かつ最新（例えば、過去1時間以内に更新されたもの）であれば、  
そのデータをクライアントに返します。

データベースにデータが存在しないか、データが古い場合は、  
その時点でFitbit Web APIにリクエストを送ります。  
APIから取得したデータはデータベースに保存（既存のデータは更新）し、  
そのデータをクライアントに返します。

