"""Önce proje kökünde python train.py çalıştırın. Sonra bu dosyayı açın."""
from pathlib import Path
import sys, joblib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from train import features
import pandas as pd

bundle=joblib.load(Path(__file__).with_name('model.joblib'))
def tahmin_et(text):
    if not text.strip(): raise ValueError('Boş mesaj analiz edilemez.')
    X=pd.DataFrame([features(text)],columns=bundle['features'])
    return 'spam' if bundle['tree'].predict(X)[0] else 'normal'

if __name__=='__main__':
    print('SpamGuard temel Python aracı. İngilizce SMS içindir. Çıkış: /q')
    while True:
        try:
            text=input('Mesaj: ')
            if text.strip()=='/q': break
            print(f'Modelin tahmini: {tahmin_et(text)}')
        except ValueError as error: print(error)
        except (EOFError,KeyboardInterrupt): break
