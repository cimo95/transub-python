from googletrans import Translator
import re
import sys


def proses(_a, _b='', _c='', _d=2, _e=50, _f='█', _g="\r"):
    _h = len(_a)

    def setProses(_i):
        _j = ("{0:." + str(_d) + "f}").format(100 * (_i / float(_h)))
        _k = int(_e * _i // _h)
        _l = _f * _k + '-' * (_e - _k)
        print(f'\r{_b} [{_l}] {_j}% {_c}', end=_g)
    setProses(0)
    for _m, _n in enumerate(_a):
        yield _n
        setProses(_m + 1)
    print()


def transub(_a, _b, _c):
    _d = open(_a, 'r')
    _e = open(_a.split('.')[-2]+'-translated.ass', 'w')
    _e.write(';Base translation generator by TranSub')
    _f = _d.readlines()
    print('Menterjemahkan : '+_a)
    for _g in proses(_f, _b='Memproses : ', _c='selesai', _g=''):
        if _g[0:8] == 'Dialogue':
            _h = _g.split(',')
            _i = Translator()
            _j = re.sub('{.+?}', '', _h[9])
            _h[9] = _i.translate(_j, src=_b, dest=_c).text
            _e.write(','.join(_h)+'\n')
        else:
            _e.write(_g)
    print('File berhasil diproses, dan disimpan ke "' +
          _a.split('.')[-2]+'-translated.ass"')
    _e.close()


def main(_a):
    import googletrans
    _b = Translator()
    if (sys.argv[1] == "?bahasa"):
        for _c, _d in googletrans.LANGUAGES.items():
            print('Bahasa : '+_d+' --> kode : '+_c)
        sys.exit()
    try:
        _e, _f, _g = _a[1], _a[2], _a[3]
        try:
            _b.translate('coba', src=_f, dest=_g)
        except Exception as _h:
            print('Terjadi kesalahan : ' +
                  _b.translate(str(_h), dest='id').text)
            sys.exit()
        transub(_e, _f, _g)
    except Exception as _i:
        print("""
Pemakaian : """+_a[0].split('\\')[-1]+""" <namafile> <id_bahasa_sumber> <id_bahasa_tujuan>
Contoh : """+_a[0].split('\\')[-1]+""" "D:\mbahmu\life of pi.ass" en id
Keterangan : id_bahasa diisi dengan kode bahasa sesuai dengan i18n, atau gunakan perintah "?bahasa" untuk menampilkan bahasa dan kodenya. 
        """)
        print('Terjadi masalah : '+_b.translate(str(_i), dest='id').text)
        sys.exit()


if __name__ == "__main__":
    print('--- TranSub simple v.1.0 ---\n')
    main(sys.argv)
