# Disred - Key-Value Memory Database
DiSred - Key-Value Memory Database | Kelompok 4

## Program DiJalankan
    - Load data backup
    - Load database, kalau belum ada buat data kosong
    - {}

## 1. Get All
    - Endpoint: "/"
    - Method: GET
    - Return Object

## 2. Get
    - Endpoint: "/{key}/one"
    - Method: GET
    - Return string

## 3. Insert / Update
    - Endpoint: "/"
    - Method: POST / PUT
    - Request Body:
        - key: str
        - value: str
    - Ketika insert, masukkan data ke backup.json
    - Ketika Update, update data di backup.json
    - Return "OK"

## 4. Delete
    - Endpoint: "/"
    - Method: DELETE
    - Ketika delete, hapus data di backup.json
    - Return "OK"

## 5. Flush
    - Endpoint: "/flush"
    - Method: DELETE
    - Ketika flush, hapus data di backup.json
    - Return "OK"

## 6. Get Keys
    - Endpoint: "/keys"
    - Method: GET
    - Return array berisikan keys yang ada