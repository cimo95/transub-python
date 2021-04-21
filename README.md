# transub-python
Bulk base-translator untuk subtitle Advanced Substation Alpha (*.ass)

## Instalasi

Sebelum menggunakan **transub.py** install terlebih dulu modul ` googletrans `

```cmd
pip install googletrans
```

## Pemakaian
```
<namafile> <id_bahasa_sumber> <id_bahasa_tujuan>
```

```cmd
transub.py "file_subtitle.ass" en id
```

## Catatan
- Proses penterjemahan memerlukan waktu, tergantung koneksi yang tersedia.
- Jika mengalami masalah pada proses / hasil penterjemahan, periksa versi terbaru (pre-release) googletrans di [https://pypi.org/project/googletrans/#history](https://pypi.org/project/googletrans/#history)
- id_bahasa diisi dengan kode bahasa sesuai dengan [i18n](https://metacpan.org/pod/I18N::LangTags::List), atau gunakan perintah "` ?bahasa `" untuk menampilkan bahasa dan kodenya. 
